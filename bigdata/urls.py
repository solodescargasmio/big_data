
from django.urls import path
from .views import inicio,consulta,mostrar,principal

urlpatterns = [
   path('inicio/',principal),
   path('consulta/',consulta),
   path('inicio/mostrar/',mostrar),
   path('prueba/',principal),
   
]