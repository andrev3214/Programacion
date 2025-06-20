#Programa para contar las lineas en un archivo

print()

while True:
    try:
        arch1=input("Ingrese el nombre de su archivo: ")
        archivo=open(arch1, "r", encoding="utf-8")
        break
    except FileNotFoundError:
        print(f"\nEl archivo {arch1} no existe, favor intentar de nuevo.")
        continue

lineas = archivo.readlines()

print("\n===============================================================\n")
if len(lineas) == 1:
    print(f"El archivo {arch1} tiene {len(lineas)} linea.")
else:
    print(f"El archivo {arch1} tiene {len(lineas)} lineas.")
print("\n===============================================================\n")

archivo.close()
salir=input("Presione enter para salir. ")