"""
URL configuration for CharlieCars project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from vehiculos import views as VehiculoViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.inicio_sesion, name="inicio_sesion"),
    path('logout/', views.cerrar_sesion, name="cerrar_sesion"),
    path('categoria/', include('vehiculos.urls')),
    path('catalogo/', VehiculoViews.catalogo, name="catalogo"),
    path('vehiculo/<int:pk>/', VehiculoViews.get_auto, name="get_auto"),
    path('categorias/', views.categorias, name="categorias"),
    path('categorias/agregar', views.agregar_categoria, name="agregar_categoria"),
    path('categorias/editar/<int:pk>/', views.editar_categoria, name="editar_categoria"),
    path('categorias/eliminar/<int:pk>', views.eliminar_categoria, name="eliminar_categoria"),
    path('vehiculos/', VehiculoViews.vehiculos, name="vehiculos"),
    path('vehiculo/agregar/', VehiculoViews.add_auto, name="add_auto"),
    path('vehiculo/editar/<int:pk>', VehiculoViews.editar_vehiculo, name="editar_vehiculo"),
    path('vehiculo/eliminar/<int:pk>', VehiculoViews.eliminar_vehiculo, name="eliminar_vehiculo"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
