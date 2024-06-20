from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from vehiculos.models import Category

class FormRegistro(UserCreationForm):
  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')
    
    
class FormCategory(forms.ModelForm):
  class Meta:
    model = Category
    fields = '__all__'
    
  


