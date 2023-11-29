from rest_framework import serializers
from .models import Producto, Carrito, ItemCarrito, Pedido
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class ItemCarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCarrito
        fields = '__all__'

class CarritoSerializer(serializers.ModelSerializer):
    productos = ItemCarritoSerializer(many=True)

    class Meta:
        model = Carrito
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    carrito = CarritoSerializer()

    class Meta:
        model = Pedido
        fields = '__all__'
