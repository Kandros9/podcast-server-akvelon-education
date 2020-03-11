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
import time


class AverageColorView(APIView):
    permission_classes = ()

    def post(self, request):
        image_urls = request.data.get('image_urls')

        dominant_colors = []

        for image_url in image_urls:
            start_time = time.time()
            resp = requests.get(image_url)
            print("--- %s seconds ---" % (time.time() - start_time))
            start_time = time.time()
            img = Image.open(BytesIO(resp.content))
            print("--- %s seconds ---" % (time.time() - start_time))
            start_time = time.time()
            img2=img.resize((1,1))
            print("--- %s seconds ---" % (time.time() - start_time))
            start_time = time.time()

            color=img2.getpixel((0,0))
            print("--- %s seconds ---" % (time.time() - start_time))
            start_time = time.time()
            dominant_colors.append(color)
            print(color)

        return Response({"dominant_colors": dominant_colors}, status=status.HTTP_200_OK)


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
