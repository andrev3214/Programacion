#Progarama para calcular la tabla de multplicación del 1 al 10 del número ingresado

import Funciones as func

print()

while True:
    try:
        num=float(input("Ingrese un número: "))
        break
    except ValueError:
        print("\nFavor ingrese un número.")
        continue

func.tabla(num)

salir=input("\nPresione 'Enter' para salir: ")
print("\n=========================================================================\n")