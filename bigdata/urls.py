
from django.urls import path
from .views import inicio,pi

urlpatterns = [
   path('inicio/',inicio),
   path('pi/',pi),
]