from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso



# Create your views here.

def inicio(request):
    #documentoTexto = 'Inicio'
    #return HttpResponse(documentoTexto)
    return render(request, "AppCoder/inicio.html")

def curso(self):

    curso = Curso(nombre = 'Desarrollo Web', comision= 12312)
    curso.save()
    documentoTexto = f'Curso {curso.nombre} Comision {curso.comision}'

    return HttpResponse(documentoTexto)

def profesor(request):
    return render (request, "AppCoder/profesores.html")
    #documentoTexto = f'Vista de profesores'
    #return HttpResponse(documentoTexto)

def estudiante(request):
    return render (request, "AppCoder/estudiantes.html")

def entregable(request):
    return render (request, "AppCoder/entregables.html")

def cursos(request):
    return render (request, "AppCoder/cursos.html")
