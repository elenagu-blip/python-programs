
# ============================================================
# Archivo: p136-segundo-examen-parcial.py
# Programa: AeroRegistro
# Descripcion: Registro y analisis de vuelos
# ============================================================
print('\033[H\033[J')  # Limpiar la pantalla
# FASE 1: CAPTURA Y ALMACENAMIENTO DE VUELOS

# Lista que almacena los diccionarios de cada vuelo.
vuelos = []

# Repetir la captura hasta recibir una señal de salida.
while True:
    numero_vuelo = input("Ingrese el numero de vuelo (o * para terminar): ")

    # Terminar si el numero de vuelo esta vacio o es "*".
    if numero_vuelo == "" or numero_vuelo == "*":
        break

    # Capturar los datos generales del vuelo.
    origen = input("Ingrese el origen: ")
    destino = input("Ingrese el destino: ")
    aerolinea = input("Ingrese la aerolinea: ")

    # Validar que la cantidad de pasajeros sea un entero.
    while True:
        try:
            pasajeros = int(input("Ingrese la cantidad de pasajeros: "))
            break
        except ValueError:
            print("Error: ingrese un numero entero valido.")

    # Validar que la tarifa sea un numero.
    while True:
        try:
            tarifa = float(input("Ingrese la tarifa: "))
            break
        except ValueError:
            print("Error: ingrese una tarifa numerica valida.")

    # Agrupar los datos del vuelo en un diccionario.
    vuelo = {
        "numero_vuelo": numero_vuelo,
        "origen": origen,
        "destino": destino,
        "aerolinea": aerolinea,
        "pasajeros": pasajeros,
        "tarifa": tarifa
    }

    # Agregar el diccionario a la lista de vuelos.
    vuelos.append(vuelo)


# FASE 2: DESTINOS UNICOS E HISTORIAL

# Crear un conjunto para almacenar destinos sin repetirlos.
destinos_unicos = set()

# Crear una lista para guardar el historial de vuelos.
historial_vuelos = []

# Recorrer los vuelos registrados.
for vuelo in vuelos:

    # Agregar el destino al conjunto.
    destinos_unicos.add(vuelo["destino"])

    # Crear una tupla con los datos principales del vuelo.
    registro = (
        vuelo["numero_vuelo"],
        vuelo["aerolinea"],
        vuelo["destino"]
    )

    # Guardar la tupla en el historial.
    historial_vuelos.append(registro)


# FASE 3: PRESENTACION DE LOS DATOS

# Mostrar la lista original de diccionarios.
print("\n========== DATOS CRUDOS ==========")
print(vuelos)

# Mostrar los destinos unicos registrados.
print("\n========== DESTINOS UNICOS ==========")
print(destinos_unicos)

# Mostrar la lista de tuplas del historial.
print("\n========== HISTORIAL DE VUELOS ==========")
print(historial_vuelos)

# Mostrar el encabezado de la tabla.
print("\n============================== TABLA DE VUELOS ==============================")

# Alinear los nombres de las columnas.
print(
    f"{'No. Vuelo':<12}"
    f"{'Origen':<20}"
    f"{'Destino':<20}"
    f"{'Aerolinea':<22}"
    f"{'Pasajeros':>12}"
    f"{'Tarifa':>15}"
)

# Dibujar una linea separadora.
print("-" * 101)

# Recorrer los vuelos para mostrar sus datos en columnas.
for vuelo in vuelos:
    print(
        f"{vuelo['numero_vuelo']:<12}"
        f"{vuelo['origen']:<20}"
        f"{vuelo['destino']:<20}"
        f"{vuelo['aerolinea']:<22}"
        f"{vuelo['pasajeros']:>12}"
        f"{vuelo['tarifa']:>15,.2f}"
    )

# Cerrar la tabla.
print("-" * 101)


# FASE 4: RESUMEN ESTADISTICO

# Obtener la cantidad total de vuelos registrados.
total_vuelos = len(vuelos)

# Mostrar el encabezado y el total de vuelos.
print("\n" + "=" * 60)
print("             RESUMEN ESTADISTICO DE VUELOS")
print("=" * 60)
print(f"\nTotal de vuelos registrados: {total_vuelos}")

# Comprobar que existan vuelos antes de calcular estadisticas.
if total_vuelos > 0:

    # Crear diccionarios para contar vuelos por aerolinea y destino.
    vuelos_por_aerolinea = {}
    vuelos_por_destino = {}

    # Inicializar los acumuladores.
    total_pasajeros = 0
    suma_tarifas = 0.0

    # Recorrer los vuelos para contar y acumular datos.
    for vuelo in vuelos:
        aerolinea = vuelo["aerolinea"]
        destino = vuelo["destino"]

        # Contar los vuelos de cada aerolinea.
        vuelos_por_aerolinea[aerolinea] = (
            vuelos_por_aerolinea.get(aerolinea, 0) + 1
        )

        # Contar los vuelos de cada ciudad de destino.
        vuelos_por_destino[destino] = (
            vuelos_por_destino.get(destino, 0) + 1
        )

        # Acumular pasajeros y tarifas.
        total_pasajeros += vuelo["pasajeros"]
        suma_tarifas += vuelo["tarifa"]

    # Calcular los promedios por vuelo.
    promedio_pasajeros = total_pasajeros / total_vuelos
    promedio_tarifas = suma_tarifas / total_vuelos

    # Identificar los vuelos con las tarifas extrema superior e inferior.
    vuelo_mas_caro = max(vuelos, key=lambda vuelo: vuelo["tarifa"])
    vuelo_mas_barato = min(vuelos, key=lambda vuelo: vuelo["tarifa"])

    # Mostrar el conteo de vuelos por aerolinea.
    print("\n--- VUELOS POR AEROLINEA ---")
    for aerolinea, cantidad in vuelos_por_aerolinea.items():
        print(f"{aerolinea:<25} {cantidad:>5} vuelo(s)")

    # Mostrar el conteo de vuelos por destino.
    print("\n--- VUELOS POR CIUDAD DE DESTINO ---")
    for destino, cantidad in vuelos_por_destino.items():
        print(f"{destino:<25} {cantidad:>5} vuelo(s)")

    # Mostrar el total y el promedio de pasajeros.
    print("\n--- ESTADISTICAS DE PASAJEROS ---")
    print(f"Total de pasajeros:       {total_pasajeros:,}")
    print(f"Promedio de pasajeros:    {promedio_pasajeros:,.2f}")

    # Mostrar la suma y el promedio de las tarifas.
    print("\n--- ESTADISTICAS DE TARIFAS ---")
    print(f"Suma de tarifas:          ${suma_tarifas:,.2f}")
    print(f"Promedio de tarifas:      ${promedio_tarifas:,.2f}")

    # Mostrar el numero y la tarifa del vuelo mas caro.
    print("\n--- VUELO MAS CARO ---")
    print(f"Numero de vuelo:           {vuelo_mas_caro['numero_vuelo']}")
    print(f"Tarifa:                    ${vuelo_mas_caro['tarifa']:,.2f}")

    # Mostrar el numero y la tarifa del vuelo mas barato.
    print("\n--- VUELO MAS BARATO ---")
    print(f"Numero de vuelo:           {vuelo_mas_barato['numero_vuelo']}")
    print(f"Tarifa:                    ${vuelo_mas_barato['tarifa']:,.2f}")

# Evitar calculos cuando no se registraron vuelos.
else:
    print("\nNo hay vuelos registrados.")
    print("No es posible calcular promedios ni identificar")
    print("los vuelos mas caros o mas baratos.")

# Mostrar el cierre del resumen estadistico.
print("\n" + "=" * 60)
print("             FIN DEL RESUMEN")
print("=" * 60)
