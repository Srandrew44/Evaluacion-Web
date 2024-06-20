from django.shortcuts import render, redirect, get_object_or_404
from .forms import FormRegistro, FormCategory
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from vehiculos.models import Category, Car


def home(request):
  autos = Car.objects.filter(auto_destacado=True).order_by('marca')
  context = {
    'autos': autos
  }
  return render(request, 'home.html', context)

def registro(request):
  if request.method == 'POST':
    form = FormRegistro(request.POST)
    if form.is_valid():
      form.save()
      return redirect('registro')
  else:
    form = FormRegistro()
  context = {
    'form': form
  }
  return render(request, 'registro.html', context)

def inicio_sesion(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = auth.authenticate(username=username, password=password)
      if user is not None:
        auth.login(request, user)
        return redirect('home')
  form = AuthenticationForm()
  context = {
    'form': form
  }
  return render(request, 'inicio_sesion.html', context)

def cerrar_sesion(request):
  auth.logout(request)
  return redirect('home')


def categorias(request):
  return render(request, 'panel/categorias.html')

def agregar_categoria(request):
  if request.method == 'POST':
    form = FormCategory(request.POST)
    if form.is_valid():
      form.save()
      return redirect('categorias')
  form = FormCategory()
  return render(request, 'panel/agregar_categoria.html', {'form': form})


def editar_categoria(request, pk):
  category = get_object_or_404(Category, pk=pk)
  if request.method == 'POST':
    form = FormCategory(request.POST, instance=category)
    if form.is_valid():
      form.save()
      return redirect('categorias')
  form = FormCategory(instance=category)
  return render(request, 'panel/editar_categoria.html', {'form': form, 'category': category})

def eliminar_categoria(request, pk):
  category = get_object_or_404(Category, pk=pk)
  category.delete()
  return redirect('categorias')
