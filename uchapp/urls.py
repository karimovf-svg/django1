from django.urls import path, include
from uchapp.views import *

urlpatterns = [
    path('bye/', bye),
    path('bye2/', bye2),
    path('bye3/', bye3)
]
