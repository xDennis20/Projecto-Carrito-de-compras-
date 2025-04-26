from Catalogo import mostrar_catalogo
from Carrito import agregar_compras,eliminar_producto,vaciar_carrito,mostrar_carrito
from Checkout import finalizar_compra
import emoji

def menu():
    salir = False
    while not salir:
        print(emoji.emojize("""
        Bienvenido a la tienda virtual
        ¿Que deseas hacer?
        1. :open_book: Ver catálogo
        2. :package: Agregar producto al carrito
        3. :wastebasket: Eliminar producto del carrito
        4. ❗ Vaciar carrito
        5. :shopping_cart: Mostrar carrito
        6. :money_with_wings: Finalizar compra
        7. :door: Salir"""))
        try:
            opcion = int(input("Que opcion vas a elegir (1-7): "))
        except ValueError:
            print("Error: Coloque un valor entero por favor")
            continue

        if opcion == 1:
            mostrar_catalogo()
        elif opcion == 2:
            agregar_compras()
            pass
        elif opcion == 3:
            eliminar_producto()
        elif opcion == 4:
            vaciar_carrito()
        elif opcion == 5:
            mostrar_carrito()
        elif opcion == 6:
            finalizar_compra()
        elif opcion == 7:
            salir = True
        else:
            print("Opcion no valida elija de las opciones que existen por favor")
menu()