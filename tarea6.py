#Comparador de Números ⚖
#Enunciado: Compara dos números (mayor, menor o igual).
#Requerimientos: Usar una estructura if-elif-else.

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
if num1 > num2:
    print(f"El número {num1} es mayor que {num2}")
elif num1 < num2:
    print(f"El número {num1} es menor que {num2}")
else:
    print(f"El número {num1} es igual a {num2}")


