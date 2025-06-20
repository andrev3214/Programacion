#Programa para hacer un diario

from datetime import datetime

arch1=input("\nIngrese el nombre del archivo: ")
archivo=open(arch1, "a", encoding="utf-8")

while True:
    ahora = datetime.now()
    fecha = ahora.strftime("%Y-%m-%d %H:%M:%S")

    entrada=input("\nEscriba una enterada (Si quiere salir escriba 'Salir'): ")

    if entrada.upper().strip() == "SALIR":
        break 
    archivo.write(f"{fecha}\n{entrada}\n\n")
    print("Se ha guardado la entrada escrita.")
    print("\n===========================================\n")

archivo.close()

print("\n==================================================================================\n")
salir=input("Se ha guardado el archivo exitosamente. Presione enter para salir. ")