from django.http import HttpResponse
from AppCoder.models import Curso


# Create your views here.
def curso(self):

    curso = Curso(nombre = 'Desarrollo Web', comision= 12312)
    curso.save()
    documentoTexto = f'Curso {curso.nombre} Comision {curso.comision}'

    return HttpResponse(documentoTexto)