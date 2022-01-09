from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    # created paths urls and using actively
    path('', views.index, name='index'),
    #path('index1', views.index1, name='index1'),
    
]


