from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('funcionarios/', include('funcionarios.urls')),
    path('clientes/', include('clientes.urls')),
    path('maquinas/', include('maquinas.urls')),
]
