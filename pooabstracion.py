from abc import ABC ,abstractclassmethod

class Personaje(ABC):
    @abstractclassmethod
    def __init__(self,nombre):
        self.nombre = nombre
        self.nivel = 0
        self.invetario =[]
        self.vida = 100
    
    @abstractclassmethod

    def atacar(self, objetivo):
        pass

    @abstractclassmethod

    def estatuspersonaje(self):
        print(f"Nombre: {self.nombre} \n Nivel: {self.nivel}")
    
    def subirLevel(self):
        self.nivel +=1
    
    def invetariover(self):
        print(f"El inventario de {self.nombre}")
        for objetos in self.invetario:
            print(objetos)
    
class Mago(Personaje):
    def __init__(self,nombre):
        super().__init__(nombre)
        self.vida = 150
        self.inteligenia = 95
        self.invetario = ["pocion de mana","libro de echizos"]
    
    def estatuspersonaje(self):
        print(f" es de la clase mago")
        super().estatuspersonaje()
    
    def atacar(self,objetivo):
        objetivo.vida -= self.inteligenia*0.6
        print(f"Vida actual del objetivo es: {objetivo.vida}")

class Guerrero(Personaje):
    def __init__(self,nombre):
        super().__init__(nombre)
        self.vida = 200
        self.fuerza = 75
        self.invetario  = ["espada","pocion de vida"]
    
    def estatuspersonaje(self):
        print(f"es de la clase guerrero")
        super().estatuspersonaje()
    
    def atacar(self, objetivo):
        objetivo.vida -= self.fuerza*0.8
        print(f"el objetivo se quedado con {objetivo.vida}")
    
guerrero= Guerrero("herakens")
mago= Mago("naruto")

guerrero.estatuspersonaje()
mago.estatuspersonaje()

guerrero.invetariover()
mago.invetariover()

mago.atacar(guerrero)
guerrero.atacar(mago)
    







