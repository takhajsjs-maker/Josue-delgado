
Lado1 = float(input("ingresa el valor del lado 1: "))
Lado2 = float(input("ingresa el valor del lado 2: "))
Lado3 = float(input("ingresa el valor del lado 3: "))   
if Lado1 == Lado2 == Lado3:
    print("El triángulo es equilátero")
elif Lado1 == Lado2 or Lado1 == Lado3 or Lado2 == Lado3:
    print("El triángulo es isósceles")
else:
    print("El triángulo es escaleno")
