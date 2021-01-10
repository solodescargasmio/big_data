
from django.urls import path
from .views import inicio,pi,consulta

urlpatterns = [
   path('inicio/',inicio),
   path('pi/',pi),
   path('consulta/',consulta),
]