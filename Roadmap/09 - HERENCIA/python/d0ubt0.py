class Empleado:
    def __init__(self,identificador: str,nombre:str) -> None:
        self.identificador = identificador
        self.nombre= nombre
        self.empleados  = []

    def hello(self):
        print(f'Mi nombre es {self.nombre} y soy un empleado')

    def add(self,empleado):
        self.empleados.append(empleado)

    def show(self):
        for i in self.empleados:
            print(i.nombre)

class Programador(Empleado):
    def __init__(self, identificador: str, nombre: str, lenguaje:str) -> None:
        super().__init__(identificador, nombre)
        self.lenguaje = lenguaje

    def hello(self):
        print(f'Mi nombre es {self.nombre} y soy un programador de {self.lenguaje}')

    def add(self,empleado):
        print(f'No puedes tener a {empleado} a tu cargo')

    def show(self):
        print('No soy jefe de nadie :(')

class Gerente(Empleado):
    def __init__(self, identificador: str, nombre: str) -> None:
        super().__init__(identificador, nombre)

    def hello(self):
        print(f'Mi nombre es {self.nombre} y soy un gerente')

gerente = Gerente('00','Sebastian')
programador1 = Programador('01','Carlos','Python')
programador2 = Programador('02','David','Java')
        
gerente.hello()  
gerente.add(programador1)
gerente.add(programador2)      
gerente.show()

programador1.hello()        
programador1.show()

programador2.hello()        
programador2.show()