#Clasificador de Números ➕➖
#Enunciado: Indica si un número es positivo, negativo o cero.
#Requerimientos: Implementar con una cadena if-elif-else.


num = float(input("Ingresa un número: "))
if num > 0:
    print(f"El número {num} es positivo")
elif    num < 0:
    print(f"El número {num} es negativo")
else:
    print("el numero es cero")