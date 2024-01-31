class Circulos:
    def __init__(self,radio):
        self.radio = radio
        self.pi = 3.14

    def perimetro(self):
        return 2*self.pi*self.radio
    
    def area(self):
        return self.pi*self.radio**2
    
    def setradio(self,nuevovalor):
        if(type(nuevovalor) == int or type(nuevovalor) == float):
            if nuevovalor >=0:
                self.radio = nuevovalor
            else:
                print("El radio no puede ser negativo")
        else:
            print("radio tiene que ser numero positivo")
    
c1= Circulos(2.5)
print(c1.perimetro())
print(c1.area)
print(f"el valor del numero PI es {c1.pi}")
c1.setradio(31)
c1.setradio(-31)
c1.setradio("!hola¡ Muy buenas")