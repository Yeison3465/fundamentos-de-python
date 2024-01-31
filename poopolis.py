class empleado:
    def __init__(self,nombre,sueldomesual):
        self.nombre = nombre
        self.sueldomesual = sueldomesual
    
    def calcularsueldoaño(self):
        sueldo = 12*self.sueldomesual*( 1 + 1/100 )
        print(f"el sueldo anual es de {self.nombre},empleado normal,es de {sueldo}")
    
class contable(empleado):
    def __init__(self, nombre, sueldomesual):
        super().__init__(nombre, sueldomesual)
    
    def calcularsueldoaño(self):
        sueldo = 12*self.sueldomesual*(1 + 4/100)
        print(f"el sueldo anual es de {self.nombre},contable ,es de {sueldo}")

class publicista(empleado):
    def __init__(self, nombre, sueldomesual):
        super().__init__(nombre, sueldomesual)
    
    def calcularsueldoaño(self):
        sueldo = 12*self.sueldomesual*(1 + 1/100)
        print(f"el sueldo anual de {self.nombre},publicista,es de {sueldo}")

class becario(empleado):
    def __init__(self, nombre, sueldomesual):
        super().__init__(nombre, sueldomesual)
    
    def calcularsueldoaño(self):
        sueldo = 12*self.sueldomesual
        print(f"el sueldo anual de {self.nombre},becario ,es de {sueldo}")

Empleados=[
    empleado("tomas",2000),
    contable("Maria",30005),
    publicista("Jose",300000),
    becario("monjamen",50000),
] 

for emple in Empleados:
    emple.calcularsueldoaño()
    