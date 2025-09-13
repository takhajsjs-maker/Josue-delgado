
peso = float(input("ingrese su peso en kg: "))
altura = float(input("ingrese su altura en metros:"))

imc = peso / (altura **2)
print(f"tu indice de masa corporal es: {imc:.2f}")
if imc < 18.5:
    print("su peso es bajo")
elif 18.5 <= imc < 24.9:
    print("tienes un peso normal")
elif 25 <= imc < 29.9:
    print("eres gordito")
elif 30 <= imc < 34.9:
        print(" eres super gordito")
elif 35 <= imc < 39.9:
        print("eres super mega gordito")
else:
      print("eres super hiper mega gordito")


