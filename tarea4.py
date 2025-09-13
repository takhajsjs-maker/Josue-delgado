#Verificador de Número Par o Impar 🔢
#Enunciado: Determina si un número es par o impar.
#Requerimientos: Usar el operador módulo (%) y un if-else.

numero = int(input("Ingresa un número entero: "))
if numero % 2 == 0:
    print(f"el numero {numero} es par ")
else:
    print(f"el numero {numero} es impar ")
