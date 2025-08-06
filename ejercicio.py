class tienda:
    def __init__(self, nombre, precio,cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def producto(self):
        print("Nombre del producto:", self.nombre)
        print("Precio del producto:", self.precio)
        print("Cantidad disponible:", self.cantidad) 

print("control de productos")
lista_productos = []
while True:
    print("Seleccione la opcion deseada:")
    print("1. Agregar producto")
    print("2. Mostrar informacion del producto")
    print("3. realizar pedido")
    print("0. Salir")
    opcion = int(input())
    
    if opcion == 1:
        print("Ingrese el nombre del producto")
        nombre = input()
        print("Ingrese el precio del producto")
        precio = float(input())
        print("Ingrese la cantidad disponible")
        cantidad = int(input())
        producto = tienda(nombre, precio, cantidad)
        lista_productos.append(producto)
        print("Producto registrado correctamente")
    
    elif opcion == 2:
        numero_productos = len(lista_productos)
        print("El numero de productos es:", numero_productos)
        for producto in lista_productos:
            producto.producto()
            print("-" * 20)
    
    elif opcion == 3:
        print("ingrese el nombre del producto a pedir")
        nombre_pedido = input()
        for producto in lista_productos:
            if producto.nombre == nombre_pedido:
                print("Ingrese la cantidad a pedir")
                cantidad_pedir = int(input())
                if cantidad_pedir <= producto.cantidad:
                    producto.cantidad -= cantidad_pedir
                    print("Pedido realizado correctamente")
                    print("Precio total:", producto.precio * cantidad_pedir)
                    print("Cantidad disponible:", producto.cantidad)
                else:
                    print("No hay suficiente cantidad disponible")
                break
        else:
            print("Producto no encontrado")

   
    elif opcion == 0:
    
        print("Hasta luego")
        break
    
    else:
        print("Opcion no valida")
