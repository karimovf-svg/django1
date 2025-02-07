from django.urls import path, include
from configapp.views import *

urlpatterns = [
    path('hello1/', hello1),
    path('hello2/', hello2),
    path('hello3/', hello3)
]
