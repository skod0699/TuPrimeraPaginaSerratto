from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CursoForm, ProfesorForm, EstudianteForm
from .models import Curso, Profesor, Estudiante
from django.db import models


# --- Vistas básicas ---

def saludo(request):
    return HttpResponse("¡Hola, mundo!")

def saludo_con_template(request):
    return render(request, 'mi_primer_app/saludo.html')

def inicio(request):
    estudiantes = Estudiante.objects.prefetch_related('cursos').all()

    # --- Buscador complejo ---
    nombre = request.GET.get('nombre', '').strip()
    apellido = request.GET.get('apellido', '').strip()
    email = request.GET.get('email', '').strip()
    curso_nombre = request.GET.get('curso', '').strip()
    comision = request.GET.get('comision', '').strip()

    if nombre or apellido or email or curso_nombre or comision:
        filtros = models.Q()
        if nombre:
            filtros &= models.Q(nombre__icontains=nombre)
        if apellido:
            filtros &= models.Q(apellido__icontains=apellido)
        if email:
            filtros &= models.Q(email__icontains=email)
        if curso_nombre:
            filtros &= models.Q(cursos__nombre__icontains=curso_nombre)
        if comision:
            filtros &= models.Q(cursos__comision__icontains=comision)

        estudiantes = Estudiante.objects.filter(filtros).distinct().prefetch_related('cursos')

    return render(request, 'mi_primer_app/inicio.html', {
        'estudiantes': estudiantes
    })

def crear_familiar(request, nombre):
    return HttpResponse(f"Familiar creado: {nombre}")

# --- Crear Curso / Profesor / Estudiante ---

def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Curso creado exitosamente.")
    else:
        form = CursoForm()
    return render(request, 'mi_primer_app/crear_curso.html', {'form': form})

def crear_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Profesor creado exitosamente.")
    else:
        form = ProfesorForm()
    return render(request, 'mi_primer_app/crear_profesor.html', {'form': form})

def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Estudiante creado exitosamente.")
    else:
        form = EstudianteForm()
    return render(request, 'mi_primer_app/crear_estudiante.html', {'form': form})

# --- Ver listas de registros ---

def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'mi_primer_app/lista_cursos.html', {'cursos': cursos})

def lista_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'mi_primer_app/lista_profesores.html', {'profesores': profesores})

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.prefetch_related('cursos').all()
    return render(request, 'mi_primer_app/lista_estudiantes.html', {'estudiantes': estudiantes})

def buscar_estudiantes(request):
    query = request.GET.get('q', '')
    estudiantes = []
    if query:
        estudiantes = Estudiante.objects.filter(
            models.Q(nombre__icontains=query) | models.Q(apellido__icontains=query)
        )
    return render(request, 'mi_primer_app/buscar_estudiantes.html', {
        'estudiantes': estudiantes,
        'query': query
    })
