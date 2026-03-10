import math 
def pedir_numero_positivo(mensaje):
    while True:
        try:
            numero = float(input(mensaje))

            if numero > 0:
                return numero
            else:
                print("Error: el numero debe ser positivo")

        except:
            print("Error: debes ingresar un numero")
while True :
    print ("\nElige una opcion")
    print ("1.Rectangulo")
    print ("2.Triangulo")
    print ("3.Circulo")
    print ("4.Cuadrado")
    print ("5.Salir")
    figura = input("Figura: ")
    if figura == "5": 
        print ("Gracias por usar :)")
        break
    if figura == "1": 
        lado_1 = pedir_numero_positivo("Escribe el lado horizontal del rectangulo: ")
        lado_2 = pedir_numero_positivo("Escribe el lado vertical del rectangulo: ")
        Area = lado_1 * lado_2 
        print ("El area del cuadrado es: ", Area )
        print ("Deseas calcular el perimetro?")
        respuesta = input ("Respuesta: ")
        if respuesta == "Si":
            perimetro = (lado_1 * 2) + (lado_2 * 2)
            print("El perimetro del rectangulo es: ", perimetro)
        else: 
            print("De acuerdo!")
    elif figura == "2": 
         Base = pedir_numero_positivo("Base: ")
         Altura = pedir_numero_positivo("Altura: ")
         Area = (Base * Altura) / 2
         print ("El area de la figura es: ", Area )
         print ("Deseas calcular el perimetro?")
         respuesta = input("Respuesta: ")
         if respuesta == "Si":
             print("El triangulo es equilatero?")
             equilatero = input("Respuesta: ")
             if equilatero == "Si":
                 perimetro = Base * 3
                 print ("El perimetro del triangulo es: ", perimetro)
             else:
                 print("Escribe los otros 2 lados del triangulo")
                 lado_2 = pedir_numero_positivo("Lado 2: ")
                 lado_3 = pedir_numero_positivo("Lado 3: ")
                 perimetro = Base + lado_1 + lado_2 
                 print("El perimetro del triangulo es: ", perimetro)
         else: 
             print("De acuerdo!")
    elif figura == "3": 
        radio = pedir_numero_positivo("Escribe el radio del circulo: ", Area )
        Area = math.pi * radio ** 2
        print ("El area del circulo es: ")
        print ("Deseas calcular el perimetro?")
        respuesta = input("Respuesta: ")
        if respuesta == "Si":
            perimetro = (2 * radio ) * math.pi 
            print ("El perimetro del circulo es: ", perimetro)
        else: 
            print ("De acuerdo!")
    elif figura == "4":
        lado = pedir_numero_positivo("Escribe el lado del cuadrado: ")
        Area = lado * lado 
        print ("El area del cuadrado es: ", Area )
        print ("Deseas calcular el perimetro?")
        respuesta = input("Respuesta: ")
        if respuesta == "Si":
            perimetro = lado * 4 
            print ("El perimetto del cuadrado es :", perimetro )
        else: 
            print ("De acuerdo!")
    else: 
        print ("Figura aun no disponible")