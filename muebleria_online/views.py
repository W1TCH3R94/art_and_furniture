from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Producto, Categoria
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')


def registro_usuario(request):
    if request.method == 'GET':
        return render(request, 'registro_usuario.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'registro_usuario.html', {
                    'form': UserCreationForm,
                    "error": 'El usuario ya se encuentra registrado'
                })
        return render(request, 'registro_usuario.html', {
            'form': UserCreationForm,
            "error": 'Las contraseñas no coinciden'
        })


def inicio_sesion(request):
    if request.method == 'GET':
        return render(request, 'iniciar_sesion.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'iniciar_sesion.html', {
                'form': AuthenticationForm,
                'error': 'El nombre de usuario o la contraseña son incorrectos'
            })
        else:
            login(request, user)
            return redirect('catalogo_muebles')
        

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('home')


@login_required
def catalogo_muebles(request):

    categorias = Categoria.objects.all()

    id_categoria = request.GET.get('categoria')
    if id_categoria:
        productos = Producto.objects.filter(categoria_id=id_categoria)
    else:
        productos = Producto.objects.all()

    return render(request, 'catalogo_muebles.html', {
        'productos' : productos,
        'categorias' : categorias,
    })


