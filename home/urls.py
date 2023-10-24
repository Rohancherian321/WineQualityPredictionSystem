from django.urls import path,include
from . views import *

urlpatterns = [
  
     path('', predict_wine_quality, name='predict_wine_quality'),
]
