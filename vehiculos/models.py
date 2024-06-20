from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
  category_name = models.CharField(max_length=50)
  
  class Meta:
    verbose_name_plural = 'categories'
  
  def __str__(self) -> str:
    return self.category_name


class Car(models.Model):
  marca = models.CharField(max_length=50)
  modelo = models.CharField(max_length=50)
  categoria = models.ForeignKey(Category, on_delete=models.CASCADE)
  imagen = models.ImageField(upload_to='uploads')  
  descripcion_corta = models.TextField(max_length=500)
  descripcion = models.TextField(max_length=2000)
  precio = models.IntegerField(default=0)
  autor = models.ForeignKey(User, on_delete=models.CASCADE)
  auto_destacado = models.BooleanField(default=False)
  
  def __str__(self) -> str:
    return self.marca
  
  