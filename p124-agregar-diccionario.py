# p124-agregar-diccionario.py
# Agregar elementos a un diccionario

print('\033[H\033[J')

ventas = {
    'Juan': 1550,
    'Jose': 2600,
    'Maria': 2220
}

print("Ventas iniciales:")
print(ventas)

# Agregar usando []
ventas['Rocio'] = 2500
ventas['Mateo'] = 1567

# Agregar usando update()
ventas.update({'Andrea': 9567})
ventas.update({'Miguel': 1234})

print("\nVentas actualizadas:")
print(ventas)