#Calculadora de Calificaciones 🎓
#Enunciado: Convierte una nota de 0-100 a A, B, C, D, F.
#Requerimientos: Usar if-elif-else para los rangos de notas.


nota = int(input("ingresa tu nota(0-100): "))
if 90<= nota <=100:
    print(" tu nota es A")
elif 75<= nota <90:
    print(" tu nota es B")
elif 60<= nota <75: 
    print(" tu nota es C") 
elif 50<= nota <60:
    print(" tu nota es D")
elif 0<= nota <50:
    print(" tu nota es F")   