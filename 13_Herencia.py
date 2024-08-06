#Aplicación de Herencia en las clases en el caso de concesionaria de vehiculos
#Clase Padre Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, precio):
        #Encapsulación
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.estado = True

    def vender(self):
        if self.estado:
            self.estado = False
            print(f"El vehículo de marca {self.marca}. Ha sido vendido.")
        else:
            print(f"El vehículo de marca {self.marca}. No está vendido.")

    #Abstracción
    def disponible(self):
        return self.estado

    #Abstracción
    def getPrecios(self):
        return self.precio

    def iniciarMotor(self):
        raise NotImplementedError("Este método debe ser implementado por la subClase.")
    
    def deternerMotor(self):
        raise NotImplementedError("Este método debe ser implementado por la subClase.")


#Clase auto (hijo) que hereda de la Clase Vehiculo (padre)
class Auto(Vehiculo):
    #Polimorfismo
    def iniciarMotor(self):
        if not self.estado:
            return f"El motor del auto de marca {self.marca} está en marcha."
        else:
            return f"El auto de marca {self.marca} no está disponible."
    
    #Polimorfismo
    def deternerMotor(self):
        if not self.estado:
            return f"El motor del auto de marca {self.marca} se ha detenido."
        else:
            return f"El auto de marca {self.marca} no está disponible."


#Clase bicicleta (hijo) que hereda de la Clase Vehiculo (padre)
class Bicicleta(Vehiculo):
    #Polimorfismo
    def iniciarMotor(self):
        if not self.estado:
            return f"La bicicleta de marca {self.marca} está en marcha."
        else:
            return f"La bicicleta de marca {self.marca} no está disponible."

    #Polimorfismo
    def deternerMotor(self):
        if not self.estado:
            return f"La bicicleta de marca {self.marca} se ha detenido."
        else:
            return f"La bicicleta de marca {self.marca} no está disponible."


#Clase camión (hijo) que hereda de la Clase Vehiculo (padre)
class Camion(Vehiculo):
    #Polimorfismo
    def iniciarMotor(self):
        if not self.estado:
            return f"El motor del camión de marca {self.marca} está en marcha."
        else:
            return f"El camión de marca {self.marca} no está disponible."

    #Polimorfismo
    def deternerMotor(self):
        if not self.estado:
            return f"El motor del camión de marca {self.marca} se ha detenido."
        else:
            return f"El camión de marca {self.marca} no está disponible."


#Clase Cliente
class Cliente:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apelli = apellido
        self.colecc = []
    
    def comprarVehiculo(self, vehiculo: Vehiculo):
        if vehiculo.disponible():
            vehiculo.vender()
            self.colecc.append(vehiculo)
        else:
            print(f"Vehículo de marca {vehiculo.marca}seleccionado no se encuentra disponible en estos momentos.")

    def disponibilidadVehiculo(self, vehiculo: Vehiculo):
        if vehiculo.disponible():
            dispo = "disponible"
        else:
            dispo = "no disponible"
        print(f"El vehículo de marca {vehiculo.marca} esta {dispo} y cuesta ${vehiculo.precio}.")


#Clase Concesionaria
class Concesionaria:
    def __init__(self):
        self.inventar = []
        self.clientes = []

    def agregarVehiculo(self, vehiculo: Vehiculo):
        self.inventar.append(vehiculo)
        print(f"El vehículo de marca {vehiculo.marca} y modelo {vehiculo.modelo} ha sido añadido al inventario.")

    def registrarCliente(self, cliente: Cliente):
        self.clientes.append(cliente)
        print(f"El cliente {cliente.nombre} {cliente.apelli} ha sido registrado satisfactoriamente.")

    def mostrarVehiculoDisponibles(self):
        print(f"============ Vehículos disponibles en el concesionario ============")
        for vehiculo in self.inventar:
            if vehiculo.disponible():
                print(f"{vehiculo.marca} - {vehiculo.modelo} por ${vehiculo.precio}.")
        print(f"===================================================================")


#Crear instancias
carro1 = Auto("Toyota","Corolla",11000)
bici1 = Bicicleta("Monark","MT-07",750)
camio1 = Camion("Volvo","Discovery",16000000)
print("")

cliente = Cliente("Eric","Jara")
print("")

concesionaria = Concesionaria()
concesionaria.agregarVehiculo(carro1)
concesionaria.agregarVehiculo(bici1)
concesionaria.agregarVehiculo(camio1)
print("")

#Mostrar vehículos disponibles
concesionaria.mostrarVehiculoDisponibles()
print("")

#Cliente consultar un vehículo
cliente.disponibilidadVehiculo(carro1)
print("")

#Cliente compra un vehículo
cliente.comprarVehiculo(carro1)
print("")

#Mostrar vehículos disponibles
concesionaria.mostrarVehiculoDisponibles()
print("")