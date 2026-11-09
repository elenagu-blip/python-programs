# p142-func-mas-param.py
# Número variable de argumentos con *args

print('\033[H\033[J')  # Limpia la pantalla


def saludatodos(*todos: str) -> None:
    # todos es ('Juan', 'Pedro', 'Luis')
    for nombre in todos:
        print(f"Saludos a {nombre}")


saludatodos("Juan", "Pedro", "Luis")