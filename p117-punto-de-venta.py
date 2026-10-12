# p117-punto-de-venta.py
# Simulación de un punto de venta usando diccionarios

print('\033[H\033[J')
print('Simulación de un punto de venta usando diccionarios\n')

# Base de conocimiento: menú con productos y precios
menu = {
    'taco': 18.50,
    'burrito': 45.00,
    'quesadilla': 35.00,
    'refresco': 20.00,
    'agua': 15.00
}

# Mostrar menú
print("--- Bienvenido a 'El Taco Feroz' ---")
print("Este es nuestro menú:")
for item, precio in menu.items():
    print(f" - {item:<12} : ${precio:,.2f}")
print("-" * 35)

orden = {}          # el "carrito"
total_general = 0

# Tomar orden
while True:
    producto = input("\n¿Qué desea ordenar? (escriba 'fin' para terminar): ").strip().lower()
    if producto == 'fin':
        break
    if producto not in menu:
        print("Error: Ese producto no está en el menú. Intente de nuevo.")
        continue
    try:
        cantidad = int(input(f"¿Cuántos '{producto}' desea?: "))
        if cantidad <= 0:
            print("Error: La cantidad debe ser un número positivo.")
            continue
    except ValueError:
        print("Error: Debe ingresar un número entero (ej. 2).")
        continue

    # Si el producto ya estaba en la orden, se suma la cantidad
    orden[producto] = orden.get(producto, 0) + cantidad
    print(f"Agregados {cantidad} {producto}(s) a su orden.")

# Reporte final: recibo
print("\n--- SU RECIBO ---")
if not orden:
    print("No se ordenó ningún producto.")
else:
    for producto, cantidad in orden.items():
        precio_unitario = menu[producto]
        subtotal = precio_unitario * cantidad
        print(f" {cantidad} x {producto:<12} : ${subtotal:,.2f}")
        total_general += subtotal

    print("-" * 35)
    print(f"TOTAL A PAGAR: ${total_general:,.2f}")
    print("¡Gracias por su compra!")