#Resolución de Ecuación Cuadrática 
#Enunciado: Resuelve una ecuación de segundo grado $ax^2 + bx + c = 0$.
#Requerimientos: Calcular el discriminante y usar if-elif-else para ver si hay 0, 1 o 2 soluciones reales.

import math
a = float(input("ingrese el ceoficiente a: "))
b = float(input("ingrese el ceoficiente b: "))
c = float(input("ingrese el ceoficiente c: "))

discriminante = b**2 - 4*a*c
if discriminante > 0:
    raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
    raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
    print(f"la ecuacion tiene dos soluciones reales: {raiz1} y {raiz2}")
elif discriminante == 0:
    raiz = -b / (2*a)
    print(f"la ecuacion tiene una solucion real: {raiz}")   
else:
    print("la ecuacion no tiene soluciones reales")
