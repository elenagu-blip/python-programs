#p086-control-gastos.py
#Gestiona una lista de gastos mensuales: ver, agregar, modificar, eliminar y sumar

gastos = []  #Lista donde se van guardando los montos de los gastos

while True:
    print("\033[2J\033[H", end="")
    #Mostrar menu
    print("--- Control de Gastos ---")
    print("1.- Ver Gastos")
    print("2.- Agregar Gasto")
    print("3.- Modificar Gasto")
    print("4.- Eliminar Gasto")
    print("5.- Ver Total")
    print("6.- Salir")
    
    try:
        opcion = int(input("\nElige una opción: "))
    except ValueError:
        print("\nError: debes ingresar un número.")
        input("\nPresiona Enter para continuar...")
        continue
    
    if opcion == 1:
        #Ver Gastos, usando enumerate para mostrar indice y valor
        print("\n--- Lista de Gastos ---")
        if len(gastos) == 0:
            print("No hay gastos registrados.")
        else:
            for i, g in enumerate(gastos):
                print(f"[{i}] ${g:.2f}")
    
    elif opcion == 2:
        #Agregar Gasto: se concatena una lista de un solo elemento a la lista existente
        try:
            monto = float(input("\nDame el monto del gasto: "))
            if monto <= 0:
                print("Error: el monto debe ser positivo.")
            else:
                gastos = gastos + [monto]
                print(f"Gasto de ${monto:.2f} agregado correctamente.")
        except ValueError:
            print("Error: debes ingresar un número válido.")
    
    elif opcion == 3:
        #Modificar Gasto: se reemplaza directamente por indice, igual que nums[i] += 10
        if len(gastos) == 0:
            print("\nNo hay gastos registrados para modificar.")
        else:
            print("\n--- Lista de Gastos ---")
            for i, g in enumerate(gastos):
                print(f"[{i}] ${g:.2f}")
            try:
                indice = int(input("\n¿Qué gasto quieres modificar? (número de índice): "))
                if indice < 0 or indice >= len(gastos):
                    print("Error: ese gasto no existe.")
                else:
                    nuevo_monto = float(input("Dame el nuevo monto: "))
                    if nuevo_monto <= 0:
                        print("Error: el monto debe ser positivo.")
                    else:
                        gastos[indice] = nuevo_monto
                        print("Gasto modificado correctamente.")
            except ValueError:
                print("Error: debes ingresar números válidos.")
    
    elif opcion == 4:
        #Eliminar Gasto: se arma una lista nueva, copiando todo menos el indice elegido
        if len(gastos) == 0:
            print("\nNo hay gastos registrados para eliminar.")
        else:
            print("\n--- Lista de Gastos ---")
            for i, g in enumerate(gastos):
                print(f"[{i}] ${g:.2f}")
            try:
                indice = int(input("\n¿Qué gasto quieres eliminar? (número de índice): "))
                if indice < 0 or indice >= len(gastos):
                    print("Error: ese gasto no existe.")
                else:
                    monto_eliminado = gastos[indice]
                    gastos_nuevos = []
                    for i, g in enumerate(gastos):
                        if i != indice:
                            gastos_nuevos = gastos_nuevos + [g]
                    gastos = gastos_nuevos
                    print(f"Gasto de ${monto_eliminado:.2f} eliminado correctamente.")
            except ValueError:
                print("Error: debes ingresar un número válido.")
    
    elif opcion == 5:
        #Ver Total: se recorre la lista sumando cada valor
        total = 0
        for g in gastos:
            total += g
        print(f"\nEl total de tus gastos es: ${total:.2f}")
    
    elif opcion == 6:
        print("\n¡Hasta luego!")
        break
    
    else:
        print("\nOpción no válida.")
    
    input("\nPresiona Enter para continuar...")