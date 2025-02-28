from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Categoria, Producto

# Personalizar el panel de admin
admin.site.site_title = "ART AND FURNITURE MC"
admin.site.site_header = "ART AND FURNITURE MC  "
admin.site.index_title = "Administración del sitio web"

# Ocultar el modelo Group
admin.site.unregister(Group)

# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)
    verbose_name = "Categoría"
    verbose_name_plural = "Categorías"

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'en_stock')
    list_filter = ('categoria', 'en_stock')
    search_fields = ('nombre', 'material')
    verbose_name = "Producto"
    verbose_name_plural = "Productos"