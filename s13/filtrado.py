def filtrar_lineas_por_palabra(archivo_entrada, archivo_salida, palabra_clave):
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as f_in:
            lineas = f_in.readlines()

        # Filtramos las líneas que contienen la palabra específica
        lineas_filtradas = [linea for linea in lineas if palabra_clave in linea]

        with open(archivo_salida, 'w', encoding='utf-8') as f_out:
            f_out.writelines(lineas_filtradas)

        print(f"Se han guardado {len(lineas_filtradas)} líneas en '{archivo_salida}' que contienen la palabra '{palabra_clave}'.")

    except FileNotFoundError:
        print(f"El archivo '{archivo_entrada}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# --- Programa principal ---
palabra = input("Introduce la palabra que deseas buscar: ").strip()
filtrar_lineas_por_palabra("libro.txt", "filtrado.txt", palabra)
