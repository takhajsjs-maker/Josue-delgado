#Enunciado: Calcula el costo de envío por peso y zona de destino, aplicando descuentos.
#Requerimientos: Usar condicionales anidados (zona y luego peso).

peso = float(input("ingrese el peso del paquete en kg:"))
zona = int(input("ingrese la zona de destino (a,b,c):"))
costo = 0
if zona == 1:
    if peso <= 1:
        costo = 5
    elif 1 < peso <= 5:
        costo = 10
    else:
        costo = 20
elif zona == 2:
    if peso <= 1:
        costo = 7
    elif 1 < peso <= 5:
        costo = 14
    else:
        costo = 28
elif zona == 3: 
    if peso <= 1:
        costo = 10
    elif 1 < peso <= 5:
        costo = 20 
    else: 
        costo = 40
else: 
    print("zona no valida")
    print(f"el costo de envio es: {costo} dolares")
    if peso > 10:
        costo *= 0.9
        print(f"se aplico un descuento del 10% por peso, el costo final es: {costo} dolares")
    else:
        print(f"el costo final es: {costo} dolares")




