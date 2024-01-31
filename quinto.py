# introducion a las listas 
from itertools import count


numeros = [1, 2 ,3 ,4 ,5 , 6 , 7, 8]
# las listas van desde 0 hata la "LONGITUD - 1" 
print(numeros[0])
print(numeros[1])
print(numeros[2])
print(numeros[3])
print(numeros[4])
print(numeros[5])
print(len(numeros))# este se usa para ver el ultimo dijito
# este se utiliza para ver la longitud de la lista o la cantidad de elementos que tiene
tipo_texto = ["tommy","mause","perro"]
print(tipo_texto)
print(tipo_texto[2])
uni_num_txt = [1 , 3.5 ,"tommy" , True , "impresora" , "cuaderno"]
print(tipo_texto)
print(tipo_texto[0])

# lend tiene la funcion de que son la lista es larga te puede decir la longitud, pero tiene que poner "longitud - 1"

print(tipo_texto[len(tipo_texto)-1])

# ======= BUCLES: bucles for ========
for listadenumero in range(5):
    print(listadenumero)

hola = ("===========================================")
print(hola)

for listadenumero in range(3,10):
    print(listadenumero)
print("bueno hasta aqui llegamos con el bucle")

hola = ("============================================")
print(hola)

for listadenumero in range( 12 , 21 , 2): #el ultimo termino es la veces que numero que se cuenta
    print(listadenumero)
print("contamos de 2 en 2")

for listadenumero in range ( 11 , 23 , 2):
    print(listadenumero)
print("el resultado es 23 porque nose puede pasar del limite ")

# ejemplo, de imprimir solo vocales de un palabra

txt = ("elefante")
for letras in txt:
    if(letras == "a" or letras == "e"  or  letras == "i" or  letras =="o" or letras == "u"):
        print(letras)
    else:
        print("esto son consonates")

hola =("===============================================")
print(hola)
# ejemplo con interar sobre una lista

numero = [36 , 45 , 39 , 25]
for numeros1 in numero:
    print(numeros1)
    numeros1 = numeros1 + 10
    print(numeros1)
print(numeros)

for indice in range(len(numero)):
    numero[indice] += 10
print(numero)

# ============ BUCLES CON WHILE ================

letraencontrada = (False)
letra =("n")
frase =("en este momento esto buscando la letra n")
numero2 = (0)

while(not(letraencontrada)):
    if(frase[numero2] == "n"):
        letraencontrada = (True)
        print(f"ya la encontramos{letra} en la posicion{numero2}")
    else:
        numero2 +=1

# ================ SEGUNDA PARTE ================

frase =("en este momento busco la letra n")
letra1 =("n")
for caracter in frase:
    if(caracter == letra1):
        print("la hemos encontrado")
    else:
        print("no hemos encotrado nada")
    print(caracter)
# ================ BUCLES CON BREAK =============
frase =("en este momento busco la letra n")
letra1 =("n")
for caracter in frase:
    if(caracter == letra1):
        print(f"la hemos encontrado la letra{letra1} en la posicion {frase.index(caracter)}")
        print(caracter)
        break # no imprime lo de de abajo porque hay esta la funcion
    else:
        print("no hemos encotrado nada")
    print(caracter)
# ================= continue ====================
frase1 =("hola tommy")
letra2 =("m")
conta =(0)
for caracter in frase1:
    if(caracter == letra2):
        conta +=1
        print(f"letra encotrada {conta} veces ")
        continue
# ================== pass ======================
lista =[0, 10 , 20, 43]
for jose in lista:
    if(jose == 10):
        pass
    else:
        print(f"el valor de jose es {jose}")
def funcionNombre(cosa1 ,cosa2):
    pass
def funcionNombre2(cosa1,cosa2):
    pass #ponemos pass para que nos de error

# ================== else =======================
# lo que hace el else cuando ha ya completado va a aparecer el codigo else
frase1 =("todos los caracteres de una frase")
contado =(0)
for caracter in frase1:
    contado +=1
else:
    print(f"la frase contiene {contado} caracteres")
#========================================================
frase1 =("todos los caracteres de una frase")
contado =(0)
for caracter in frase1:
    contado +=1
    break
else:
    print(f"la frase contiene {contado} caracteres")

numerocorrecto = 20
def pediryComprobar(numeroAAdivinar):
    numUser = int(input("Ei, adivina el número: "))
    if(numUser == numeroAAdivinar):
        print("eres un pro has acertado")
        return True
    elif(numUser > numeroAAdivinar):
        print("un numero mas pequeño")
        return False
    elif(numUser < numeroAAdivinar):
        print("un numero mas grande")
while(True):
    if(pediryComprobar(numerocorrecto)):
        break


  
