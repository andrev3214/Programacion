# Programa para añadir texto a un archivo

arch1 = input("Ingrese el nombre del archivo: ")

archivo = open(arch1, "a", encoding="utf-8")
print("Escriba texto que desea agregar. Escriba 'Salir' para guardar y salir.")

while True:
    texto = input("Texto: ")
    if texto.upper().strip() == "SALIR":
        break
    archivo.write(texto + "\n")

archivo.close()
print("Se ha guardado el archivo.")