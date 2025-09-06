edad = int(input("ingrese su edad "))
inscrito = input("¿estas inscrito en el CNE? (si/no):  ").lower()
if edad >= 18 and inscrito == "si":
    print(" usted tiene la edad para votar y esta en inscrito en el CNE.")
else:
    print("usted no cumple con los requisitos para.")    
