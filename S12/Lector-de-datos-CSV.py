#Programa para leer datos de un CSV

print()

while True:
    try:
        arch1=input("Ingrese el nombre del archivo (por ejemplo: productos.csv): ")
        archivo=open(arch1, "r", encoding="utf-8")

        next(archivo)

        for linea in archivo:
            linea=linea.strip()
            partes=linea.split(",")
            producto = partes[0]
            precio = partes[1]
            stock = partes[2]

            print("\n===============================================================\n")
            print(f"El producto {producto} tiene un precio de {precio} y tiene {stock} unidades en stock.")
        break
    except (FileNotFoundError, StopIteration):
        print(f"\nEl archivo {arch1} no existe o está vacio, favor intentar de nuevo.")
        continue

archivo.close()

print("\n===============================================================\n")
salir=input("Presione enter para salir. ")