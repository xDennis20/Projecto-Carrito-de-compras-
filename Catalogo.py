Lista_Productos = {
    "P001": {"Nombre": "Auriculares Bluetooth", "Precio": 25.99},
    "P002": {"Nombre": "Mouse Gamer RGB", "Precio": 18.50},
    "P003": {"Nombre": "Teclado Mecánico", "Precio": 45.75},
    "P004": {"Nombre": "Webcam HD", "Precio": 30.00},
    "P005": {"Nombre": "Power Bank 10000mAh", "Precio": 22.90}
}

def mostrar_catalogo():
    print("CATALOGO DE PRODUCTOS")
    print("-" * 30)
    for key,valor in Lista_Productos.items():
        nombre = valor.get("Nombre")
        precio = valor.get("Precio")
        print(f"{key} | Productos: {nombre} | Precio: ${precio}")