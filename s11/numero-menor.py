#Programa para calcular el número menor

print()

import Funciones as func

while True:
    try:
        num1=float(input("Ingrese el número 1: "))
        num2=float(input("Ingrese el número 2: "))
        num3=float(input("Ingrese el número 3: "))
        break
    except ValueError:
        print("\nPor favcor ingrese un número.")
        continue

print("\nEl número menor es: ", func.menor_de_tres(num1, num2, num3))

salir=input("\nPresione 'Enter' para salir: ")