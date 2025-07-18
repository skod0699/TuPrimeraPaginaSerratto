from django.db import models
from django.utils import timezone

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion_en_semanas = models.PositiveIntegerField()
    fecha_inicio = models.DateField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} ({self.duracion_en_semanas} semanas)"

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    especialidad = models.CharField(max_length=100, default='General')
    fecha_contratacion = models.DateField(default=timezone.now)
    cursos = models.ManyToManyField(Curso, blank=True, related_name='profesores')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField(default='2000-01-01')
    cursos = models.ManyToManyField(Curso, blank=True, related_name='estudiantes')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
