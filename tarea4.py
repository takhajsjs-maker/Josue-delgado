#Mi Primera Lista:
#Enunciado: Organiza tus frutas favoritas.
#Requerimientos: Crea una lista, accede al primer y último elemento, agrega uno nuevo e imprime todo.

'''frutas =["manzana", "banana", "uva", "naranja"]
print(f"lista inicial de frutas: {frutas}")

primera_fruta = frutas[0]
print(f"la primera fruta es: {primera_fruta}")

ultima_fruta = frutas[-1]
print(f"la ultima fruta es: {ultima_fruta}")

nueva_fruta = "fresa"
frutas.append(nueva_fruta)
print(f"fruta agregada: {nueva_fruta}")

print(f"la lista de frutas actualizadas: {frutas}")'''

'''Verificador de Mayoría de Edad:
Enunciado: ¿Puedes entrar al club? 😉
Requerimientos: Pide una edad y usa un if-else para verificar si es mayor o igual a 18.'''

'''edad = int(input("ingrese su edad"))
edad_minima = 18

if edad >= edad_minima:
    
    print(f"Tienes {edad} años Eres mayor de edad")
else:
   
    print(f"Tienes {edad} años. Eres menor de edad.")'''

'''Tabla de Multiplicar:
   - Enunciado: Genera la tabla de multiplicar de un número.
   - Requerimientos: Pide un número y usa un bucle for del 1 al 10.'''

'''numero = int(input("ingrese un numero que quieras ver la tabla de multiplicacion: "))
print(f"\n tabla de multiplicar del {numero}")

for i in range(1,11):
    resultado = numero * i

    print(f"{numero}*{i} = {resultado}")'''


'''Contador de Vocales:
   - Enunciado: Cuenta las vocales de un texto.
   - Requerimientos: Crea una función que reciba un string, cuente las vocales (a, e, i, o, u) y retorne el total.'''

'''def contar_vocales(texto: str)-> int:
    texto_limpio = texto.lower()
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in texto_limpio:
        if letra in vocales:
            contador += 1

    return contador

frase_usuario = input("Introduce una frase para contar sus vocales: ")
total_vocales = contar_vocales(frase_usuario)
print(f"\nANÁLISIS DE LA FRASE: '{frase_usuario}'")
print(f"-> El número total de vocales es: {total_vocales}")'''













    
