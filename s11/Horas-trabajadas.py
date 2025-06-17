#Programa para calcular salario

import Funciones as func

print()

while True:
    try:
        horas=float(input("Ingrese el número de horas trabajadas: "))
        break
    except ValueError:
        print("\nPor favcor ingrese un número.")
        continue

print(f"El valor a pagar es: ${func.trabajadas(horas):.2f}")