#Caso bibliotecla con clases, objetos y métodos
#Clase Libro
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor =  autor
        self.dispo = True

    def prestar(self):
        if self.dispo:
            self.dispo = False
            print("")
            print(f"El libro {self.titulo} ha sido prestado.")
        else:
            print("")
            print(f"El libro {self.titulo} no está disponible.")
    
    def retornarLibro(self):
        self.dispo = True
        print("")
        print(f"El libro {self.titulo} ha sido devuelto.")

#Clase Usuario
class Usuario:
    def __init__(self, nomb, user_id):
        self.nombre = nomb
        self.id = user_id
        self.coleccionLibro = []
    
    def prestarLibro(self, libro):
        if libro.dispo:
            libro.prestar()
            self.coleccionLibro.append(libro)
        else:
            print(f"El libro {libro.titulo} no esta disponible.")

    def retornarLibro(self, libro):
        if libro in self.coleccionLibro:
            libro.retornarLibro()
            self.coleccionLibro.remove(libro)
        else:
            print("")
            print(f"El libro {libro.titulo}, no se encuentra entre los libros prestado.")

#Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libro = []
        self.usuar = []

    def agrgarLibro(self, lib):
        self.libro.append(lib)
        print(f"El libro {lib.titulo} ha sido agregado.")
    
    def registrarUsuario(self, usu):
        self.usuar.append(usu)
        print(f"El usuario {usu.nombre} ha sido registrado.")

    def mostrarLibro(self):
        print("")
        print("============== Los libros disponibles: ==============")
        for Libro in self.libro:
            if Libro.dispo:
                print(f"El {Libro.titulo} del autor {Libro.autor}.")
        print("=====================================================")

#Crear los libros - objetos
libro1 = Libro("El Principito","Antoine de Saint-Exupéry")
libro2 = Libro("1984", "George Orwell")

#Crear los usuarios - objetos
user1 = Usuario("Eric","001")

#Crear Biblioteca - objetos
print("================== CREAR BIBLIOTECA ==================")
bibli = Biblioteca()
bibli.agrgarLibro(libro1)
bibli.agrgarLibro(libro2)
bibli.registrarUsuario(user1)
print("======================================================")


#Crear métodos
#Mostrar Libro
bibli.mostrarLibro()

#Realizar un prestamo de libro
user1.prestarLibro(libro1)

#Mostrar librosç
bibli.mostrarLibro()

#Devolver libro
user1.retornarLibro(libro1)

#Mostrar libros
bibli.mostrarLibro()