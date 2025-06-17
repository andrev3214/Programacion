#Factorial

import Funciones as func

numero = int(input("Ingrese un número entero positivo: "))

if numero < 0:
    print("El factorial no está definido para números negativos.")
else:
    resultado = func.calcular_factorial(numero)
    print(f"El factorial de {numero} es {resultado}")