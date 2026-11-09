# p140-func-param-nombre.py
# Parámetros por nombre: se puede cambiar el orden si se especifica el nombre

print('\033[H\033[J')  # Limpia la pantalla


def saluda(apaterno: str, amaterno: str, nombre: str) -> None:
    print(f'Hola {nombre} {apaterno} {amaterno}')


saluda('Lopez', 'Martinez', 'Ana')
saluda(nombre='Ana', amaterno='Martinez', apaterno='Lopez')