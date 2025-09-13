#Calculadora de Descuento 💰
#Enunciado: Calcula un descuento del 15% si el precio supera los $100.
#Requerimientos: Usar if-else para aplicar el descuento y mostrar el precio final.




precio = float(input("Ingresa el precio del producto: "))
if precio > 100:
    descuento = precio * 0.15
    precio_final = precio - descuento
    print(f"El precio final con descuento es: {precio_final}")
else:
    print(f"El precio final es: {precio}")
