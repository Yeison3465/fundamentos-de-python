# execiopnes de python

frutas=["0 ---> platano","1 ---> manzana","2 ---> pomelo","3 ---> mango"]
for x in frutas:
    print(x)
try:
    print(frutas)
    listafru=(int(input("ingrese el numero de su fruta: ")))
    print(f"tu fruta favorita es {frutas[listafru]}") 
except IndexError: # este se usa para la posicion de las lista
    print("este numero esta fueras de lista de frutas")
except ValueError:
    print("ingrese un numero entero ")

#para no estar poninedo muchas execiones simplemete pon 'Exeption'