#Calcular comisiones de vendedores

import Funciones as func

print()
nVen=int(input("Ingrese el número de vendedores: "))
ventas=[]

for i in range(nVen):
    salario=float(input(f"\nIngrese el salario del vendedor {i+1}: "))
    print()

    for j in range(3):
        venta=float(input(f"Ingrese la venta {j+1} del vendedor {i+1}: "))
        ventas.append(venta)
    
    func.comision(ventas)
    total_semana=salario+func.comision(ventas)

    print(f"El vendedor {i+1} tiene una comisión de: {func.comision(ventas):.2f}")
    print(f"El salario total del vendedor {i+1} es: {total_semana:.2f}")
    
    ventas=[]