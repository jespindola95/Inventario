from inventario import Inventario
from producto import ProductoElectronico, ProductoAlimenticio

def main():
    inventario = Inventario()

    while True:
        print("\n1. Agregar producto")
        print("2. Listar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Guardar datos")
        print("6. Cargar datos")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == '1':
                tipo = input("Tipo de producto (electronico/alimenticio): ")
                nombre = input("Nombre: ")
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))

                if tipo == 'electronico':
                    garantia = int(input("Garantía (meses): "))
                    producto = ProductoElectronico(nombre, precio, cantidad, garantia)
                elif tipo == 'alimenticio':
                    fecha_vencimiento = input("Fecha de vencimiento (YYYY-MM-DD): ")
                    producto = ProductoAlimenticio(nombre, precio, cantidad, fecha_vencimiento)
                else:
                    print("Tipo de producto no válido.")
                    continue

                inventario.agregar_producto(producto)

            elif opcion == '2':
                inventario.listar_productos()

            elif opcion == '3':
                nombre = input("Nombre del producto a actualizar: ")
                precio = input("Nuevo precio (presione enter para dejar igual): ")
                cantidad = input("Nueva cantidad (presione enter para dejar igual): ")

                inventario.actualizar_producto(
                    nombre,
                    precio=float(precio) if precio else None,
                    cantidad=int(cantidad) if cantidad else None
                )

            elif opcion == '4':
                nombre = input("Nombre del producto a eliminar: ")
                inventario.eliminar_producto(nombre)

            elif opcion == '5':
                filename = input("Nombre del archivo para guardar: ")
                inventario.guardar_datos(filename)

            elif opcion == '6':
                filename = input("Nombre del archivo para cargar: ")
                inventario.cargar_datos(filename)

            elif opcion == '7':
                break

            else:
                print("Opción no válida. Por favor, intente de nuevo.")
        
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
    
    