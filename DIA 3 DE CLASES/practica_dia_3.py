
def validar_precio(precio):
    if not isinstance(precio, (int, float)):
        raise ValueError("el precio debe ser un numero")
    if precio <= 0:
        raise ValueError("el precio debe ser un numero positivo.")

def validar_stock(stock):
    if not isinstance(stock, int):
        raise ValueError("el stock debe ser un numero entero")
    if stock <= 0:
        raise ValueError("el stock debe ser un numero entero positivo")

def registrar_producto(nombre, precio, stock, lista_inventario):
    try:
        validar_precio(precio)
        validar_stock(stock)
        
        # Creamos el diccionario y lo guardamos en la lista
        nuevo_producto = {"nombre": nombre, "precio": precio, "stock": stock}
        lista_inventario.append(nuevo_producto)
        
        print(f"Éxito: Producto {nombre} registrado correctamente.")
    except ValueError as e:
        print(f"Error al registrar el producto: {e}")
    except TypeError as e:
        print(f"Error de tipo: {e}")

def mostar_inventario(productos):
    print("\n--- Inventario de productos ---")
    if not productos:
        print("El inventario está vacío.")
    for producto in productos:
        print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Stock: {producto['stock']}")

inventario = []

nombre = input("Ingrese el nombre del producto: ")

try:
    # Convertimos los inputs a números para que las validaciones funcionen
    precio_ingresado = float(input("Ingrese el precio del producto: "))
    stock_ingresado = int(input("Ingrese el stock del producto: ")) # Aquí agregamos el int()
    
    # Llamamos a la función pasando también la lista de inventario
    registrar_producto(nombre, precio_ingresado, stock_ingresado, inventario)

except ValueError:
    print("Error: El precio debe ser decimal y el stock un número entero.")

# Mostramos el resultado final
mostar_inventario(inventario)