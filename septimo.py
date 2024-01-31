
"""suma=0
n=(int(input("ingrese la cantidad que desea registrar: ")))
while n<= 0 :
    n=(int(input("ingrese la cantidad que desea registrar")))
i=1
n2=(int(input("ingrese la cantidad de notas: ")))
p=1
while i <=n:
    nb=(input("ingrese el nonbre: "))
    while p <=n2:
        op=(float(input("nota " + str(p) + ": ")))
    p=p+1
i= i +1
suma=suma+op
por=suma/n2
print(por)"""



# comproba un dato tipo string tiene numero

"""while(True):
    name=(input("ingrese el nombre: "))
    if name.isalpha():
        break
    else:
        print("esto tiene numeros")"""
# probabilidades de respuesta 
"""import random 
igr=(input("ingrese su y te digo que piendo de ti : "))
num= random.randint(1,10)
print(num)
if (num < 3):
    print("pienso que eres un buena persona")
elif (num == 4 ):
    print("pienso que eres tonto")
elif(num == 6):
    print("piensa mas en ti")
elif(num > 7):
    print("eres gracioso")"""
# hacer una suma 
"""while(True):
    try:
        total= 0
        restados=(input("ingrese los numeros(por espacios): "))
        restados= restados.split()
        for num in restados:
            if num.isnumeric():
                total += float(num)
            else:
                raise ValueError ("el valor no es un numero")
    except ValueError:
        print("los datos son incorrectos")
    else:
        print(f"el valor de la suma es {total}")
        break
    finally:
        print("el programa a terminado")"""

"""import pygame
pygame.mixer.init()
pygame.mixer.music.load('sample.mp3')
pygame.mixer.music.play()"""

"""tupla = [("computadora",2,"procesador"),("i",0,"w"),("t",1,"lp")]

for x in range(1,len(tupla)-1):
    print(tupla[x],end=" ")
    for y in x:
        print(tupla[y],end=" ")"""

tupla = [("computadora",2,"procesador"),("i",0,"w"),("t",1,"lp")]

for x in range(1,len(tupla)-1):
    print(tupla[x])
    tupla1 = list(tupla[x])
    print(tupla1)
i = 1
for t in tupla1:
    print(f" componete numero {i} y el item es {t}")
    i = i + 1
