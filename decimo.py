from os import system
system("cls")
# formato tipo string
numeros="123456789"
total=0

for x in numeros:
    total=total+ int(x)
else:
    print("el resulado de la suma es " + str(total) )

# format string 
canti=(int(input("ingrese la cantidad de computadores que desea comprar: ")))
preci=(float(input("ingrese el precio: ")))
total=(f"usted a comprado la cantidad de computadores {canti},con el precio {preci}  y es total de su compra es {canti * preci}")
print(total)

# metodos de string 
mail=("yeison@gmail.com")

posi=mail.index("@")
print(posi)

posi=mail.find("@")
print(posi)
posi= mail.find("*")
print(posi)
try:
    posi= mail.index("*")
except IndexError:
    print("no se ha encotrado este articulo")


# el metodo index devuelve un error y el find un -1 
# metodo count te dice la cantidad de veces que se repite un string
"""apar=("manzana")
apari=apar.count("a")
print(f"la cantidad que se repite la letra {apari}")"""

#otros metodos para String
#metodo string , este metodo sirve para serpara los objetos de una lista 
"""comprar=("perro caliente, hamburguesa, picada, salsa, patacon")
listadecom= comprar.split(", ")
print(listadecom)
print(f"la cantidad de elementos de la lista es {len(listadecom)}") # esta funcion de sirve para contar las cantidad objetos que hay o letras
cambiocom=comprar.replace(", ", " - ") # esta funcion sirve para cambiar... los signos con que se separan 
print(cambiocom)
comprar="/".join(comprar)
print(comprar)"""

# metodos .... (yeison del futuro me canse de escribirr los tipos de metodos asi que aqui va los metodos que restan (como te va en el futuro ))
"""x=("hola mundo")
print(x.upper())"""
# este metodo se usa para el tipo string se ponga en mayuscula 
"""print(x.capitalize())"""
# sirve para poner la primera letra en mayusculas 

