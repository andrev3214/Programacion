# Programa para mostrar archivo ASCII

arch1 = open("ascii.txt", "r", encoding="utf-8")
print("Contenido del archivo ASCII:")

for linea in arch1:
    print(linea, end="")
    
arch1.close()