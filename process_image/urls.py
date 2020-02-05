from django.urls import path
from rest_framework import routers

from process_image.views import *


router = routers.DefaultRouter()
urlpatterns = [
    path("get_color", AverageColorView.as_view(), name="get_color_view"),
]
urlpatterns += router.urls
