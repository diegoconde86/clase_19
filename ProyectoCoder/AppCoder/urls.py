from django.urls import path
from .views import *


urlpatterns = [
    path('cursos/', cursos),
    path('curso/', curso),
    path('profesor/', profesor),
    path('estudiante/', estudiante),
    path('entregable/', entregable),
    
   
    path('', inicio)
]