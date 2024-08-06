def greet(name, lastname="apellido no disponible"):
    print("Hola", name, lastname)

greet("Eric", "Jara")
greet("Edu")
greet(lastname="Pupuche",name="Dora")

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    return a/b

def calculadora():
    while True:
        print("")
        print("::::::::: Selecione una operación :::::::::")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        option = int(input("Ingrese su opción [1,2,3,4,5]: "))

        if option == 5:
            print("Saliste de la calculadora.")
            print("")
            break
        elif option in [1,2,3,4]:
            num1 = float(input("Ingrese 1er número: "))
            num2 = float(input("Ingrese 2do número: "))

            if option == 1:
                print("La suma es: ", suma(num1,num2))
            elif option == 2:
                print("La resta es: ", resta(num1,num2))
            elif option == 3:
                print("La multiplicación es: ", multiplicar(num1,num2))
            elif option == 4:
                print("La dividir es: ", dividir(num1,num2))
        else:
            print("Opción no válida, intente nuevamente.")
            continue

calculadora()