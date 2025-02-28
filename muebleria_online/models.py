from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ['nombre'] #Ordenamiento predeterminado

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos') #Related name permite consultas inversas como categoria.productos.all() para obtener todos los productos de una categoria
    material = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    precio =models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True) #De momento acepta como vacio este campo
    en_stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        #Mejor concatenado y manejo del error de producto con categoria NONE
        return f"{self.nombre} - {self.categoria.nombre if self.categoria else 'Sin categoría'}"
    
    class Meta:
        ordering = ['nombre']