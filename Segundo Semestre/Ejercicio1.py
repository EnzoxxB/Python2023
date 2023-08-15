# Ejercicio 1: Iterar un rango de 0 a 10 e imprimir números divisibles entre 3

numeros = range(0,10,1)
# numeros = range(0,10,3) // Otra forma de hacerlo
print("Los numeros divisibles entre 3 son:")
for num in numeros:
    if (num%3 == 0):
        print(num)
