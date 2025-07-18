from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Ruta para el panel de administración de Django
    path('admin/', admin.site.urls),

    # Incluye todas las URLs definidas en la aplicación "mi_primer_app"
    path('', include('mi_primer_app.urls')),
]
