from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template

def saludar(request):
    return HttpResponse('Hola Mundo')

def segundo_saludo(request):
    return HttpResponse('Hola Mundo 2')

def diaDeHoy(request):
    texto = f'El día de hoy es :'+ str(datetime.today())
    return HttpResponse(texto)

def saludoConNombre(self, nombre):
    return HttpResponse('<h1>Mi nombre es: </h1>' + nombre)

def probandoHtml(self):
    miArchivo = open('/media/eduardo/Datos/repo_personal/Django/Projecto1/Plantillas/template.html')
    plantilla = Template(miArchivo.read())
    contexto = Context()
    documento = plantilla.render(contexto)

    return HttpResponse(documento)


def probandoHtml2(self):
    nombre = 'Eduardo'
    apellido = 'Montero'
    notas = [6,7,8,9,8,9,8,9]

    diccionario = { 'nombre': nombre,
                    'apellido': apellido
                    }
                    
    miHtml = open('/media/eduardo/Datos/repo_personal/Django/Projecto1/Plantillas/template.html')
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context(diccionario)
    documento = plantilla.render(miContexto)

    return HttpResponse(documento)