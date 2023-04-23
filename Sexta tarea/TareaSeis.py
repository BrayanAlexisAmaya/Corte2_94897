# Cree tres clases heredadas de la clase "Ciudadano", basadas en tres profesiones,
# que incluyan mínimo 2 campos propios cada una.
# Cree por lo menos un método único para cada clase heredada, que tenga relación
# con cada una de las profesiones seleccionadas.
# En una de las tres clases heredadas, sobrecargue un método.
try:
    import math as m
    class Ciudadano:
        def __init__(self):
            self.__CC = None
            self.__Name = None
            self.__Edad = None
            self.__Profesion = None
# Setters
        def setCC(self,CC: int):
            self.__CC = CC
        def setName(self,Name: str):
            self.__Name = Name
        def setEdad(self,Edad: int):
            self.__Edad = Edad
        def setProfesion(self,Profesion: str):
            self.__Profesion = Profesion
# Getters
        def gerCC(self):
            return self.__CC
        def getName(self):
            return self.__Name
        def getEdad(self):
            return self.__Edad
        def getProfesion(self):
            return self.__Profesion
# Metodo sobrecarga
        def Hablar(self):
            print(f"Hola, soy {self.__Name}")

    class Escritor(Ciudadano):
        def __init__(self):
            super().__init__()
            self.__CantBooks = None
            self.__Genero = None
# Setters
        def setCantBooks(self,CantBooks: int):
            self.__CantBooks = CantBooks
        def setGenero(self,Genero: str):
            self.__Genero = Genero
# Getters
        def getCantBooks(self):
            return self.__CantBooks
        def getGenero(self):
            return self.__Genero
# Metodos Propios
        def Escribir(self):
            Tema = input("¿De que tema quieres que te escriba?: ")
            Paginas = int(input("¿Cuantas paginas quieres que tenga el libro?: "))
            Flan = []
            print("¿En que fecha quieres que salga el libro?")
            Flan.append(int(input("Dia: ")))
            Flan.append(int(input("mes: ")))
            Flan.append(int(input("año: ")))
            print("\n")
            print(f"Okey, voy a empezar a escribir sobre {Tema}, hare lo posible para que tenga\n"+\
                  f"{Paginas} paginas y entregarte el resultado el dia {Flan[0]}/{Flan[1]-1}/{Flan[2]}\n"+\
                  f"para que tengas un mes para organizar la distribucion\n")
#Metodo sobrecarga
        def Hablar(self):
            print(f"Hola soy {self.getName()} y escribo sobre {self.__Genero}")

    class Programador(Ciudadano):
        def __init__(self):
            super().__init__()
            self.__LDP = None
            self.__Entorno = None
# Setters
        def setLDP(self,LDP: str):
            self.__LDP = LDP
        def setEntorno(self,Entorno: str):
            self.__Entorno = Entorno
# Getters
        def getLDP(self):
            return self.__Entorno
        def getGenero(self):
            return self.__Entorno
# Metodos Propios
        def Programar(self):
            print(f"En un momento te dare la imformacion sobre la libreria math")
            print(help(m))
#Metodo sobrecarga
        def Hablar(self):
            print(f"Hola soy {self.getName()} y programo en {self.__LDP}")

    class Dibujante(Ciudadano):
        def __init__(self):
            super().__init__()
            self.__Estilo = None
            self.__CantDibujos = None
# Setters
        def setEstilo(self,Estilo: str):
            self.__Estilo = Estilo
        def setCantDibujos(self,CantDibujos: str):
            self.__CantDibujos = CantDibujos
# Getters
        def getEstilo(self):
            return self.__Estilo
        def getCantDibujos(self):
            return self.__CantDibujos
# Metodos Propios
        def Dibujar(self):
            Tema = input("¿sobre que quieres que dibuje?: ")
            Tono = input("¿Que tono deseas que tenga el dibujo?: ")
            print(f"Okey, voy a empezar a dibujar sobre {Tema}, hare lo posible para crear un ambiente con " + \
                  f"un tono {Tono}")
# Metodo sobrecarga
        def Hablar(self):
            print(f"Hola soy {self.getName()} y mi estilo es {self.__Estilo}")


# creando personas
    def Personas():
        Cant = int(input("¿Cuantas personas quiere crear?: "))
        print("Las profesiones son: Programador, Escritor y dibujante\n")
        Ciudadanos = []
        for i in range(Cant):
            Profesion = input(f"Ingrese la profesion de la persona {i+1}: ").lower()
            Name = input("Ingrese el nombre: ")
            Edad = int(input("Ingrese la edad: "))
            CC = int(input("Ingrese el numero de identificacion: "))
            if Profesion == "escritor":
                CantBooks = int(input("¿Cuantos libros ha escrito?: "))
                Genero = input("¿Sobre que genero escribe?: ")
                print("\n")
                Persona = Crear(Profesion,Name,Edad,CC,CantBooks,Genero)
                Ciudadanos.append(Persona)
            elif Profesion == "programador":
                LDP = input("¿Cual es su lenguaje de programacion principal?: ")
                Entorno = input("¿En que entorno programa?: ")
                print("\n")
                Persona = Crear(Profesion,Name,Edad,CC,LDP,Entorno)
                Ciudadanos.append(Persona)
            elif Profesion == "dibujante":
                Estilo = input("¿Cual es su estilo de dibujo principal?: ")
                CantDibujos = int(input("¿Cuantos dibujos a realizado?: "))
                print("\n")
                Persona = Crear(Profesion,Name,Edad,CC,Estilo,CantDibujos)
                Ciudadanos.append(Persona)
            else:
                Persona = Crear(Profesion,Name,Edad,CC,None,None)
                print("\n")
                Ciudadanos.append(Persona)

        return Ciudadanos


# creando personas
    def Crear(Profesion, Name, Edad, CC, Esp1, Esp2):
        if Profesion == "escritor":
            Persona = Escritor()
            Persona.setProfesion(Profesion)
            Persona.setName(Name)
            Persona.setEdad(Edad)
            Persona.setCC(CC)
            Persona.setCantBooks(Esp1)
            Persona.setGenero(Esp2)

        elif Profesion == "programador":
            Persona = Programador()
            Persona.setProfesion(Profesion)
            Persona.setName(Name)
            Persona.setEdad(Edad)
            Persona.setCC(CC)
            Persona.setLDP(Esp1)
            Persona.setEntorno(Esp2)

        elif Profesion == "dibujante":
            Persona = Dibujante()
            Persona.setProfesion(Profesion)
            Persona.setName(Name)
            Persona.setEdad(Edad)
            Persona.setCC(CC)
            Persona.setEstilo(Esp1)
            Persona.setCantDibujos(Esp2)

        else:
            Persona = Ciudadano()
            Persona.setProfesion(Profesion)
            Persona.setName(Name)
            Persona.setEdad(Edad)
            Persona.setCC(CC)

        return Persona

# Usando metodos propios
    def MetodosP(Ciudadanos):
        Usar = input("¿Desea usar el metodo de algun personaje?: ").lower()
        print("\n")
        while "si" in Usar:
            for i in range(len(Ciudadanos)):
                print(f"{i+1}. {Ciudadanos[i].getName()},{Ciudadanos[i].getProfesion()}")
            Id = int(input("Ingrese el numero de la persona seleccionada: "))

            if Ciudadanos[Id-1].getProfesion() == "escritor":
                Ciudadanos[Id-1].Escribir()
                print("\n")

            elif Ciudadanos[Id-1].getProfesion() == "programador":
                Ciudadanos[Id-1].Programar()
                print("\n")

            elif Ciudadanos[Id-1].getProfesion() == "dibujante":
                Ciudadanos[Id-1].Dibujar()
                print("\n")

            else:
                Ciudadanos[Id-1].Hablar()
                print("\n")
            Usar = input("¿Desea usar el metodo del personaje?: ").lower()


    def MetodosS(Ciudadanos):
        Usar = input("¿Desea usar el metodo sobrecargado de algun personaje? Si/No:  ").lower()
        print("\n")
        while "si" in Usar:
            for i in range(len(Ciudadanos)):
                print(f"{i + 1}. {Ciudadanos[i].getName()},{Ciudadanos[i].getProfesion()}")
            Id = int(input("Ingrese el numero de la persona seleccionada: "))
            Ciudadanos[Id-1].Hablar()
            print("\n")
            Usar = input("¿Desea usar el metodo sobrecargado de algun personaje?: ").lower()

# Creando app
    def app():
        Ciudadanos = Personas()
        MetodosP(Ciudadanos)
        MetodosS(Ciudadanos)

    if __name__ == "__main__":
        app()

except Exception as e:
    print(e)