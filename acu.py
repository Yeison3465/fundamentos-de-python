from os import system



system("cls")
import time
import sys
from os import system

gastos=[]
nuevos=[]
registro={}
print("=========== BIENVENIDO ==========")
print("")
print("registrese primero, para ver las opciones ")
print("")
user = input("Ingrese el nombre de usuario: ")
if user in registro:
    print("Usuario ya registrado.")
else:
    pasword = input("Ingrese la contraseña: ")
    registro[user]=pasword
    print("su userio y contraseña es: ")
    for producto,precio in registro.items():
        print("usuario:",producto,",contraseña:",precio)
    print("\n")
    print("redirigiendo....")
    time.sleep(2)
    system("cls")



while(True):
    print("========= INICIO DE SESION ==========")
    print("")
    beginning = input("Ingrese el usuario: ")
    beginning2 = input("Ingrese la contraseña: ")
    if beginning in registro and beginning2 in registro[beginning]:
        system("cls")
        print("redirigiendo...")
        time.sleep(1)
        break
    print("parece que los datos que ingresastes son incorrectos puedes salirte presionando 0 o precionando 1 para volver a intentar")
    exit=(input("ingrese aqui: "))
    if(exit == "0"):
        break
    elif(exit == "1"):
        print("")
    else:
        print("este dato no se encuentra o son incorrectos")

g = 0
system("cls")
while(True):
    print("======= BIENVENIDO AL MENU DE OPCIONES =========")
    menu=("\n 1. agregar gastos \n 2. ver productos registrados \n 3. ver gastos \n 4. añadir producto \n 5. calculadora básica \n 6. salir")
    print(menu)
    vamos=(input("cual funcion quieres ejecutar: "))
    if(vamos == "agregar gastos"  or vamos == "1"):
        while(True):
            try:
                canti=(int(input("ingrese la cantidad de gasto de quiere registrar: ")))
                while canti<=0:
                  canti=(int(input("error,este dato no es incorrecto: ")))
                break
            except ValueError:
              print("error, el dato ingresado no es un numero")
        for a in range(canti):
            name=(input("ingrese el nombre del gasto: "))
            while(True):
                try:
                    gastos2=(int(input("ingrese el valor del gasto: ")))
                    break
                except ValueError:
                  print("error, esto no es un numero...")
            gastos.append({'Nombre':name,'valor':gastos2})
        i=1
        for e in gastos:
            print("\n gastos",i)
            for nombre,valor in e.items():
              print(nombre," : ",valor)
            i=i+1
    elif(vamos == "ver productos registrados" or vamos == "2"):
        system("cls")
        print(" ========= LISTA DE PRODUCTOS ========== ")
        print("")
        lapiz={
            "producto":"lapiz",
            "precio": 800,
            "cantidad": 90  
        }
        lapiceros={
            "producto":"lapiceros",
            "precio": 1000,
            "cantidad": 90 

        }
        borradores={
            "producto":"borrador",
            "precio": 500,
            "cantidad": 100 
        }
        portami={
            "producto":"portaminas",
            "precio": 2000,
            "cantidad": 30 
        }
        minasfinas={
            "producto":"paquete de minas fina",
            "precio": 3000,
            "cantidad": 40 
        }
        minasgruesas={
            "producto":"paquete de minas gruesas",
            "precio": 5000,
            "cantidad": 35
        }
        sacapuntas={
            "producto":"sacapuntas",
            "precio": 500,
            "cantidad": 90 
        }
        corrector={
            "producto":"corrector de lapiceros",
            "precio": 2000,
            "cantidad": 50 
        }
        colores={
            "producto":"paquete de colores grande ",
            "precio": 12000,
            "cantidad": 22
        }
        colores1={
            "producto":"paquete de colores mediano ",
            "precio": 7000,
            "cantidad": 29
        }
        colores2={
            "producto":"paquete de colores pequeño ",
            "precio": 4000,
            "cantidad": 21
        }
        macpuanch={
            "producto":" paquete de marcadores punta ancha",
            "precio": 20000,
            "cantidad": 15 
        }
        macpuanch1={
            "producto":"paquete de marcadores punta fina",
            "precio": 50000,
            "cantidad": 25
        }
        plastilina={
            "producto":"platilina",
            "precio": 5000,
            "cantidad": 65 
        }
        cartulina={
            "producto":"cartulina",
            "precio": 2000,
            "cantidad": 35
        }
        cartulina2={
            "producto":"octavo de cartulina",
            "precio": 800,
            "cantidad": 50
        }
        cartulina3={
            "producto":"media cartulina",
            "precio": 1500,
            "cantidad": 37
        }
        pega={
            "producto":"goma en barra grande",
            "precio": 3000,
            "cantidad": 20
        }
        pega1={
            "producto":"goma en barra pequeña",
            "precio": 2000,
            "cantidad": 30
        }
        gota={
            "producto":"gota magica",
            "precio": 700,
            "cantidad": 34 
        }
        pega2={
            "producto":"goma liquida  grande ",
            "precio": 5000,
            "cantidad": 20
        }
        pega={
            "producto":"goma liquida pequeña",
            "precio": 2500,
            "cantidad": 23 
        }
        cilico={
            "producto":"cilicona grande",
            "precio": 5000,
            "cantidad": 30
        }
        cilico2={
            "producto":"cilicona pequeña",
            "precio": 2000,
            "cantidad": 32
        }
        cuaderno={
            "producto":"cuaderno de 50 hojas",
            "precio": 1500,
            "cantidad": 35
        }
        cuaderno2={
            "producto":"cuaderno de 100 hojas",
            "precio": 2500,
            "cantidad": 34
        }
        libreta={
            "producto":"libreta grande de 5 materias",
            "precio": 10000,
            "cantidad": 29
        }
        libreta1={
            "producto":"libreta grande de 7 materias",
            "precio": 15000,
            "cantidad": 47
        }
        fomis={
            "producto":"fomi",
            "precio": 800,
            "cantidad": 19
        }
        fomiesc={
            "producto":"fomi escarchado",
            "precio": 1200,
            "cantidad": 45
        }







        while(True):
        
            product=("\n 1. lapiz \n 2. lapiceros \n 3. borradores \n 4. porta minas \n 5. paquetes de minas \n 6. saca puntas \n 7. corrector  de lapiceros \n 8. paquete de colores \n 9. paquetes de marcadores \n 10. plastilina \n 11. cartulinas \n 12. gomas \n 13. gota magica \n 14. cilicona \n 15. fomis \n 16. cuadernos \n 17. libretas \n 18. ver nuevos productos registrados \n 19. salir")
            print(product)
            ingresar=(input("ingrese la opcion que quiere ejecutar: "))
            print("")
            if(ingresar == "1" or ingresar == "lapiz"):
                for producto,precio in lapiz.items():
                    print(producto," : ",precio)
                print("\n")
            elif(ingresar == "lapiceros" or ingresar == "2"):
                for producto,precio in lapiceros.items():
                    print(producto," : " ,precio)
            elif(ingresar == "borradores" or ingresar == "3"):
                for producto, precio in borradores.items():
                    print(producto," : ",precio)
            elif(ingresar == "porta minas" or ingresar == "4"):
                for producto, precio in portami.items():
                    print(producto," : ",precio)
            elif(ingresar == "paquete de minas" or ingresar == "5"):
                print("========== TIPOS DE PAQUETES ==========")
                for producto, precio in minasfinas.items():
                    print(producto," : ",precio)
                print("")
                for producto1,precio1, in minasgruesas.items():
                    print(producto1," : ", precio1)
            elif(ingresar == "saca puntas" or ingresar == "6"):
                for producto, precio in sacapuntas.items():
                    print(producto," : ",precio)
            elif(ingresar == "corrector de lapiceros" or ingresar == "7"):
                for producto, precio in corrector.items():
                    print(producto," : ",precio)
            elif(ingresar == "paquete de colores" or ingresar == "8"):
                print("========= TIPOS DE PAQUETES DE COLORES ==========")
                for producto, precio in colores.items():
                    print(producto," : ",precio)
                print("")
                for producto1,precio1 in colores1.items():
                    print(producto1," : ",precio1)
                print("")
                for producto2,precio2 in colores2.items():
                    print(producto2,precio2)
                print("")
            elif(ingresar == "paquete de marcadores" or ingresar == "9"):
                print("========= TIPOS DE PAQUETES DE MARCADORES ===========")
                print("")
                for producto, precio in macpuanch.items():
                    print(producto," : ",precio)
                print("")
                for producto1,precio1 in macpuanch1.items():
                    print(producto1,precio1)
            elif(ingresar == "plastilina" or ingresar == "10"):
                for producto, precio in plastilina.items():
                    print(producto," : ",precio)
            elif(ingresar == "cartulina" or ingresar == "11"):
                print("========== TIPOS DE CARTULINA ==========")
                print("")
                for producto, precio in cartulina.items():
                    print(producto," : ",precio)
                print("")
                for producto1,precio1 in cartulina2.items():
                    print(producto1," : ",precio1)
                print("")
                for producto2,precio2 in cartulina3.items():
                    print(producto2,": ",precio2)
            elif(ingresar == "goma" or ingresar == "12" or ingresar == "pega"):
                print("========= TIPOS DE GOMAS O PEGAS ======== ")
                print("")
                for producto, precio in pega.items():
                    print(producto," : ",precio)
                print("")
                for producto1, precio1 in pega1.items():
                    print(producto1," : ",precio1)
                print("")
                for producto2, precio2 in pega2.items():
                    print(producto2," : ",precio2)
            elif(ingresar == "gota magica" or ingresar == "13"):
                for producto,precio in gota.items():
                    print(producto," : " ,precio)
                print("")
            elif(ingresar == "cilicona" or ingresar == "14"):
                print("========= TIPOS DE CILICONA =========")
                print("")
                for producto,precio in cilico.items():
                    print(producto," : " ,precio)
                print("")
                for producto1,precio1 in cilico2.items():
                    print(producto1," : ", precio1)
            elif(ingresar == "fomi" or ingresar == "15"):
                print("======== TIPOS DE FOMIS ========")
                print("")
                for producto,precio in fomis.items():
                    print(producto," : " ,precio)
                print("")
                for producto1,precio1 in fomiesc.items():
                    print(producto1," : ", precio1)
            elif(ingresar == "cuadernos" or ingresar == "16"):
                print("======= TIPOS DE CUADERNOS =========")
                print("")
                for producto, precio in cuaderno.items():
                    print(producto," : ",precio)
                print("")
                for producto1, precio1 in cuaderno2.items():
                    print(producto1," : ",precio1)
            elif(ingresar == "libretas" or ingresar == "17"):
                print("======= TIPOS DE LIBRETAS =========")
                print("")
                for producto, precio in libreta.items():
                    print(producto," : ",precio)
                print("")
                for producto1, precio1 in libreta1.items():
                    print(producto1," : ",precio1)
            elif(ingresar == "18" or ingresar == "nuevos productos registrados"):
                l=1
                for g in nuevos:
                  print("\n nuevos productos registrados",l,": ")
                  for pro,despues in g.items():
                    print(pro,despues)
                  l=l+1

            elif(ingresar == "19" or ingresar == "salir"):
                system("cls")
                time.sleep(1)
                print("limpiando pantalla")
                time.sleep(2)
                print("verificando...")
                time.sleep(3)
                print("rediregiendo....")
                time.sleep(3.1)
                system("cls")
                break
            else:
                print("esta opcion nose encuetra")
    elif(vamos == "3" or vamos == "ver gastos"):
        system("cls")
        print("")
        
        i=1
        for e in gastos:
            print("\n gastos",i)
            for nombre,valor in e.items():
                print(nombre," : ",valor)
            i= i + 1
        
    elif(vamos == "4" or vamos == "agregar nuevos productos"):
        system("cls")
        while(True):
            try:
                cantidad=(int(input("Ingrese la cantidad que desea registrar: ")))
                while cantidad<=0:
                    cantidad=(int(input("error, tipo de dato incorrecto: ")))
                break
            except ValueError:
                print("ERROR, el dato no es numerico")
        for a in range(cantidad):
            name1=(input("ingrese el nombre del producto: "))
            while(True):
                try:
                    preci=(int(input("Ingrese el precio: ")))
                    while preci<=0:
                        preci=(int(input("Error, este dato no es congruente, ingrese de nuevo")))
                    break
                except ValueError:
                    print("Error, este dato no es numerico")
            while(True):
                try:
                    canti1=(int(input("ingrese la cantidad: ")))
                    while canti1 <=0:
                        canti1=(int(input("Error, este dato no es congruente ingrese de nuevo: ")))
                    break
                except ValueError:
                    print("Error, este dato no es numerico")
            nuevos.append({'producto':name1,'precio':preci,'cantidad':canti1})
        l=1
        for g in nuevos:
            print("\n nuevos productos registrados",l,": ")
            for pro,despues in g.items():
                print(pro,despues)
            l=l+1
        system("cls")
    elif(vamos == "5" or vamos == "calculadora basica"):
        system("cls")
        while(True):
            print("============ CALCULADORA ===========")
            print("")
            print("\n 1. suma \n 2. resta \n 3. muliplicacion \n 4. division \n 5. salir")
            print("")
            u=(input("ingrese la opciones que se desea ejecutar: "))
            if( u == "1" or u == "suma"):
                system("cls")
                while(True):
                    try:
                        x=(int(input("ingrese la cantidad de numeros que desea sumar: ")))
                        while x <=0:
                            print("ERROR 427, el numero digitado no es valido para esta opcion, le sugerimos que ingrese un numero mayor a 0")
                            print("")
                            x=(int(input("ingrese de nuevo la cantidad que desea sumar: ")))
                            print("")
                        break
                    except ValueError:
                        print("ERROR 431, el dato ingresado no es un numero")
                p=1
                suma=0
                while p <= x:
                    while(True):
                        try:
                            num=(float(input("Ingrese el numero " + str (p) + ": ")))
                            break
                        except ValueError:
                            print("ERROR 431, el dato ingresado no es un numero")
                    suma=suma+num
                    print("el resultado de la suma es ", suma)
                    p= p + 1
            elif( u == "2" or u == "resta"):
                system("cls")
                while(True):
                    try:
                        num=(float(input("ingrese el primer dijito: ")))
                        print("")
                        print("-")
                        num2=(float(input("ingrese el segundo dijito: ")))
                        print("")
                        break
                    except ValueError:
                        print("ERROR 431, el dato ingresado no es un numero")
                resta=num-num2
                print("el resultado de la resta es ",resta)
            elif( u == "3" or u == "multiplicacion"):
                system("cls")
                while(True):
                    try:
                        num=(float(input("ingrese el primer dijito: ")))
                        print("")
                        print("*")
                        num2=(float(input("ingrese el segundo dijito: ")))
                        print("")
                        break
                    except ValueError:
                        print("ERROR 431, el dato ingresado no es un numero")
                multi=num*num2
                print("el resultado de la resta es ",multi)
            elif( u == "4" or u == "division"):
                system("cls")
                while(True):
                    try:
                        num=(float(input("ingrese el primer dijito: ")))
                        print("")
                        print("/")
                        num2=(float(input("ingrese el segundo dijito: ")))
                        print("")
                        break
                    except ValueError:
                        print("ERROR 431, el dato ingresado no es un numero")
                while(True):
                    try:
                        resta=num/num2
                    except ZeroDivisionError:
                        print("ERROR, esto no se puede dividir")
                        time.sleep(5)
                        system("cls")
                        break
                    else:
                        print("el resultado es",resta)
                        break
            elif(u == "5" or u == "salir"):
                system("cls")
                time.sleep(1)
                print("limpiando pantalla")
                time.sleep(2)
                print("verificando...")
                time.sleep(3)
                print("rediregiendo....")
                time.sleep(3.1)
                system("cls")
                break
            else:
                print("esta funcion nose encuentra")
                time.sleep(4)
                system("cls")



                
    
        




                
    

        
    elif(vamos == "salir" or vamos == "6"):
        break
    else:
        print("esta funcion nose encuentra")


