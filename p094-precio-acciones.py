#p094-precio-acciones.py
#Analisis basico de portafolio de acciones

print("\033[2J\033[H", end="")

#Precios de cierre de una accion (Lunes a Viernes)
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
precios = [150.25, 152.50, 149.75, 155.00, 153.20]

#Encontrar el precio maximo y minimo
precio_max = max(precios)
precio_min = min(precios)

#Encontrar la posicion (el dia) de esos precios
pos_max = precios.index(precio_max)
pos_min = precios.index(precio_min)

print(f"Precios de la semana: {precios}")
print(f"El precio más alto fue ${precio_max} el día {dias[pos_max]}.")
print(f"El precio más bajo fue ${precio_min} el día {dias[pos_min]}.")