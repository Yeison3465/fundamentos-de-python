ingr =(int(input("ingrese la cantidad de numero que quiere ingresar: ")))
while ingr <0:
    print("ERROR NUMERO 3, ingrese numero mayor que 0")
    ingr=(int(input("ingrese de nuevo aqui el numero: ")))
i = 1
par = 0
prompar = 0
impar = 0 
promimpar = 0
pos = 0
prompos = 0
neg = 0
promneg = 0
suma = 0

while i <= ingr: 
    num = (int(input("ingrese el numero" + str(i) + " : ")))
    if (num % 2 == 0):
        par = par + 1
        prompar=prompar + num
       
       


    else:
        impar = impar + 1
        promimpar = promimpar + num

    if num >= 0:
        pos = pos + 1
        prompos = prompos + num
    else:
        neg = neg + 1
        promneg = promneg + num
    suma = suma + num
  

    i = i + 1
print("la cantidad de numeros pares es " , par )
print("la cantidad de numeros impares es ", impar)
print("la cantidad de numeros positivos es ", pos)
print("la cantidad de numeros negativos es ", neg)
print("la sumatoria de todos los numeros es" , suma)
if par >0:
    prompar=(prompar)/par
    print("el promedio de los nuemeros pares es:",prompar)
else:
    print("no hay promedio")
if impar >0:
    promimpar=(promimpar)/impar
    print("el promedio de los nuemeros impares es:",prompar)
else: 
    print("no hay nada que calcular")
if prompos >0:
    prompos=(prompos)/prompos
    print("el promedio de los nuemeros positivos es:",prompos)
else:
    print("no hay nada que calcular ")
if promneg >0:  
    promneg=(promneg)/promneg
    print("el promedio de los nuemeros negativos es:",promneg)
else:
    print("no hay nada que calcular ")
prom= suma / ingr
print("el promedio de todos los numeros es : " , prom)