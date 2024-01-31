from pydoc import classname


class Persona:
    def __init__(self,nombre,edad,N_doc):
        self.nombre = nombre
        self.edad = edad
        self.N_doc = N_doc
    def presentacion(self):
        print(f"!hola me llamo {self.nombre} y tengo {self.edad} años ")
class trabajor(Persona):
    def __init__(self, nombre, edad, N_doc,sueldo,cargo, empresa):
        super().__init__(nombre, edad, N_doc) # esta se esta heredando las parte de clase persona es decir se completando con la nueva clase que vas a crear
        self.sueldo = sueldo
        self.cargo = cargo
        self.empresa = empresa
    def calcular(self):
        return 12 * self.sueldo + 2000
class estudiante(Persona):
    def __init__(self, nombre, edad, N_doc,universidad,curso,asignatura):
        super().__init__(nombre, edad, N_doc)
        self.universidad = universidad
        self.curso = curso
        self.asignatura = asignatura
    def descrip(self):
        print(f"!!!! hola mi nombres es {self.nombre} tengo {self.edad} de edad \n estudio en la universidad {self.universidad}")

    
Trabajador=trabajor("juan",45,"651861991",1000000,"coordinador","eletricaribe")
Trabajador.presentacion()
print(Trabajador.N_doc)
print(Trabajador.calcular())
Estudiante=estudiante("Maria",19,"61981965","unversidad del choco","ING.industrial","matematicas")
Estudiante.descrip()

