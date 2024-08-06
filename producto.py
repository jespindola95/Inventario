class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"Producto(nombre={self.nombre}, precio={self.precio}, cantidad={self.cantidad})"

class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, cantidad, garantia):
        super().__init__(nombre, precio, cantidad)
        self.garantia = garantia

    def __str__(self):
        return f"ProductoElectronico(nombre={self.nombre}, precio={self.precio}, cantidad={self.cantidad}, garantia={self.garantia})"

class ProductoAlimenticio(Producto):
    def __init__(self, nombre, precio, cantidad, fecha_vencimiento):
        super().__init__(nombre, precio, cantidad)
        self.fecha_vencimiento = fecha_vencimiento

    def __str__(self):
        return f"ProductoAlimenticio(nombre={self.nombre}, precio={self.precio}, cantidad={self.cantidad}, fecha_vencimiento={self.fecha_vencimiento})"