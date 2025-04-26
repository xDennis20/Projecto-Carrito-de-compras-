from datetime import datetime
from Carrito import productos_comprados,mostrar_carrito,productos
def finalizar_compra():
    if productos_comprados:
        mostrar_carrito()
        finalizar = input("¿Deseas confirmar la compra (S/N)? ").lower()
        if finalizar.isalpha():
            while not finalizar == "s" or finalizar == "n":
                print("Por favor coloque solo (S/N)")
                finalizar = input("¿Deseas confirmar la compra (S/N)? ").lower()
            if finalizar == "s":
                print("Muchas gracias por su compra espero regrese pronto")
                guardar_historial()
                productos_comprados.clear()
            elif finalizar == "n":
                return
        else:
            print("Opcion no valida")
    else:
        print("Tu carrito esta vacia, no hay nada que finalizar")

def guardar_historial():
    fecha = datetime.now()
    formato_fecha = fecha.strftime("%Y-%m-%d %H:%M")
    total_todo = 0
    contenido = f"Fecha: {formato_fecha}\n"
    for key,valor in productos_comprados.items():
        cosas = productos[key]
        name = cosas.get("Nombre")
        price = cosas.get("Precio")
        total_producto = price * valor
        total_todo += valor * price
        contenido += f"- Producto: {name} (x{valor}) -> Precio: ${total_producto:.2f}\n"
    contenido += f"Total Compra: ${total_todo:.2f}\n ----------------- \n"
    try:
        with open("Historial.txt","a") as archivo:
            archivo.write(f"{contenido}")
    except FileNotFoundError:
        print("¡El archivo no se encontro!")