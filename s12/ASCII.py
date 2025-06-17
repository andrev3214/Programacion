# Programa para escribir los caracteres ASCII

arch1 = open("ascii.txt", "w", encoding="utf-8")

for i in range(32, 127):
    arch1.write(f"{i}: {chr(i)}\n")

arch1.close()
print("Archivo 'ascii.txt' creado con la lista de caracteres ASCII.")