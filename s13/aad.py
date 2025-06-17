def reemplazar_palabra():
    archivo_entrada = "documento.txt"
    archivo_salida = "modificado.txt"

    palabra_buscar = input("Ingresa la palabra que deseas buscar: ")
    palabra_reemplazo = input("Ingresa la palabra por la que deseas reemplazarla: ")

    try:
        with open(archivo_entrada, "r", encoding="utf-8") as original:
            contenido = original.read()

        contenido_modificado = contenido.replace(palabra_buscar, palabra_reemplazo)

        with open(archivo_salida, "w", encoding="utf-8") as modificado:
            modificado.write(contenido_modificado)

        print(f"Se reemplazó '{palabra_buscar}' por '{palabra_reemplazo}' y se guardó en '{archivo_salida}'.")
    except FileNotFoundError:
        print(f"El archivo '{archivo_entrada}' no existe.")

reemplazar_palabra()
