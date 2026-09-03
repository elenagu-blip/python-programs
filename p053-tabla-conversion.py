#p053-tabla-conversion.py3
# p052-tabla-conversion.py
# Muestra una tabla de conversión de Peso a Dólar

tc = 20.71

while True:
    print('\033[H\033[J')
    print("Tabla de Conversión Peso a Dólar")
    print(f'Tipo de Cambio: {tc} Pesos por Dólar')
    print("-" * 15)
    
    while True:
        pi = float(input("Valor inicial: "))
        pf = float(input("Valor final: "))
        if (pi > 0 and pf > 0) and pi < pf:
            break
        print("Error en los valores, intente de nuevo")
    
    c = pi
    print("\nPesos\tDólar")
    print("-" * 15)
    while c <= pf:
        print(f'{c}\t{c/tc:.2f}')
        c += 1
    print("-" * 15)
    
    res = input('¿Deseas continuar (S/N)? ').upper()
    if res != 'S':
        break

print("\n¡Gracias por usar el conversor!")