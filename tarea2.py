print("calculadora simple\n")

operacion = input("elige la operacion que deseas realizar(SUMA, RESTA, MULTIPLICACION Y DIVISION ) ")

if operacion ==  "SUMA":
    n1 = float(input("ingrese un numero"))
    n2 = float(input("ingrese otro numero"))
    nf = n1 + n2

    print(f"el resultado final es: {nf}")

if operacion == "RESTA":
    n1_1 = float(input("ingrese un numero"))
    n1_2 = float(input("ingrese otro numero"))
    n1_f = n1_1 - n1_2

    print(f" el resultado final es: {n1_f} ")

if operacion == "MULTIPLICACION":
    n2_1 = float(input("mostrar un numero"))
    n2_2 = float(input("mostrar otro numero"))
    n2_f = n2_1 * n2_2

    print(f"el resultado final es: {n2_f}")

if operacion == "DIVISION":
    n3_1 = float(input("mostrar un numero"))
    n3_2 = float(input("mostrar otro numero"))
    n3_f = n3_1/n3_2

    print(f"el relsultado final es: {n3_f}")    

