from django import forms
from .models import Curso, Profesor, Estudiante

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'
