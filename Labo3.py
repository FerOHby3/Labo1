print("Inventario de Tienda\n ")
print("1. Agregar un Nuevo Producto ")
print("2. Elimine un Producto ")
print("3. Actualizar la cantidad de un producto ")
print("4. Consultar el inventario Completo ")
print("5. Cerrar el Programa \n")

opcion=""
productos=[]
cantidades=[]

while opcion !="5":
    opcion=input("Ingrese la opcion deseada ")

    if opcion=="1":
        producto=input("Ingrese el producto a Añadir ")
        cantidad=input("Ingrese la cantidad del producto a Añadir ")
        productos.append(producto)
        cantidades.append(cantidad)
    if opcion=="2":
        producto=input("Ingrese el producto a Eliminar ")
        productos.remove(producto)
        cantidades.remove
    if opcion=="3":
        print("Coming Soon")
    if opcion=="4":
        print("Coming Soon")
    if opcion=="5":
        print("Gracias por Usar el programa")

print(productos)
print(cantidades)
