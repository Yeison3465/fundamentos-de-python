# Entrada de datos del usurio . Identificacion del tipo de datos.

edad = input("escribe tu edad por favor: ")
tipo_de_datos = type(edad)
nombre = input("escribe tu nombre: ")
nombre_2 =type(nombre)
print(edad)
print(tipo_de_datos)
print(nombre)
print(nombre_2)


# Booleanos, IF
verdadero = True
falso = False

if(verdadero == True):
    print("soy verdadero")

if(falso == True):
    print("son iguales")

if(falso == False):
    print("el es falso")

    # Operaciones de compraracion, elif, else
    edad = input("dime tu edad, por favor: ")
    edad = int(edad)
    if(edad >= 18):
        print("Eres mayor de edad, puedes pasar")
    elif(edad <0):
        print("los datos incogruentes")
    else:
        print("eres menor de edad, no pasa de la puerta")

  # Operadores logicos and, or, not
edad = input("dime tu edad , eseguida:")
edad = int(edad)

if(type(edad) == int):
    if(edad > 120 or edad < 0):
        print("esto no es creible tonto")
    elif(edad > 18 and edad < 45):
        print ("puedes entra aqui")
    elif(edad < 18 and edad > 15):
        print("todovia eres un niño , vete a jugar")
    else:
        print("no sea cumplido nada")
else:
    print("oye la edad que escribes debe ser un numero mayo que cero")

if(not(edad <= 18)):
    print("puedes pasar aqui")



