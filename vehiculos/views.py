from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from vehiculos.forms import FormVehiculo
from vehiculos.models import Car, Category

# Create your views here.
def categoria_auto(request, category_id):
  autos = Car.objects.filter(categoria=category_id)
  try:
    categoria = Category.objects.get(pk=category_id)
  except:
    return redirect('home')
  context = {
    'autos': autos,
    'categoria':categoria
  }
  return render(request, 'auto_por_categoria.html', context)


def catalogo(request):
  autos = Car.objects.all()
  context = {
    'autos':autos
  }
  return render(request, 'catalogo.html', context)

def get_auto(request, pk):
  auto = get_object_or_404(Car, pk=pk)
  context = {
    'auto': auto
  }
  return render(request, 'auto_por_id.html', context)

def vehiculos(request):
  vehiculos = Car.objects.all()
  return render(request, 'panel/vehiculos.html', {'vehiculos': vehiculos})

def add_auto(request):
  if request.method == 'POST':
    form = FormVehiculo(request.POST, request.FILES)
    if form.is_valid():
      post = form.save(commit=False)
      post.autor = request.user
      post.save()
      return redirect('home')
  else:
    form = FormVehiculo()
  context = {
    'form':form
  }
  return render(request, 'agregar_auto.html', context)

def editar_vehiculo(request, pk):
  vehiculo = get_object_or_404(Car, pk=pk)
  if request.method == 'POST':
    form = FormVehiculo(request.POST, request.FILES, instance=vehiculo)
    if form.is_valid():
      form.save()
      return redirect('vehiculos')
  form = FormVehiculo(instance=vehiculo)
  return render(request, 'panel/editar_vehiculo.html', {'form': form, 'vehiculo': vehiculo})

def eliminar_vehiculo(request, pk):
  vehiculo = get_object_or_404(Car, pk=pk)
  vehiculo.delete()
  return redirect('vehiculos')
