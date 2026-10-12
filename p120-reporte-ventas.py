# p120-reporte-ventas.py
# Crear una lista de diccionarios para representar un reporte de ventas

print('\033[H\033[J')
print('Reporte de Ventas\n')
print('-' * 60)

print("\n--- Registro de Transacciones ---")
while True:
    try:
        n = int(input("Número de compras a registrar: "))
        if n > 0:
            break
        print("Debe ser un número mayor que 0.")
    except ValueError:
        print("Debe ingresar un número entero.")

# Lista de compras: cada compra es un diccionario
compras = []
for i in range(1, n + 1):
    print(f'\n------ Compra {i} ------')
    cliente = input("Nombre Cliente : ").strip()
    producto = input("Nombre Producto : ").strip()
    while True:
        try:
            cantidad = int(input("Cantidad : "))
            break
        except ValueError:
            print("Cantidad no válida. Debe ser un número entero.")
    while True:
        try:
            precio = float(input("Precio : "))
            break
        except ValueError:
            print("Precio no válido. Debe ser un número.")

    compra = {
        "cliente": cliente,
        "producto": producto,
        "cantidad": cantidad,
        "precio": precio
    }
    compras.append(compra)

print('\n--- Lista de Compras Registradas ---\n', compras)

# Diccionario de diccionarios: totales por cliente
clientes = {}
for compra in compras:
    cliente = compra["cliente"]
    if cliente not in clientes:
        clientes[cliente] = {"cantidad": 0, "subtotal": 0}
    clientes[cliente]["cantidad"] += compra["cantidad"]
    clientes[cliente]["subtotal"] += compra["cantidad"] * compra["precio"]

print('\n--- Reporte de Totales por Cliente ---\n')
for cliente, datos in clientes.items():
    print("Cliente :", cliente)
    print("Cantidad Total de Productos :", datos["cantidad"])
    print("Subtotal a Pagar : $", datos["subtotal"])
    print()

print('\n--- Diccionario de Clientes (Estructura Interna) ---\n', clientes)