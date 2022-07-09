from django.urls import path
from .views import *


urlpatterns = [
    path('cursos/', cursos),
    path('curso/', curso),
    path('profesor/', profesor),
    path('estudiante/', estudiante),
    path('entregable/', entregable),
    
   
    path('', inicio, name = 'Inicio'),
    path('profesor/', profesor, name = 'Profesores'),
    path('cursos/', curso, name = 'Cursos'),
    path('estudiante/', estudiante, name = 'Estudiantes'),
    path('entregable/', entregable, name = 'Entregables'),
    path('cursoFormulario/', cursoFormulario , name = 'cursoFormulario'),
    path('busquedaComision/', busquedaComision , name = 'busquedaComision'),
    path('buscar/', buscar , name = 'buscar'),

]