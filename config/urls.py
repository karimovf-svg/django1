from django.contrib import admin
from django.urls import path, include
from configapp.views import *
from sam_config.views import *
from uchapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', include('configapp.urls')),
    path('app2/', include('sam_config.urls')),
    path('app3/', include('uchapp.urls'))
]
