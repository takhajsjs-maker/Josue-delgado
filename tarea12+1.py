#Verificador de Vocal o Consonante 🅰
#Enunciado: Pide un carácter y di si es vocal o consonante.
#Requerimientos: Convertir a minúscula y usar or o in para chequear.

caracter = input("ingrese un caracter:").lower()
if caracter in 'aeiou' and len(caracter) == 1 and caracter.isalpha():
    print(f"el caracter {caracter} es una vocal")
else:
    print(f"el caracter {caracter} es una consonante")
