from django.urls import path, include
from sam_config.views import *

urlpatterns = [
    path('sam/', sam),
    path('sam2/', sam2),
    path('sam3/', sam3)
]
