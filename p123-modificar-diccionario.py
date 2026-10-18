# p123-modificar-diccionario.py
# Modificar valores de un diccionario
print('\033[H\033[J')
paises = {
    'Argentina': 100,
    'Brasil': 200,
    'Colombia': 300,
    'Chile': 400,
    'Ecuador': 500,
    'Bolivia': 600,
    'Jamaica': 700
}

print("Diccionario inicial:")
print(paises)

# Modificar usando []
paises['Brasil'] = 250
paises['Chile'] = 450

# Modificar usando update()
paises.update({'Bolivia': 650})
paises.update({'Jamaica': 750})

print("\nDiccionario modificado:")
print(paises)