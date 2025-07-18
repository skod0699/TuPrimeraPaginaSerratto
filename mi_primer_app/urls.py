from django.urls import path
from .views import (
    saludo, saludo_con_template, inicio, crear_familiar,
    crear_curso, crear_profesor, crear_estudiante,
    lista_cursos, lista_profesores, lista_estudiantes,buscar_estudiantes
)

urlpatterns = [
    path('hola-mundo/', saludo, name='saludo'),
    path('hola-mundo-template/', saludo_con_template, name='saludo_template'),
    path('crear-familiar/<str:nombre>/', crear_familiar, name='crear_familiar'),
    path('crear-curso/', crear_curso, name='crear_curso'),
    path('crear-profesor/', crear_profesor, name='crear_profesor'),
    path('crear-estudiante/', crear_estudiante, name='crear_estudiante'),

    # Nuevas rutas para ver las listas
    path('cursos/', lista_cursos, name='lista_cursos'),
    path('profesores/', lista_profesores, name='lista_profesores'),
    path('estudiantes/', lista_estudiantes, name='lista_estudiantes'),

    path('', inicio, name='inicio'),

  path('buscar-estudiantes/', buscar_estudiantes, name='buscar_estudiantes'),


]
