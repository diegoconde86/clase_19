from django.shortcuts import render
from django.http import HttpResponse
from AppFamilia.models import Familiar
from django.template import loader
# Create your views here.


def familiar(self):

    # Creo los familiares
    familiar1 = Familiar(
        id = 1,
        nombre ='Eduardo',
        apellido ='Montero',
        edad = 34,
        fecha_nacimiento = '1988-06-05',
        parentesco = 'hijo'
    )
    familiar1.save()

    familiar2 = Familiar(
        id = 2,
        nombre ='Lucrecia',
        apellido ='Constante',
        edad = 38,
        fecha_nacimiento = '1984-06-05',
        parentesco = 'hija'
    )
    familiar2.save()

    familiar3 = Familiar(
        id = 3,
        nombre ='Patricia',
        apellido ='Romero',
        edad = 34,
        fecha_nacimiento = '1988-07-05',
        parentesco = 'madre'
    )
    familiar3.save()

    # Guardo en un diccionario los atributos de los familiares con su respectiva etiqueta
    dic ={}
    dic['familiar1'] = ['Nombre: '+familiar1.nombre,'Apellido: '+familiar1.apellido, 'Edad: '+str(familiar1.edad), 'Fecha Nacimiento: '+ familiar1.fecha_nacimiento, 'Tipo parentesco: '+familiar1.parentesco ]
    dic['familiar2'] = ['Nombre: '+familiar2.nombre,'Apellido: '+familiar2.apellido, 'Edad: '+str(familiar2.edad), 'Fecha Nacimiento: '+ familiar2.fecha_nacimiento, 'Tipo parentesco: '+familiar2.parentesco ]
    dic['familiar3'] = ['Nombre: '+familiar3.nombre,'Apellido: '+familiar3.apellido, 'Edad: '+str(familiar3.edad), 'Fecha Nacimiento: '+ familiar3.fecha_nacimiento, 'Tipo parentesco: '+familiar3.parentesco ]
    

    template = loader.get_template('template1.html')
    documento = template.render(dic)

    return HttpResponse(documento)

    #pushear y subir
    
