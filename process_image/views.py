from io import BytesIO

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from PIL import Image
import cv2
from sklearn.cluster import KMeans
from collections import Counter
import numpy as np


class AverageColorView(APIView):
    permission_classes = ()

    def get(self, request):
        #image_url = request.data.get('image_url')
        image_url = 'https://cdn-images-1.listennotes.com/podcasts/in-pursuit-from-glassdoor-glassdoor-oq9VMd3XrOi-XL3IjyeScFK.1400x1400.jpg'

        resp = requests.get(image_url)
        img = Image.open(BytesIO(resp.content))
        img_arr = np.array(img)

        return Response({"dominant_color": get_dominant_color(img_arr)}, status=status.HTTP_200_OK)


def get_dominant_color(image, k=4, image_processing_size=(25, 25)):

    # resize image if new dims provided
    if image_processing_size is not None:
        image = cv2.resize(image, image_processing_size,
                           interpolation=cv2.INTER_AREA)

    # reshape the image to be a list of pixels
    image = image.reshape((image.shape[0] * image.shape[1], 3))

    # cluster and assign labels to the pixels
    clt = KMeans(n_clusters=k)
    labels = clt.fit_predict(image)

    # count labels to find most popular
    label_counts = Counter(labels)

    # subset out most popular centroid
    dominant_color = clt.cluster_centers_[label_counts.most_common(1)[0][0]]

    return list([int(round(color)) for color in dominant_color])
