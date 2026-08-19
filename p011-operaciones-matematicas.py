# p011-operaciones-matematicas.py 
# Demostrar el uso de los diferentes operadores aritméticos con números 

print("\033[2J\033[H", end="") # Limpia pantalla
print("-"*65)
print("Calculadora de operaciones matemáticas")
print("-"*65)

x = 1000.54
y = 3.22

suma = x + y
resta = x - y
multiplicacion = x * y
modulo = x % y
division = x / y
exponenciacion = x ** y
division_entera = x // y

print(f'Los resultados de las operaciones son:')
print("-"*65)
print(f'Los números son: {x} y {y}\n')

# Encabezados de la tabla
print(f'{"Operación":<18} | {"Expresión":<18} | {"Resultado":<20}')
# Filas de la tabla con anchos fijos
print("-"*65)
print(f'{"Suma":<18} | {f"{x} + {y}":<18} | {suma:<20,.2f}')
print(f'{"Resta":<18} | {f"{x} - {y}":<18} | {resta:<20,.2f}')
print(f'{"Multiplicación":<18} | {f"{x} * {y}":<18} | {multiplicacion:<20,.2f}')
print(f'{"Módulo":<18} | {f"{x} % {y}":<18} | {modulo:<20,.2f}')
print(f'{"División":<18} | {f"{x} / {y}":<18} | {division:<20,.2f}')
print(f'{"Exponenciación":<18} | {f"{x} ** {y}":<18} | {exponenciacion:<20,.2f}')
print(f'{"División entera":<18} | {f"{x} // {y}":<18} | {division_entera:<20,.2f}')
print("-"*65)

