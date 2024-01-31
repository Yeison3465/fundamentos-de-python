# funciones de de python parte 2
# esta funcion se usa cuando no se sabe el numero de parametros que la funcion va a recibir 
def maximo (*args):
    maximo = args[0]
    for numero in args[1:]:
        if maximo > numero:
            maximo = numero
    return maximo
print(maximo(1.0,45,9,87))
print(maximo(42,32,45,74))

def maximo (*arg):
    maximo = arg[0]
    for numero in arg[1:]:
        if maximo > numero:
            maximo = numero
    return maximo
print(maximo([1.0,45,9,87]))

# argumentos de palabras claves 
def rol (clase,raza,nombre):
    print(f"{nombre.upper()} es un {clase} raza{raza}")
rol(nombre="ratita",clase="blanco",raza="furro")
rol("mago","doñaclas","elfo")

# funcion kwargs
def printk(**kwargs):
    print("\n")
    print("los atributos del personaje: ")
    for clave , valor in kwargs.items():
        print(f"{clave} ----> {valor}")
printk(nombre = "jose", clase = "guerrero", raza = "humano" , mascota = "dragon" , clan = "los NOOD")


