#Programa para calcular el importe a pagar

import Funciones as func

print()

while True:
    try:
        importe=float(input("¿Cuantó costó su compra?: "))
        break
    except ValueError:
        print("\nPor favcor ingrese un número.")
        continue

print(f"\nEl importe a pagar es: ${func.total(importe):.2f}")

salir=input("\nPresione 'Enter' para salir: ")

print("\n=========================================================================\n")