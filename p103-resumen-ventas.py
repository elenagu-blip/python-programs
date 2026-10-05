#p103-resumen-ventas.py
#Transforma y filtra ventas con comprensiones

print("\033[2J\033[H", end="")

ventas = [250, 800, 1200, 450, 1800, 950]

finales = [round(v * 0.90, 2) if v > 1000 else v for v in ventas]
relevantes = [v for v in finales if v > 500]

print(f"Ventas originales: {ventas}")
print(f"Ventas finales: {finales}")
print(f"Ventas mayores de $500: {relevantes}")
print(f"Total relevante: ${sum(relevantes):.2f}")