# p125-eliminar-diccionario.py
# Eliminar elementos de un diccionario

print('\033[H\033[J')

municipios = {
    'Apozol': 1863,
    'Calera': 1868,
    'Fresnillo': 1554,
    'Guadalupe': 1821,
    'Jalpa': 1824,
    'Jerez': 1824,
    'Loreto': 1931,
    'Mazapil': 1824,
    'Momax': 1857
}

print("Diccionario inicial:")
print(municipios)

del municipios['Apozol']
print("\nDespués de 'del Apozol':")
print(municipios)

municipios.pop('Fresnillo')
print("\nDespués de 'pop(\"Fresnillo\")':")
print(municipios)

municipios.popitem()  # elimina el último insertado (Momax)
print("\nDespués de 'popitem()' (eliminando Momax):")
print(municipios)

municipios.clear()
print("\nDespués de 'clear()':")
print(municipios)