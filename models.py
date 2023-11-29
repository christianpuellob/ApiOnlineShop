from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

class Carrito(models.Model):
    productos = models.ManyToManyField(Producto, through='ItemCarrito')

class ItemCarrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

class Pedido(models.Model):
    carrito = models.OneToOneField(Carrito, on_delete=models.CASCADE)
    direccion_entrega = models.TextField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
