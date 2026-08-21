#p021-numero-suerte.py
#Calcular el número de la suerte a partir del año de nacimiento del usuario

print("\033[2J\033[H", end="") #Limpia pantalla
print('Calculando el número de la suerte a partir del año de nacimiento \n')
año_nacimiento = int(input('Ingrese su año de nacimiento (YYYY): ')) #Lee el año de nacimiento

#Calcula el número de la suerte sumando los dígitos del año de nacimiento
digito1 = año_nacimiento // 1000 #Obtiene el primer dígito
digito2 = (año_nacimiento // 100) % 10 #Obtiene el segundo dígito 
digito3 = (año_nacimiento // 10) % 10 #Obtiene el tercer dígito
digito4 = año_nacimiento % 10 #Obtiene el cuarto dígito

#Suma los dígitos del año de nacimiento
suma_digitos = digito1 + digito2 + digito3 + digito4 #Suma los dígitos del año de nacimiento

#Número de la suerte obtenido
numero_suerte = suma_digitos #Calcula el número de la suerte

#Muestra el resultado
print(f'Digito uno: {digito1}, Digito dos: {digito2}, Digito tres: {digito3}, Digito cuatro: {digito4}') #Muestra los dígitos del año de nacimiento
print(f'El número de la suerte para el año de nacimiento {año_nacimiento} es: {numero_suerte}') #Muestra el número de la suerte

 