# p138-funcion-parametro.py
# Función con un parámetro posicional

print('\033[H\033[J')  # Limpia la pantalla


def saluda(nombre: str) -> None:
    print(f'Hola {nombre} bienvenido a Python, tu nombre tiene {len(nombre)} caracteres')


saluda('Carlos Castaneda')
saluda('Juan Perez Diaz')
saluda('María Soto García')