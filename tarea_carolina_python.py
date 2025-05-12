
def ejecutable_1 ():
    def calculadora(operacion, num1, num2):
        if operacion == "suma":
            result = num1 + num2
        elif operacion == "resta":
            result = num1 - num2
        elif operacion == "division":
            result = num1 / num2
        elif operacion == "multiplicacion":
            result = num1 * num2
        else:
            print("operación no válida.")
            return
        print(result)

    print("Calculadora")
    num1 = input("inserte el primer número de la ecuación:  ")
    num2 = input("inserte el segundo número de la ecuación:  ")
    operacion = input("inserte el tipo de operación de la ecuación, [suma] [resta] [division] [multiplicacion]:  ")

    calculadora(operacion, int(num1), int(num2))

def ejecutable_2():
    def indice_masa_corporal():
        resultado = float(kilo_gramos) / (float(metros)*float(metros))
        resultado_redondeado = round(resultado,2)
        print("Tu indice de masa corporal es: ", resultado_redondeado)

    print("Indice de masa corporal (IMC)")
    kilo_gramos = input("favor, ingresar su peso en kilogramos:  ")
    metros = input("favor, ingresar su altura en metros:  ")

    indice_masa_corporal()

def ejecutable_3():
    def division():
        resultado = int(num1) / int(num2)
        cociente = int(num1) // int(num2)
        resto = int(num1) % int(num2)

        print("Tu division es: ", num1, "/",num2)
        print("el resultado es: ", resultado)
        print("el cociente es: ", cociente)
        print("el resto es: ", resto)

    print("incerte dos numeros enteros:")
    num1 = input("primer numero: ")
    num2 = input("segundo numero: ")
    division()

def ejecutable_4():
    print("Cálculo de intereses")
    print("Los intereses de la cuenta de ahorro son 4% al año")
    dinero_depositado = float(input("Por favor, inserte la cantidad de dinero depositado en la cuenta de ahorros: "))
    year =0
    for year in range(3):
        year += 1
        resultado = dinero_depositado * (1 + 0.04) * year
        resultado_redondeado = round(resultado, 2)
        print("Cantidad de ahorros tras el", year ,"año:  ", resultado_redondeado)

def ejecutable_5():
    nombre = input("favor, insertar su nombre completo: ")
    print(" ")
    print("El nombre completo es: ", nombre)
    print(" ")
    print(nombre.lower())
    print(nombre.upper())
    print(nombre.capitalize())

def ejecutable_6():
    user = input("favor, insertar su nombre de usuario: ")
    print(" ")
    cant_letra = user.count("")
    print("El nombre de usuario es: ", user.upper())
    print("El nombre de usuario tiene: ", cant_letra-1, "letras")

def ejecutable_7():
    print("numero de telefono de una empresa")
    numero_tel = input("inserte el numero de telefono de una empresa en un formato +34-número-extensión: ")
    partes = numero_tel.split('-')
    print(partes)
    print(partes[1])

def ejecutable_8():
    cantidad = input("favor, insertar la cantidad de asignaturas del curso: ")
    number = 0
    lista = []
    for asignaturas_del_curso in range(int(cantidad)):
        number +=1
        asignaturas_del_curso = input("favor, insertar su asignatura del curso, una por vez: ")
        print("la asignatura", number,"es: ",asignaturas_del_curso)
        lista.append(asignaturas_del_curso)
    print("las asignaturas son : ", lista)

def ejecutable_9():
    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    notas = []

    print("Notas y asignaturas")
    print("Las asignaturas de este semestre son:", asignaturas)

    notas.append(float(input("Favor, insertar su nota de Matemáticas: ")))
    notas.append(float(input("Favor, insertar su nota de Física: ")))
    notas.append(float(input("Favor, insertar su nota de Química: ")))
    notas.append(float(input("Favor, insertar su nota de Historia: ")))
    notas.append(float(input("Favor, insertar su nota de Lengua: ")))

    print("")
    print("")

    print("Para Matemáticas tuviste una nota de:", notas[0])
    print("Para Física tuviste una nota de:", notas[1])
    print("Para Química tuviste una nota de:", notas[2])
    print("Para Historia tuviste una nota de:", notas[3])
    print("Para Lengua tuviste una nota de:", notas[4])


def ejecutable_10():
    cantidad = input("favor, insertar la cantidad de números ganadores de la lotería primitiva :  ")
    number = 0
    lista = []
    for numeros_ganadores in range(int(cantidad)):
        number += 1
        numeros_ganadores = input("favor, insertar los números ganadores de la lotería primitiva (una por vez) : ")
        print("los números ganadores de la lotería ", number, "es: ", int(numeros_ganadores))
        lista.append(int(numeros_ganadores))

    print("lista :", lista)
    print("lista ordenada: ", sorted(lista))



print("cual ejercicio quieres ejecutar?")
ejecutable = input("ejercicio [1] [2] [3] [4] [5] [6] [7] [8] [9] [10]:  ")
if ejecutable == "1":
    ejecutable_1()
elif ejecutable == "2":
    ejecutable_2()
elif ejecutable == "3":
    ejecutable_3()
elif ejecutable == "4":
    ejecutable_4()
elif ejecutable == "5":
    ejecutable_5()
elif ejecutable == "6":
    ejecutable_6()
elif ejecutable == "7":
    ejecutable_7()
elif ejecutable == "8":
    ejecutable_8()
elif ejecutable == "9":
    ejecutable_9()
elif ejecutable == "10":
    ejecutable_10()
else:
    print("dato no existe")
