import math 
while True :
    print ("\nElige una opcion")
    print ("1.Rectangulo")
    print ("2.Triangulo")
    print ("3.Circulo")
    print ("4.Salir")
    figura = input("Figura: ")
    if figura == "4": 
        print ("Gracias por usar :)")
        break
    if figura == "1": 
        lado_1 = float(input("Escribe el lado horizontal del cuadrado: "))
        lado_2 = float(input("Escribe el lado vertical del cuadrado: "))
        Area = lado_1 * lado_2 
        print ("El area del cuadrado es: ", Area )
    elif figura == "2": 
         Base = float(input("Base: "))
         Altura = float(input ("Altura: "))
         Area = (Base * Altura) / 2
         print ("El area de la figura es: ", Area )
    elif figura == "3": 
        radio = float(input("Escribe el radio del circulo: ", Area ))
        Area = math.pi * radio ** 2
        print ("El area del circulo es: ")
    else: 
        print ("Figura aun no disponible")