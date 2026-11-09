# p139-funcion-parametros.py
# Función con múltiples parámetros (el orden importa)

print('\033[H\033[J')  # Limpia la pantalla


def saluda(apaterno: str, nombre: str) -> None:
    print(f'Hola {nombre} {apaterno}')


saluda('Perez', 'Juan')
# saluda('Juan')  # Genera error (pocos argumentos)
# saluda('Pérez', 'Juan', 'Extra')  # Error: demasiados argumentos