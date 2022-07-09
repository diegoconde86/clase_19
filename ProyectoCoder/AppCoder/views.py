from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso
from AppCoder.forms import CursoForm


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

""" def cursoFormulario(request):

    if (request.method == 'POST'):
        nombre = request.POST.get('curso')
        comision = request.POST.get('comision')
        curso = Curso (nombre = nombre, comision = comision)
        curso.save()

        return render(request, 'AppCoder/inicio.html')

    return render(request, 'AppCoder/cursoFormulario.html') VISTA PARA FORMULARIO HTML"""

def cursoFormulario(request):

    if (request.method == 'POST'):
        form = CursoForm(request.POST)
        print(form)
        if form.is_valid():
            info = form.cleaned_data
            print(info)
            nombre = info['nombre']
            comision = info['comision']
            curso = Curso (nombre = nombre, comision = comision)
            curso.save()

            return render(request, 'AppCoder/inicio.html')
    else:
        form = CursoForm()
    return render(request, 'AppCoder/cursoFormulario.html', {'formulario':form})


def busquedaComision(request):
    return render(request, 'AppCoder/busquedaComision.html')

def buscar(request):
    #comision = request.GET.get('comision')
    #respuesta = f'Estoy buscando la comision: {comision}'
    #return HttpResponse(respuesta)
    if request.GET['comision']:
        comision = request.GET['comision']
        cursos = Curso.objects.filter(comision__icontains = comision) # una lista con la busqueda correspondiente

        return render(request, 'AppCoder/resultadosBusqueda.html', {'cursos':cursos})
    else:
        return render(request, 'AppCoder/busquedaComision.html', {'errors':'No ingresaste ninguna comision'})
