#Verificación de Contraseña Simple 🔐
#Enunciado: Simula un login simple.
#Requerimientos: Guardar una contraseña en una variable, pedirla al usuario y comparar.

contraseña_guardada = "ryan18"
contraseña_guardada = contraseña_guardada.lower()
contraseña_guardada = contraseña_guardada 
contraseña_ingresada = input("Ingresa la contraseña: ")
if contraseña_ingresada == contraseña_guardada:
    print("tienes acceso")
else:
    print("contraseña mal escrita")
    


