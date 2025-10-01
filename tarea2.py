'''#Calculadora de Propinas 💵
#Enunciado: Calcula el total a pagar en un restaurante, añadiendo un 15% de propina.
#Requerimientos: Pedir costo con input(), calcular 15%, sumar y mostrar todo.


print("Calculadora de Propinas 💵")
costo_comida = float(input("Ingrese el costo de la comida: "))
propina = costo_comida * 0.15
total_a_pagar = costo_comida + propina
print(f"Costo de la comida: ${costo_comida:.2f}")
print(f"Propina (15%): ${propina:.2f}")
print(f"Total a pagar: ${total_a_pagar:.2f}")'''










'''#Verificador de Edad para Votar 🗳
# Enunciado: Un programa que te dice si tienes edad para votar.
#Requerimientos: Pedir la edad, usar un if-else y mostrar el mensaje correspondiente.

print("Verificador de Edad para Votar ")
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Usted es mayor de edad y puede votar.")
else:
    print("Usted es menor de edad y no puede votar.")'''




'''Suma de Números Pares ✨
Enunciado: Suma todos los números pares desde 1 hasta un número N.
Requerimientos: Pedir N, usar un for con un if dentro para encontrar y sumar los pares.

print("Suma de Números Pares ")
N = int(input("Ingrese un número N: "))
suma_pares = 0
for i in range(1, N + 1):
    if i % 2 == 0:
        suma_pares += i
print(f"La suma de los números pares desde 1 hasta {N} es: {suma_pares}")'''



'''#Suma de Números Pares ✨
#Enunciado: Suma todos los números pares desde 1 hasta un número N.
#Requerimientos: Pedir N, usar un for con un if dentro para encontrar y sumar los pares.

print("Suma de Números Pares ")
Num = int(input("Ingrese un número N: "))
suma_pares = 0
for i in range(1, Num + 1):
    if i % 2 == 0:
        suma_pares += i
print(f"La suma de los números pares desde 1 hasta {Num} es: {suma_pares}")'''







'''#Contador de Vocales 
#Enunciado: Cuenta cuántas vocales hay en un texto que ingrese el usuario.
#Requerimientos: Pedir texto, usar un for para recorrerlo y un if para contar las vocales (¡no olvides las mayúsculas!).

print("Contador de Vocales ")
texto = input("Ingrese un texto: ")
vocales = "aeiouAEIOU"
contador = 0
for char in texto:
    if char in vocales:
        contador += 1
print(f"El texto ingresado tiene {contador} vocales.")'''







