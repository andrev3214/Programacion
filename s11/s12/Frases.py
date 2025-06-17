#Programa para guarda frases en un archivo

arch1 = input("Escriba el nombre del archivo (por ejemplo: frases.txt): ")

archivo = open(arch1, "w", encoding="utf-8")
print("Escriba frases. Para guardar en el archivo y salir escriba 'Salir' y nada más.")

while True:
    frase = input("Frase: ")
    if frase.upper().strip() == "SALIR":
        break
    archivo.write(frase + "\n")

archivo.close()
print("Se ha guardado el archivo.")