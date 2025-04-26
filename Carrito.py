import Catalogo
productos_comprados = dict()
productos = Catalogo.Lista_Productos

def agregar_compras():
    codigo_producto = input("Ingrese el codigo del producto que desea: ").upper().strip()
    cantidad = 0

    try:
        cantidad = int(input("Cantidad de producto que desea: ").strip())
    except ValueError :
        print("Por favor coloque un valor entero")
    while not cantidad > 0:
        print("Coloque una cantidad valida mayor de 0 porfavor")
        cantidad = int(input("Cantidad de producto que desea: ").strip())

    if codigo_producto in productos:
        if codigo_producto in productos_comprados:
            cantidad_existente = productos_comprados.get(codigo_producto)
            productos_comprados[codigo_producto] = cantidad_existente + cantidad
        else:
            productos_comprados[codigo_producto] = cantidad
    else:
        print("El codigo no existe")
    print("¡Producto agregado con exito!")

def eliminar_producto():
    codigo_eliminar = input("Coloque el codigo del producto que desee eliminar del carrito: ").strip()
    if codigo_eliminar in productos_comprados:
        del productos_comprados[codigo_eliminar]
        print("Producto eliminado con exito")
    else:
        print("El codigo que desea eliminar no esta en el carrito")

def mostrar_carrito():
    total_general = 0
    if productos_comprados:
        for codigo,cantidad in productos_comprados.items():
            producto = productos.get(codigo)
            nombre = producto.get("Nombre")
            precio = producto.get("Precio")
            total = cantidad * precio
            total_general += cantidad * precio
            print(f"""Tu carrito:
            - {nombre} (x{cantidad}) -> ${precio} -> Total: ${total:.2f}""")
    else:
        print("No hay nada que mostrar el carrito esta vacio, Por favor haga compras")
    print(f"Total compras: ${total_general:.2f}")

def vaciar_carrito():
    productos_comprados.clear()
    print("Carrito vaciado con exito!")