# p085_SimuladorVentaCombustible.py
# Simula la venta de combustible, rendimiento y clasificación de clientes

while True:
    print("\033[2J\033[H", end="")

    # MENÚ PRINCIPAL
    print("SIMULADOR DE VENTA DE COMBUSTIBLE")
    print("1.- Venta de combustible")
    print("2.- Simulación de rendimiento")
    print("3.- Clasificador de cliente")
    print("4.- Salir")

    # OPCIÓN DEL USUARIO
    opcion = int(input("Dame la opción deseada: "))

    # VENTA DE COMBUSTIBLE
    if opcion == 1:
        print("\033[2J\033[H", end="")

        print("VENTA DE COMBUSTIBLE")
        print("1.- Gasolina Magna")
        print("2.- Gasolina Premium")
        print("3.- Diésel")
        print("4.- Regresar al menú principal")

        tipo_combustible = int(input("Dame el tipo de combustible: "))

        # SELECCIÓN DEL COMBUSTIBLE
        if tipo_combustible == 1:
            nombre_combustible = "Gasolina Magna"
        elif tipo_combustible == 2:
            nombre_combustible = "Gasolina Premium"
        elif tipo_combustible == 3:
            nombre_combustible = "Diésel"
        elif tipo_combustible == 4:
            continue
        else:
            print("\nCombustible no válido")
            input("Presiona Enter para volver al menú principal...")
            continue

        # DATOS DE LA VENTA
        precio = float(input("Dame el precio por litro: $"))
        cantidad_litros = float(input("Dame la cantidad de litros a vender: "))

        # VALIDACIÓN DE LOS DATOS
        if precio <= 0 or cantidad_litros <= 0:
            print("\nEl precio y la cantidad de litros deben ser mayores que cero")
            input("Presiona Enter para volver al menú principal...")
            continue

        # CÁLCULOS DE LA VENTA
        total = precio * cantidad_litros
        litros_completos = cantidad_litros // 1
        fraccion_litro = cantidad_litros % 1

        # RESUMEN DE LA VENTA
        print("\nRESUMEN DE VENTA")
        print(f"{'Combustible:':>22} {nombre_combustible}")
        print(f"{'Precio por litro:':>22} ${precio:>10.2f}")
        print(f"{'Cantidad de litros:':>22} {cantidad_litros:>10.2f} L")
        print(f"{'Litros completos:':>22} {litros_completos:>10.0f} L")
        print(f"{'Fracción de litro:':>22} {fraccion_litro:>10.2f} L")
        print(f"{'Total a pagar:':>22} ${total:>10.2f}")

        input("\nPresiona Enter para volver al menú principal...")
        continue

    # SIMULACIÓN DE RENDIMIENTO
    if opcion == 2:
        print("\033[2J\033[H", end="")

        print("SIMULACIÓN DE RENDIMIENTO")

        km_inicial = float(input("Dame el kilometraje inicial del vehículo: "))
        rendimiento = float(input("Dame el rendimiento del combustible (km/L): "))
        periodos = int(input("Dame la cantidad de periodos a proyectar: "))
        km_por_periodo = float(input("Dame los kilómetros estimados en el primer periodo: "))
        incremento = float(input("Dame el aumento porcentual del recorrido por periodo (0 si no aumenta): "))

        # VALIDACIÓN DE LA SIMULACIÓN
        if km_inicial < 0 or rendimiento <= 0 or periodos <= 0 or km_por_periodo <= 0 or incremento < 0:
            print("\nDatos no válidos para la simulación de rendimiento")
            input("Presiona Enter para volver al menú principal...")
            continue

        consumo_acumulado = 0.0
        km_actual = km_inicial

        # ENCABEZADO DE LA TABLA
        print("\nPROYECCIÓN DE RENDIMIENTO DEL COMBUSTIBLE")
        print(f"{'Periodo':>8} {'Km inicial':>14} {'Km final':>14} {'Consumo (L)':>15} {'Acumulado (L)':>16}")
        print(f"{'=' * 8} {'=' * 14} {'=' * 14} {'=' * 15} {'=' * 16}")

        # PROYECCIÓN DE CADA PERIODO
        for periodo in range(1, periodos + 1):

            # ** calcula el crecimiento compuesto del recorrido
            factor_crecimiento = (1 + incremento / 100) ** (periodo - 1)

            recorrido_periodo = km_por_periodo * factor_crecimiento
            km_final = km_actual + recorrido_periodo
            consumo_periodo = recorrido_periodo / rendimiento
            consumo_acumulado = consumo_acumulado + consumo_periodo

            # MOSTRAR RENGLÓN DE LA TABLA
            print(f"{periodo:>8} {km_actual:>14.2f} {km_final:>14.2f} {consumo_periodo:>15.2f} {consumo_acumulado:>16.2f}")

            # ACTUALIZAR EL KILOMETRAJE
            km_actual = km_final

        input("\nPresiona Enter para volver al menú principal...")
        continue

    # CLASIFICADOR DE CLIENTE
    if opcion == 3:
        print("\033[2J\033[H", end="")

        print("CLASIFICADOR DE CLIENTE")

        volumen_mes = float(input("Dame el volumen de combustible comprado en el mes (L): "))

        if volumen_mes < 0:
            print("\nEl volumen debe ser mayor o igual que cero")
        elif volumen_mes < 100:
            print("\nCliente Regular")
        elif volumen_mes >= 100 and volumen_mes <= 500:
            print("\nCliente Premium")
        else:
            print("\nFlotilla Corporativa")

        input("Presiona Enter para volver al menú principal...")
        continue

    # SALIDA DEL PROGRAMA
    if opcion == 4:
        print("\nSaliendo del programa...")
        break

    # OPCIÓN INCORRECTA
    else:
        print("\nOpción no válida. Intenta de nuevo.")
        input("Presiona Enter para volver al menú principal...")
        continue