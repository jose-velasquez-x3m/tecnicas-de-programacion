#objetivo: evaluacion parcial
#nombre: Velasquez Ramos Jose Gabriel
#Fecha: 13/04/2025
 
#entrada
Usuario = "Velasquez".upper
Contraseña = 75863065
cantAlumnos = 0
Masculino = 0
Femenino = 0
conLentes = 0
sinLentes = 0
mayorEdad = 0
menoredad = 0
montoRecaudado = 0
while(True):
    MenuMando = int(input("""
    1.AUTENTICARSE
    2.REGISTRAR DONACIONES
    3.CALCULADORA
    4.REPORTE TOTAL
    5.SALIR DE EL PROGRAMA
    """))

    if(MenuMando == 1):
        Usuario = str(input("Ingrese su Usuario: "))
        Contraseña = int(input("Ingrese su contraseña: "))
        if(Usuario == "Velasquez")and(Contraseña == 75863065):
            print("Bienvenido estimado estudiante")
            break
        else:
            print("Error, vuelva a intentarlo")

    elif(MenuMando == 2):
      while(True):

        seccion = str(input("Ingrese su seccion(A/B/C/D): ")).upper
        if (seccion == "A" or seccion == "B" or seccion == "C" or seccion == "D"):
            break
        else:
            print("Por favor ingrese una seccion valida")
      while(True):

        cantAlumnos = int(input("Ingrese la cantidad de alumnos: "))
        cantAlumnos += 1
        if (cantAlumnos > 0):
            str(input("Ingrese el apellido paterno del alumno: "))
            Dni= int(input("Ingrese el DNI del alumno: "))
            if (Dni > 9999999 and Dni < 100000000):
                break
            else:
                print("Ingrese un numero valido")
            
            genero=str(input("Ingrese el Genero (M/F) del alumno: ")).upper()
            if (genero == "M"):
                Masculino+=1
            elif (genero == "F"):
                Femenino+=1
                break
            else:
                print("Ingrese un dato valido (M/F)")
            usolentes=bool(input("Ingrese si el alumno usa lentes: "))
            if (usolentes == True):
                conLentes+=1
            elif(usolentes == False):
                sinLentes+=1
                break
            else:
                print("Ingrese un dato valido (1/0)")
            edad=int(input("Ingrese la edad del alumno: "))
            if (edad > 17):
                mayorEdad+=1
            elif (edad < 17):
                menoredad+=1
                break    
            montoRecaudado = int(input("Ingrese el monto recaudado: "))
            montoRecaudado += montoRecaudado
        else:
            print("Ingrese un numero valido")
    elif(MenuMando == 3):
        while (True):
            calculadora = int(input("""
            1.Suma de dos numeros
            2.Resta de dos numeros
            3.Multiplicar dos numeros
            4.Dividir dos numeros
            5.Modulo de dos numeros
            """))

            if(calculadora == 1):
                num1 = int(input("Ingrese el primer numero: "))
                num2 = int(input("Ingrese el segundo numero: "))
                resultado = num1 + num2
                print("La suma es:", resultado)
            elif(calculadora == 2):
                num1 = int(input("Ingrese el primer numero: "))
                num2 = int(input("Ingrese el segundo numero: "))
                resultado = num1 - num2
                print("La resta es:", resultado)
            elif(calculadora == 3):
                num1 = int(input("Ingrese el primer numero: "))
                num2 = int(input("Ingrese el segundo numero: "))
                resultado = num1 * num2
                print("La multiplicacion es:", resultado)
            elif(calculadora == 4):
                num1 = int(input("Ingrese el primer numero: "))
                num2 = int(input("Ingrese el segundo numero: "))
                resultado = num1 / num2
                if num1 or num2 == 0:
                    print("No se puede dividir entre cero")
            elif(calculadora == 5):
                num1 = int(input("Ingrese el primer numero: "))
                num2 = int(input("Ingrese el segundo numero: "))
                resultado = num1 % num2
                print("El modulo es:", resultado)
            else:
                print("Ingrese un dato valido porfavor")
    elif(MenuMando == 4):
        print ("cantidad de alumnos masculinos: ", Masculino)
        print ("cantidad de alumnos femeninas: ", Femenino)
        if (conLentes and Femenino):
            print ("cantidad de alumnas que usan lentes: ", conLentes)
        if (conLentes and Masculino):
            print ("cantidad de alumnos que usan lentes: ", conLentes)
        print ("cantidad de alumnos que no usan lentes: ", sinLentes)
        print ("cantidad de alumnos mayores de edad: ", mayorEdad)
        print ("cantidad de alumnos menores de edad: ", menoredad)
        print ("la seccion ingresada es: ", seccion)
        print ("monto total recaudado: ", montoRecaudado)
        print ("monto total recaudado: ", montoRecaudado - 50)
        print ("monto neto recaudado: ", montoRecaudado - 50)

    elif(MenuMando == 5):
        print("Esta saliendo de tecnicas de programacion :P")
        break