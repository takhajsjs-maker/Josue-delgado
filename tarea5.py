#Elegibilidad para Votar 🗳
#Enunciado: Verifica si alguien puede votar por su edad.
#Requerimientos: Pedir edad y usar un if para ver si es >= 18.


edad = int(input("ingresa tu edad: "))
if edad >= 18:
    print("si puedes votar ")
else:
    print(" no puedes votar porque eres menor de edad")

