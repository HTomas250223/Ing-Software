from django.db import models

class Aula(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()

    def __str__(self):
        return self.nombre

class Docente(models.Model):
    nombre = models.CharField(max_length=100)
    disponibilidad = models.JSONField()  # Almacena la disponibilidad en formato JSON

    def __str__(self):
        return self.nombre

class Horario(models.Model):
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    fecha_hora_inicio = models.DateTimeField()
    fecha_hora_fin = models.DateTimeField()

    def __str__(self):
        return f"{self.docente} - {self.aula} ({self.fecha_hora_inicio} - {self.fecha_hora_fin})"



# Create your models here.
