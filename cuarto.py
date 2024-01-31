#cuarto 
# definicon de las funciones



def saludar():
    print("hola como estas")


# funciones con argumentos 
def saludardos(nombre):
    print("hola" + nombre + "que tal")

saludardos("tommy")
saludardos("yeison")


# funciones con retornos
def suma(a, c):
    resultado = a + c
    return resultado

valor = suma(20,3)
print(valor)

def sumados (a,b):
    return a + b
valor = sumados (10,5)
print(valor)

def sonidenticos(num1,num2):
    return num1 == num2 

verdad = sonidenticos(3,6) 
if(verdad):
    print("son iguales")
else:
    print("son Diferentes")
print(verdad)

verdad = sonidenticos(4,6)
print(verdad)
 

 #funciones con argumentos con valor con defecto 
def saludarPor(nombre="tommy"):
    print("hola" + nombre + "como estas")

saludarPor()
saludarPor("yeison")

# funciones  que retoman varios valores 

def sumaYResta(a, b):
    suma = a + b
    resta =a - b
    return suma , resta
    
resultado1 , resultado2 = sumaYResta (20,5) 
print("Los resultados son:\nsuma: " + str (resultado1) + "\nresta: " +  str (resultado2))




