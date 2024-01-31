# la tuplas 
mitupla=("teclado","impresora","pantalla","procesador")
print(mitupla)
print(f"la longitud de la tupla es: {len(mitupla)}")

for componete in mitupla:
    print(f"los componetes son: {mitupla.index(componete)} es {componete}")

# indexando tuplas
mitupla=("teclado","impresora","pantalla","procesador")
print(mitupla)
primero=mitupla[0]
ultimo=[-1]
subtupla=mitupla[1:3]
print(f"el primer {mitupla}")
print(f"el ultimo {ultimo}")
print(subtupla)

# modificar una tupla
mitupla=("teclado","impresora","pantalla","procesador")
milista=list(mitupla)
print(milista)
milista.append("cpu")
print(milista)
mitupla=tuple(milista)
print(mitupla)

# empaquetar una tupla 
mitupla=("teclado","impresora","pantalla","procesador")
partes=("ram")
partes1=("TARGE.madre")
nuevatupla=(partes,partes1)
print(nuevatupla)
# desenpaquetar
(par1,par2,par3,part4)=mitupla
print(f"primera parte:{par1}.segunda parte {par2}")
(par1,*variaspart)=mitupla
print(par1)
print(variaspart)

mitupla2=mitupla + nuevatupla
(par1,*todos,ulti)=mitupla2
print(par1)
print(todos)
print(ulti)