#Año Bisiesto 🗓
#Enunciado: Determina si un año es bisiesto.
#Requerimientos: Usar condicionales anidados o lógicos para la regla completa.

año = int(input("Ingresa un año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")