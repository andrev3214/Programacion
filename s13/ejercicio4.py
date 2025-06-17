# Abrir el archivo original para lectura
with open("original.txt", "r") as archivo_origen:
    contenido = archivo_origen.read()  # Leer todo el contenido

# Crear un nuevo archivo y escribir en él el contenido copiado
with open("copia.txt", "w") as archivo_destino:
    archivo_destino.write(contenido)

print("El contenido ha sido copiado exitosamente de original.txt a copia.txt.")
