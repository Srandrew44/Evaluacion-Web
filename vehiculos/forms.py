from django import forms
from vehiculos.models import Car

class FormVehiculo(forms.ModelForm):
  class Meta:
    model = Car
    fields = ('marca', 'modelo', 'categoria', 'imagen', 'descripcion_corta', 'descripcion', 'precio', 'auto_destacado')

