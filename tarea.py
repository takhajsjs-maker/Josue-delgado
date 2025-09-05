# de donde son, que edad tienen, y cual es tu nombre, y si tienes mas de 18 o menos.

lugar = input("¿De dónde eres? ") # where do they live
edad = int(input("¿Cuántos años tienes? ")) # how old are they   
nombre = input("¿Cuál es tu nombre? ") # what is your name
if  edad < 18:
    print("eres menor de edad")
elif edad == 18:
    print("tienes 18 ")
else:
    print("eres mayor de edad")

print(f"holaa {nombre}, un gusto, que edad tienes, {edad}, y donde vives, {lugar}") 
      
