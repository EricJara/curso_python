#Caso concesionaria de autos con clases, objetos y métodos
#Clase Auto
class Auto:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.estado = True

    def venderAuto(self):
        if self.estado:
            self.estado = False
            print("")
            print(f"El auto de marca {self.marca} y modelo {self.modelo} ha sido vendido.")
        else:
            print("")
            print(f"El auto de marca {self.marca} y modelo {self.modelo} no esta disponible.")

    def recargaStock(self):
        if not self.estado:
            self.estado = True
            print("")
            print(f"El auto de marca {self.marca} y modelo {self.modelo} ya esta disponible.")

    def disponibilidad(self):
        return self.estado

#Clase Cliente
class Cliente:
    def __init__(self, nom, ape):
        self.nombre = nom
        self.apellido = ape
        self.ccom = []

    def buy_car(self, auto):
        if auto.disponibilidad():
            auto.venderAuto()
            self.ccom.append(auto)
        else:
            print(f"El auto de marca {auto.marca} y modelo {auto.modelo} no esta disponible.")

    def dispCarro(self, auto):
        dispo = "disponible" if auto.disponibilidad() else "no disponible"
        print(f"El coche de marca {auto.modelo} y modelo {auto.modelo} esta {dispo} y cuesta {auto.precio}")


#Clase Concesionario
class Concesionario:
    def __init__(self,):
        self.inventario = []
        self.clientes = []
    
    def agregarCarro(self, auto):
        self.inventario.append(auto)
        print(f"El auto de marca {auto.marca} y modelo {auto.modelo} ha sido agregado al inventario.")

    def registrarCliente(self, clie):
        self.clientes.append(clie)
        print(f"El cliente {clie.nombre} ha sido registrado satisfactoriamente.")

    def mostrarCarroDisponible(self):
        print("============== Los autos disponibles: ==============")
        for auto in self.inventario:
            if auto.disponibilidad():
                print(f"{auto.marca} - {auto.modelo} por {auto.precio}")


#Crear instancias de autos
car1 = Auto("Toyota", "Corolla", "$11,000")
car2 = Auto("Ford", "Territory", "$23,000")
car3 = Auto("Chevrolet", "Spin", "$19,000")

#Crear instancias de clientes
clie1 = Cliente("Eric","Jara")

# Crear instancia de concesionaria, registrar autos y clientes
cons = Concesionario()
cons.agregarCarro(car1)
cons.agregarCarro(car2)
cons.agregarCarro(car3)
cons.registrarCliente(clie1)

#Mostrar autos disponibles
cons.mostrarCarroDisponible()

#Consulta el estado del carro 1
clie1.dispCarro(car1)

#Cliente compra el carro 1
clie1.buy_car(car1)

#Mostrar autos disponibles
cons.mostrarCarroDisponible()

#Cliente intenta comprar un coche que no esta disponible
clie1.buy_car(car1)