# main.py - Proyecto base en Python para gestión de inventario

productos = []

def registrar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    productos.append(nombre)
    print("Producto registrado.")

def listar_productos():
    print("Lista de productos:")
    for p in productos:
        print("-", p)

def buscar_producto():
    nombre = input("Ingrese el nombre del producto a buscar: ")
    encontrados = [p for p in productos if nombre.lower() in p.lower()]
    if encontrados:
        print("Productos encontrados:")
        for p in encontrados:
            print("-", p)
    else:
        print("No se encontraron productos.")

def eliminar_producto():
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    if nombre in productos:
        productos.remove(nombre)
        print("Producto eliminado.")
    else:
        print("Producto no encontrado.")

def main():
    while True:
        print("\n1. Registrar producto")
        print("2. Listar productos")
        print("3. Buscar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_producto()
        elif opcion == '2':
            listar_productos()
        elif opcion == '3':
            buscar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
