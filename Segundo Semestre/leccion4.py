# lista = Mati, Marcos, Enzo, Ale

nombres = ["Mati", "Marcos", "Enzo", "Ale"]
print(nombres)
print(nombres[0:2])
print(nombres[ :3])
print(nombres[1: ])
# modificamos un valor
nombres[0] = "Matías"
print(nombres)
for nombre in nombres:
    print(nombre)
else:
    print("Se acabaron los elementos.")

# Preguntamos cuantos elementos tiene
print(f'la lista posee {len(nombres)} elementos')

# Agregamos un elemento
nombres.append("Ro")
print(nombres)
# Agregamos un elemento en un índice específico
nombres.insert(3, "Mari")
print(nombres)
# Eliminamos un elemento
nombres.remove("Mari")
print(nombres)
# Eliminar el último elemento
nombres.pop()
print(nombres)
# Eliminar un elemento de índice específico
del nombres[0]
print(nombres)
# Eliminar todos los elementos
nombres.clear()
print(nombres)
