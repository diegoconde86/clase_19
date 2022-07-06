from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=50) #txt
    comision = models.IntegerField() #int

    def __str__(self) -> str:
        return self.nombre +' '+ str(self.comision)


class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre + ' '+self.apellido+ ' '+self.email+ ' '+ self.profesion

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()   


    def __str__(self) -> str:
        return self.nombre + ' '+ self.apellido+ ' '+self.email

class Entregable(models.Model):
    nombre_entrega= models.CharField(max_length=50)
    tipo_entrega = models.CharField(max_length=50)
    fecha_entrega = models.DateField()

    def __str__(self) -> str:
        return self.nombre_entrega+' '+ self.tipo_entrega+' '+ str(self.fecha_entrega)