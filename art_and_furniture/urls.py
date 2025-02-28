"""
URL configuration for art_and_furniture project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from muebleria_online import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #  Vistas de Art and Furniture
    path('', views.home, name='home'),
    path('registro/', views.registro_usuario, name='registro_usuario'),
    path('catalogo/', views.catalogo_muebles, name='catalogo_muebles'),
    path('inicio_sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)