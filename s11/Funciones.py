def ejer1 (a, b):
    return a*b

def comision(a):
    comision_total = sum(a) * 0.10
    return comision_total

def renta (a):
    return a * 0.10

def trabajadas (a):
    if a<=160:
        return 6.5*a
    else:
        return 7.5*a

def calcular_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def a_circulo (r):
    return 3.1416*r**2

def menor_de_tres(a, b, c):
    return min(a, b, c)

def total (importe):
    if importe > 700:
        descuento = 0.12
    elif importe > 500:
        descuento = 0.10
    elif importe > 300:
        descuento = 0.05
    else:
        descuento = 0
    return importe - (importe * descuento)

def tabla (n):
    n = round(n, 2)
    for i in range (1, 11):
        resultado = n*i
        print(f"{n} x {i:2} = {resultado:.2f}")