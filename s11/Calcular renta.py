#Programa para calcular renta

import Funciones as func
print()

N_emp=int(input("Ingrese el número de empleados: "))
renta=0
E_salario_neto=[]
E_salario=[]

for i in range(N_emp):
    while True:
        try:
            salario=float(input(f"Ingrese el salario del empleado {i+1}: "))
            salario_neto=salario-func.renta(salario)
            E_salario_neto.append(salario_neto)
            E_salario.append(salario)
            break
        except ValueError:
            print("\nPor favcor ingrese un número.")
            continue

for i in range(N_emp):
    print(f"El salario neto del empleado {i+1} es: {E_salario_neto[i]:.2f}")
    print(f"El salario bruto del empleado {i+1} es: {E_salario[i]:.2f}")