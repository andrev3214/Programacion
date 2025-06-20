#Programa para hacer una lista de compras

arch1=input("\nIngrese el nombre del archivo: ")
archivo=open(arch1, "w", encoding="utf-8")

while True:
    texto=input("\nEscriba un producto (Si quiere salir escriba 'Salir'): ")

    if texto.upper().strip() == "SALIR":
        break
    archivo.write(texto + "\n")
    print("\nSe ha guardado el producto escrito.")
    print("\n===========================================\n")

archivo.close()

print("\n==================================================================================\n")
salir=input("Se ha guardado la lista de compras exitosamente. Presione enter para salir. ")