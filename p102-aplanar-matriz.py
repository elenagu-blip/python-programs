#p102-aplanar-matriz.py
#Recorre una matriz con ciclos anidados

print("\033[2J\033[H", end="")

matriz = [[4, -2, 8], [0, 5, -1], [7, 3, -6]]

valores = [numero for fila in matriz for numero in fila]
positivos = [numero for fila in matriz for numero in fila if numero > 0]

print(f"Matriz: {matriz}")
print(f"Lista plana: {valores}")
print(f"Valores positivos: {positivos}")