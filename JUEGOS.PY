print(" imagina que estas en el accidente de los Andes, y tienes que sobrevivir con pocos recursos durante 72 dias")
opcion_1 = input("cual escojes : QUEDARSE o BUSCAR AYUDA ").lower()
if opcion_1 == "buscar ayuda":
    print("subes la montaña y te das cuenta que estas en el medio de la nada pero a lo lejos vez la otra parte del avion")
    opcion_2_1 = input("\n que haces IR A INVESTIGAR O REGRESAR \n").lower()
    if opcion_2_1 == "ir a investigar":
        print("estas caminando hacia el avion")
        print("al ir llegando te sientes debil y hambriento")
        print(
            "al abrir forzar la puerta del avion logras entrar y te encuentras con suministros (agua,chocolates,y galletas)")
        otra = input("\n LLEVAR LOS SUMINISTROS A TODOS (1) O ESCONDERLOS SOLO PARA TI (2) \n").lower()
        if otra == "1" :
            print("al regresar cuando vas a mitad de camino sufres por una avalancha y Mueres")

        elif otra == "2" :
            print("te llevaste los suministros al otro pedazo del avion")
if opcion_1 == "quedarse":
    print("tienes que compartir tu comida con tus compañeros hasta que se termine")
    opcion_1_1 = input(" \n que haces? TRATAS DE GUARDAR COMIDA Y COMES UNA VEZ AL DIA O COMES NORMAL \n : ").lower()
    if opcion_1_1 == "tratas de guardar comida y comes una vez al dia":
        print("lo haces y al dia 25 no hay mas comida")
        print("al terminarse la comida piensas si comer con los cuerpos de tus amigos muertos, que haras?")
        otra = input("\n COMERTE LOS CUERPOS O MORIRTE DE HAMBRE :").lower()
        if otra == "comerte los cuerpos":
            print("empiezas a buscar los cuerpos de tus compañeros para cortarlos, y despues comertelo")
        elif otra == "morirte de hambre":
            print("mueres a los dias sin posibilidades de sobrevivir")
        else:
            print("estas muy indesiso y no sabes que hacer")
    elif opcion_1_1 == "comes normal":
        print("se te acaba la comida super rapido, no tienes nada")
        opcion_1_2 = input()
    else:
        print(" estas muy indesiso y no sabes que hacer")          