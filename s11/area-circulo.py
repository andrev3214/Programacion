#Programa para calcular area de un circulo

import Funciones as func

print()

while True:
    try:
        radio=float(input("Ingrese el radio del circulo: "))
        break
    except ValueError:
        print("\nPor favcor ingrese un número.")
        continue

print(f"\nEl area del circulo es: {func.a_circulo(radio):.2f}")

salir=input("\nPresione 'Enter' para salir: ")