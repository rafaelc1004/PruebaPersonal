from django.db import models

# Create your models here.

class Departamento(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    

class Trabajador(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fechaIngreso = models.DateField()
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)


    def __str__(self):
        return 'f{self.nombre} {self.apellido}'