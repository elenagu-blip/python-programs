print("\033[2J\033[H", end="")

print("OPERADORES DE ASIGNACIÓN EN PYTHON\n")

x = 100

print(f"{'Operación':<30} {'Antes':>8} {'Operador':>10} {'Después':>10}")
print("-" * 62)

antes = x
x += 5
print(f"{'Sumar 5 a x':<30} {antes:>8} {'+= 5':>10} {x:>10}")

antes = x
x -= 3
print(f"{'Restar 3 a x':<30} {antes:>8} {'-= 3':>10} {x:>10}")

antes = x
x *= 2
print(f"{'Multiplicar x por 2':<30} {antes:>8} {'*= 2':>10} {x:>10}")

antes = x
x /= 4
print(f"{'Dividir x entre 4':<30} {antes:>8} {'/= 4':>10} {x:>10}")

antes = x
x %= 3
print(f"{'Módulo de x entre 3':<30} {antes:>8} {'%= 3':>10} {x:>10}")

antes = x
x **= 2
print(f"{'x elevado al cuadrado':<30} {antes:>8} {'**= 2':>10} {x:>10}")