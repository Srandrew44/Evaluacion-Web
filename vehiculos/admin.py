from django.contrib import admin
from .models import Category, Car

class VehiculoAdmin(admin.ModelAdmin):
  list_display = ('marca', 'modelo', 'categoria', 'auto_destacado')

# Register your models here.
admin.site.register(Category)
admin.site.register(Car, VehiculoAdmin)

