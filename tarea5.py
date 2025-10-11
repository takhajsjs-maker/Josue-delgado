'''#Agenda de Contactos Simple:
#Enunciado: ¡Tu propia agenda digital!
#Requerimientos: Usa un diccionario para guardar nombres y teléfonos. Implementa funciones para agregar, buscar y eliminar contactos.

# Inicializamos la agenda como un diccionario vacío
agenda = {}

def agregar_contacto(nombre: str, telefono: str):
    
    nombre = nombre.strip().title() 
    telefono = telefono.strip()     

    if nombre in agenda:
        print(f"Contacto '{nombre}' actualizado. Teléfono anterior: {agenda[nombre]}, nuevo: {telefono}")
    else:
        print(f"Contacto '{nombre}' agregado con éxito.")

    agenda[nombre] = telefono

def buscar_contacto(nombre: str):

    nombre = nombre.strip().title()

    if nombre in agenda:
        print(f"\n--- Resultado de Búsqueda ---")
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {agenda[nombre]}")
        print(f"----------------------------")
    else:
        print(f"\n[ERROR] Contacto '{nombre}' no encontrado en la agenda.")

def eliminar_contacto(nombre: str):
    """
    Elimina un contacto de la agenda si existe.
    """
    nombre = nombre.strip().title()

    if nombre in agenda:
        
        telefono_eliminado = agenda.pop(nombre)
        print(f"Contacto '{nombre}' (teléfono: {telefono_eliminado}) eliminado con éxito.")
    else:
        print(f"\n[ERROR] No se puede eliminar. Contacto '{nombre}' no encontrado en la agenda.")

def mostrar_agenda():
    """
    Muestra todos los contactos guardados en la agenda.
    """
    if not agenda:
        print("\nLa agenda de contactos está vacía.")
        return

    print("\n--- AGENDA DE CONTACTOS ---")
    
    for nombre, telefono in sorted(agenda.items()):
        print(f"| Nombre: {nombre: <15} | Teléfono: {telefono: <15} |")
    print("----------------------------")

print("--- 1. AGREGAR CONTACTOS ---")
agregar_contacto("Alice Smith", "123-456-7890")
agregar_contacto("Bob Johnson", "987-654-3210")
agregar_contacto("Carlos Garcia", "555-123-4567")

mostrar_agenda()

print("\n--- 2. ACTUALIZAR CONTACTO ---")
agregar_contacto("Alice Smith", "111-222-3333")

mostrar_agenda()

print("\n--- 3. BUSCAR CONTACTOS ---")
buscar_contacto("Bob Johnson")
buscar_contacto("No Existe")

print("\n--- 4. ELIMINAR CONTACTOS ---")
eliminar_contacto("Carlos Garcia")
eliminar_contacto("No Existe")

mostrar_agenda()'''





'''from typing import List

def sumar_lista_con_bucle(numeros: List[float]) -> float:
    """
    Suma todos los números en una lista usando un bucle 'for'
    y retorna el total.

    Args:
        numeros: Una lista de números (enteros o flotantes).

    Returns:
        La suma total de todos los elementos de la lista.
    """
   
    suma_total = 0.0

    
    for numero in numeros:
        
        suma_total += numero  

    
    return suma_total

lista1 = [1, 2, 3, 4, 5]
resultado1 = sumar_lista_con_bucle(lista1)
print(f"La suma de {lista1} es: {resultado1}")

lista2 = [10.5, 20.25, 30.0]
resultado2 = sumar_lista_con_bucle(lista2)
print(f"La suma de {lista2} es: {resultado2}")

lista3 = [-5, 10, -2, 7]
resultado3 = sumar_lista_con_bucle(lista3)
print(f"La suma de {lista3} es: {resultado3}")

lista_vacia = []
resultado_vacio = sumar_lista_con_bucle(lista_vacia)
print(f"La suma de una lista vacía es: {resultado_vacio}")'''



'''Generador de Números Pares:
Enunciado: Muestra los números pares hasta 100.
Requerimientos: Usa un bucle while y el operador módulo (%).'''

'''def generar_pares_hasta_cien():
    print("--- Generador de Números Pares (0 a 100) ---")
    numero = 0
    while numero <= 100:
        # Usamos el operador módulo (%): si el resto de la división entre 2 es 0,
        # el número es par.
        if numero % 2 == 0:
            print(numero)
            numero += 1
generar_pares_hasta_cien()'''

