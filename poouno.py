# progrmacion orientada a a objetos 


class pantalones:
    def __init__(self,marca,precio,talla,color):
        self.marca=marca
        self.precio=precio
        self.talla=talla
        self.color=color
        self.rebaja=False
    def descuento (self,pocer):
        self.precio=self.precio*pocer/100
        if(pocer < 100):
            self.rebaja=True
    def info(self):
        info=(f"descripcion de los pantalones:\nMarca:{self.marca}\nPrecio:{self.precio:2f}\nTalla:{self.talla}\nColor:{self.color}\n")
        if(self.rebaja):
            info+="este producto esta rebajado"
        return info

Pantolones=pantalones("nike",500000,"S","negro")
"""print(Pantolones.precio)
Pantolones.descuento(15)
print(Pantolones.precio)"""

print(Pantolones.info())