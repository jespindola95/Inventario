import json
from producto import Producto, ProductoElectronico, ProductoAlimenticio

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def obtener_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        return None

    def actualizar_producto(self, nombre, precio=None, cantidad=None):
        producto = self.obtener_producto(nombre)
        if producto:
            if precio is not None:
                producto.precio = precio
            if cantidad is not None:
                producto.cantidad = cantidad

    def eliminar_producto(self, nombre):
        producto = self.obtener_producto(nombre)
        if producto:
            self.productos.remove(producto)

    def listar_productos(self):
        for producto in self.productos:
            print(producto)

    def guardar_datos(self, filename):
        with open(filename, 'w') as file:
            json.dump([producto.__dict__ for producto in self.productos], file)

    def cargar_datos(self, filename):
        try:
            with open(filename, 'r') as file:
                productos_data = json.load(file)
                for producto_data in productos_data:
                    if 'garantia' in producto_data:
                        producto = ProductoElectronico(**producto_data)
                    elif 'fecha_vencimiento' in producto_data:
                        producto = ProductoAlimenticio(**producto_data)
                    else:
                        producto = Producto(**producto_data)
                    self.productos.append(producto)
        except FileNotFoundError:
            print("Archivo no encontrado.")