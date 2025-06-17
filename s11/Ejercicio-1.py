#Calcular presupuesto correspondiente a cada departamento

import Funciones as func

print()
monto=float(input("Ingrese el monto: "))

HR=func.ejer1(monto, 0.50)
Man=func.ejer1(monto, 0.25)
Emp=func.ejer1(monto, 0.15)
ads=func.ejer1(monto, 0.10)

print("\n=========================================================================\n")
print(f"El presupuesto para el departamento de Recursos Humanos es: {HR:.2f}")
print(f"El presupuesto para el departamento de Manufactura es: {Man:.2f}")
print(f"El presupuesto para el departamento de Empaquetado es: {Emp:.2f}")
print(f"El presupuesto para el departamento de Publicidad es: {ads:.2f}")
print("\n=========================================================================\n")