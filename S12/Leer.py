#Programa para leer el contenido de un archivo
arch1 = input("Ingrese el nombre del archivo: ")

archivo = open(arch1, "r", encoding="utf-8")
contenido = archivo.read()

print("\nContenido del archivo:\n")
print(contenido)

archivo.close()