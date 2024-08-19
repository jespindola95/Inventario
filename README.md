Sistema de Gestión de Productos
Este proyecto en Python te permite manejar un inventario de productos de forma sencilla. Podés agregar, ver, actualizar y eliminar productos, y toda la información se guarda en un archivo para que no se pierda.

¿Qué hace este programa?
El sistema te permite gestionar dos tipos de productos:

Productos Electrónicos: Como celulares, computadoras, etc.
Productos Alimenticios: Como alimentos, bebidas, etc.
A través de un menú interactivo, podés:

Agregar nuevos productos al inventario.
Listar todos los productos que tenés guardados.
Actualizar la información de un producto existente.
Eliminar un producto que ya no necesitás.
Guardar todos los cambios en un archivo JSON.
Cargar los datos desde un archivo JSON para continuar donde dejaste.
Estructura del Proyecto
producto.py: Define la clase base Producto y las clases derivadas para los distintos tipos de productos.
inventario.py: Contiene la clase Inventario, que se encarga de manejar las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) y la persistencia en JSON.
main.py: Es el punto de entrada del programa, donde se maneja la interacción con el usuario a través del menú.
