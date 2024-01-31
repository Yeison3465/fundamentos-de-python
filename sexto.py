numeros=[1, 2, 3, 4, 5, 6]
print(numeros)
primerapos= numeros[0]

longitud= len(numeros)
print(f"el primer digito es : {primerapos} \n la longitud de la lista es: {longitud}")
for i in numeros:
    print(i)
    i=i+1
    print(i)
print(numeros)
listas=["anime","de","one","pieces"]
print(listas)
ultipos= listas[-1]
print(ultipos)
penul= listas[-2]
print(penul)
# tambien se puede contar de derecha a izquierda en negativo

sublista= listas[1:4]
print(sublista)
sublista= listas[:4]
print(sublista)
sublista= listas [2:]
print(sublista)
sublista = listas [-2:-3]

# comprovar si esta en una lista
listas1 = ["el", "one", "pieces" , "existe"]
palabra= "pieces"
palabra2="f"
if palabra in listas1:
    print("la palabra pertenece")

if palabra2 not in listas1:
    print("la palabra no esta en lista")

# modificar 
lenguaje = ["C","java", "python", "javascript"]
print(lenguaje)
lenguaje[2]="serpiente"
print(lenguaje)
lenguaje[0]=lenguaje[0] + "++"
print(lenguaje)

lenguaje[2:4] = ["perro", "araña"]
print(lenguaje)

lenguaje[1:3] =["computador","portatil", "directa"]
print(lenguaje)

# metodos en python X)))
# metodo insert - este metodo se usa para modificar una lista sin afectarla un elemento dentro de ella
lenguajes = ["C","python","Java","Java scrip", "Ruby","Rust"]
print(lenguajes)

lenguajes.insert(-1,"C++")
print(lenguajes)
lenguajes.insert(4,"serpiente")
print(lenguajes)

# append el siguente metodo se usa para poner un elemento al final de la lista automaticamenete 
lenguajes.append("Computador")
print(lenguajes)
lenguajes.append("mouse")
print(lenguajes)

# extend - este metod se usa combinar 2 listas en una sola

partes= ["computador","mouse","CPU"]
print(partes)
lenguajes.extend(partes)
print(lenguajes)
print(partes)

# asi como se puede añadir se pueden eliminar 
# pop, este metodo sirve para eliminar elemetos de la listas 
animals=["perro", "gatos" , "buho", "lechusa" , "tigre" , "leon"]
print(animals)
animals.pop()
print(animals)
# al no poner un numero en la lista se elimina el ultimo numero

animals.pop(2)
print(animals)

# remove - este metodo se usa para eliminar elemento de una lista por texto

animals.remove("lechusa")
print(animals)

# metodo del se usa para eliminar pero sin comandos
del animals[1]
print(animals)

# metodo index este metodo se usa para remplazar el valor por numero de la posicion

indice= animals.index("tigre")
print(indice)
