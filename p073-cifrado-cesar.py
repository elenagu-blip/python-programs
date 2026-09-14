#p073-cifrado-cesar.py
#Cifra un mensaje usando el Cifrado Cesar

while True:
    print("\033[2J\033[H", end="")
    print("Encriptador con Cifrado César")
    
    mensaje_original = input("Ingresa el mensaje a encriptar: ")
    desplazamiento = int(input("Ingresa la clave de desplazamiento (un número): "))
    
    #Variable de texto donde se va armando el mensaje cifrado, letra por letra
    mensaje_cifrado = ""
    
    #Ciclo for que recorre cada caracter del mensaje original
    for caracter in mensaje_original:
        if caracter.isalpha():  #Solo ciframos las letras
            codigo_ascii = ord(caracter)
            
            #Verificamos si es mayuscula o minuscula, para mantener el mismo caso
            if caracter.islower():
                base = ord('a')
            else:
                base = ord('A')
            
            #Aplicamos la formula del cifrado por desplazamiento
            codigo_nuevo = base + (codigo_ascii - base + desplazamiento) % 26
            mensaje_cifrado = mensaje_cifrado + chr(codigo_nuevo)
        else:
            #Los caracteres que no son letras (espacios, numeros, signos) pasan igual
            mensaje_cifrado = mensaje_cifrado + caracter
    
    print(f"\nMensaje Original: {mensaje_original}")
    print(f"Mensaje Cifrado: {mensaje_cifrado}")
    
    if input("\n\n¿Deseas encriptar otro mensaje (S/N)? ").upper() == "N":
        break

print("\n¡Encriptación finalizada!")