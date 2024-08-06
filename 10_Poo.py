#Programación Orientados a Objetos mediantes clases y funciones
class Persona:
    def __init__(self, nombre, edad):
        self.nom = nombre
        self.eda = edad

    def saluda(self):
        print(f"Hola, mi nombre es {self.nom} y tengo {self.eda} años.")

persona1 = Persona("Ana", 30)
persona2 = Persona("Eric", 27)
persona1.saluda()
persona2.saluda()


#Programación Orientados a Objetos (Funcionaes propias de una clase o objeto se llaman método)
class cuentaBank:
    def __init__(self, cuenta, balance):
        self.cuenta = cuenta
        self.balance = balance
        self.is_active = True
    
    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Se ha depósitado {amount} soles. Saldo actual es {self.balance} soles.")
        else:
            print("No se puede depósitar, su cuenta se encuentra inactiva.")

    def retirar(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Se ha retirado {amount} soles. Su saldo actual es {self.balance} soles.")
            else:
                print("No cuenta con suficiente efectivo para retirar.")
        else:
            print("No se puede retirar, su cuenta se encuentra inactiva.")

    def desactiva_cuenta(self):
        self.is_active = False
        print(f"La cuenta ha sido desactivada satisfactoriamente.")

    def activar_cuenta(self):
        self.is_active = True
        print(f"La cuenta ha sido activada satisfactoriamente.")

#Para crear un objeto la momenclatura o la sintaxis debe ser Nombre = clase (parámetros)
cuenta_1 = cuentaBank("Ana", 500)
cuenta_2 = cuentaBank("Eric", 1000)

#Llamada a los métodos
cuenta_1.deposit(200)
cuenta_2.deposit(1500)

cuenta_1.desactiva_cuenta()
cuenta_1.deposit(50)
cuenta_1.activar_cuenta()
cuenta_1.deposit(50)
cuenta_2.retirar(3000)