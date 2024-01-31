import code
from os import system
import sys
import time
system("cls")

codemate="4548"
codecaste="4325"
codegeo="4789"
codeingles="4650"
codesoci="4001"
# ================= #
tareamate={}
recibirmate={}
# ================= #
tareageo={}
recibirgeo={}
# ================= #
tareaing={}
recibiring={}
# ================= #
tareacaste={}
recibircaste={}
# ================= #
tareanatu={}
recibirnatu={}
# ================= #
tareasoci={}
recibirsoci={}
# ================= #
nuevataredemaye=[]
registrodeprofes={}
registrodeestu={}
notasingles={}
notasmate={}
notasnatu={}
notasgeo={}
notascaste={}
notassoci={}
soloprofe="454780"
apro=0
desa=0
pro=0
suma=0
n="no hay notas"
# menu de inicio de sesion 
while(True):
    print("========== bienvenido a la plataforma pinguino ==========")
    print("\n 1. registrarse \n 2. inicio de sesion \n 3. salir ")
    op=(input("ingrese la opcion que desea ejecutar: "))
    # registro 
    if(op == "1" or op == "resgitrarse"):
        system("cls")
        while(True):
            print("¿quien es usted? \n 1. estudiante \n 2. profesor \n 3.salir")
            op2=(input("reponda aqui: "))
            if(op2 == "1" or op2 == "estudiante"):
                system("cls")
                user=(input("ingrese nombre de usuario: "))
                if (user in registrodeestu):
                    print("este usuario se encuntra registrado por favor ingrese otro")
                    
                    system("cls")
                else:
                    contraseña = input("Ingrese una contraseña:")
                    registrodeestu[user]=contraseña
                    system("cls")
                    time.sleep(2)
                    print("espere un momento")
                    time.sleep(3)
                    print("\n registrado con exito \n redirigiendo....")
                    
                    system("cls")
                    break
            elif(op2 == "2" or op2 == "profesor"):
                system("cls")
                while(True):
                    print("ingrese el codigo de acceso, si desea salir escriba 'salir' o solo escribiendo el numero 0  ")
                    x=(input("ingrese aqui: "))
                    if(x == soloprofe):
                        system("cls")
                        user=(input("ingrese nombre de usuario: "))
                        if (user in registrodeprofes):
                            print("este usuario se encuntra registrado por favor ingrese otro")
                    
                            system("cls")
                        else:
                            contraseña = input("Ingrese una contraseña:")
                            registrodeprofes[user]=contraseña
                            print("\n registrado con exito \n redirigiendo....")
                    
                            system("cls")
                            break
                    elif(x == "salir" or x == "0"):
                        system("cls")
                        time.sleep(2)
                        print("espere un momento...")
                        time.sleep(3)               
                        break
                    else:
                        print("esta funcion nose encuentra")
                    
                        system("cls")
            elif(op2 == "3" or op2 == "salir"):
                system("cls")
                break
            else:
                print("esta opcion no existe")
    # inicio de sesion 
    elif(op == "2" or op == "inicio de sesion"):
        system("cls")
        while(True):
            print("¿quien es usted? \n 1. estudiante \n 2. profesor \n 3. salir")
            op2=(input("responda aqui: "))
            if (op2 == "1"):
                user=(input("ingrese el usuario: "))
                contraseña=(input("ingrese la contraseña: "))
                if ((user in registrodeestu) and (contraseña in registrodeestu[user])) or user==1 or contraseña==1:
                    system("cls")
                    time.sleep(2)
                    print("iniciando sesion.")
                    time.sleep(2)
                    print("iniciando sesion..")
                    time.sleep(2)
                    print("iniciando sesion...")
                    print(f"bienvenido estudiante {user} disfrute la opciones que le ofrece la plataforma pinguino")
                    time.sleep(2)
                    print("espere uno segundos")
                    time.sleep(2)
                    system("cls")
                    while(True):
                        print("============ MENU DE ESTUDIANTE =============")
                        print("\n 1. ver notas \n 2. ver nueva tareas \n 3. enviar tareas \n 4. salir")
                        estu=(input("ingrese opcion que desea ejecutar: "))
                        if(estu == "1" or estu == "ver notas"):
                            system("cls")
                            print("notas de \n 1. matematicas \n 2. castellano \n 3. ingles \n 4. naturales \n 5. sociales \n 6. castellano \n 7. geometria \n 8. salir")
                            xx=(input("cual quieres revisar"))
                            if(xx == "1" or xx == "matematicas"):
                                
                               while(True):
                                            a=0
                                            while True:
                                                for ww in range(n):
                                                    print("")
                                                    print("\n resgistro de notas",a+1,": ")
                                                    print("Nombre:",notasmate[a][0])
                                                    print("Promedio:",notasmate[a][1])
                                                    print("Notas:",*notasmate[a][2])
                                                    a=a+1
                                                break
                                            print("")
                                            u=(input("responde aqui: "))
                                            if (u == "x" or u == "X"):
                                                system("cls")
                                                time.sleep(2)
                                                print("espere un momento")
                                                system("cls")

                                                break
                                            elif(u == "n"or "N"):
                                                pass
                                            else:
                                                print("esta funcion nose encuentra")
                            elif(xx == "2" or xx == "castellano"):
                                while(True):
                                            a=0
                                            while True:
                                                for ww in range(n):
                                                    print("")
                                                    print("\n resgistro de notas",a+1,": ")
                                                    print("Nombre:",notascaste[a][0])
                                                    print("Promedio:",notascaste[a][1])
                                                    print("Notas:",*notascaste[a][2])
                                                    a=a+1
                                                break
                                            print("")
                                            u=(input("responde aqui: "))
                                            if (u == "x" or u == "X"):
                                                break
                                            elif(u == "n"or "N"):
                                                pass
                                            else:
                                                print("esta funcion nose encuentra") 
                            elif(xx == "3" or xx == "ingles"):
                                while(True):
                                            a=0
                                            while True:
                                                for ww in range(n):
                                                    print("")
                                                    print("\n resgistro de notas",a+1,": ")
                                                    print("Nombre:",notasingles[a][0])
                                                    print("Promedio:",notasingles[a][1])
                                                    print("Notas:",*notasingles[a][2])
                                                    a=a+1
                                                break
                                            print("")
                                            u=(input("responde aqui: "))
                                            if (u == "x" or u == "X"):
                                                break
                                            elif(u == "n"or "N"):
                                                pass
                                            else:
                                                print("esta funcion nose encuentra")
                            elif(xx == "4" or xx == "naturales"):
                                while(True):
                                            a=0
                                            while True:
                                                for ww in range(n):
                                                    print("")
                                                    print("\n resgistro de notas",a+1,": ")
                                                    print("Nombre:",notasnatu[a][0])
                                                    print("Promedio:",notasnatu[a][1])
                                                    print("Notas:",*notasnatu[a][2])
                                                    a=a+1
                                                break
                                            print("")
                                            u=(input("responde aqui: "))
                                            if (u == "x" or u == "X"):
                                                system("cls")
                                                time.sleep(2)
                                                print("espere un momento")
                                                system("cls")
                                                break
                                            elif(u == "n"or "N"):
                                                pass
                                            else:
                                                print("esta funcion nose encuentra")
                            elif(xx == "5" or xx == "sociales"):
                                while(True):
                                            a=0
                                            while True:
                                                for ww in range(n):
                                                    print("")
                                                    print("\n resgistro de notas",a+1,": ")
                                                    print("Nombre:",notassoci[a][0])
                                                    print("Promedio:",notassoci[a][1])
                                                    print("Notas:",*notassoci[a][2])
                                                    a=a+1
                                                break
                                            print("")
                                            u=(input("responde aqui: "))
                                            if (u == "x" or u == "X"):
                                                system("cls")
                                                time.sleep(2)
                                                print("espere un momento")
                                                system("cls")
                                                break
                                            elif(u == "n"or "N"):
                                                pass
                                            else:
                                                print("esta funcion nose encuentra")
                            elif(xx == "6" or xx == "castellano"):
                                while(True):
                                            a=0
                                            while True:
                                                for ww in range(n):
                                                    print("")
                                                    print("\n resgistro de notas",a+1,": ")
                                                    print("Nombre:",notascaste[a][0])
                                                    print("Promedio:",notascaste[a][1])
                                                    print("Notas:",*notascaste[a][2])
                                                    a=a+1
                                                break
                                            print("")
                                            u=(input("responde aqui: "))
                                            if (u == "x" or u == "X"):
                                                system("cls")
                                                time.sleep(2)
                                                print("espere un momento")
                                                system("cls")
                                                break
                                            elif(u == "n"or "N"):
                                                pass
                                            else:
                                                print("esta funcion nose encuentra")
                            elif(xx == "7" or xx == "geometria"):
                                while(True):
                                            a=0
                                            while True:
                                                for ww in range(n):
                                                    print("")
                                                    print("\n resgistro de notas",a+1,": ")
                                                    print("Nombre:",notasgeo[a][0])
                                                    print("Promedio:",notasgeo[a][1])
                                                    print("Notas:",*notasgeo[a][2])
                                                    a=a+1
                                                break
                                            print("")
                                            u=(input("responde aqui: "))
                                            if (u == "x" or u == "X"):
                                                system("cls")
                                                time.sleep(2)
                                                print("espere un momento")
                                                system("cls")
                                                break
                                            elif(u == "n"or "N"):
                                                pass
                                            else:
                                                print("esta funcion nose encuentra")
                            elif(xx == "8" or xx == "salir"):
                                system("cls")
                                break


                        elif(estu == "2" or estu == "ver nueva tareas"):
                            system("cls")
                            while(True):
                                print(f"========= BIENVENIDO ESTUDIANTE {user}===========")
                                print("Asignaturas \n 1. matematicas \n 2. geometria \n 3. ingles  \n 4. castellano \n 5. naturales \n 6. sociales \n 7. salir  ")
                                xx=(input("cual quieres ver: "))
                                if(xx == "1" or xx == "matematicas"):
                                    while(True):
                                        for clave,valor in tareamate.items():
                                            print(clave,valor)
                                        print("\n")
                                        op4=(input("ingrese 'x' para volver al menu: "))
                                        if(op4 == "x" or op4 == "X"):
                                            break
                                elif(xx == "2" or xx == "geometria"):
                                    while(True):
                                        for clave,valor in tareageo.items():
                                            print(clave,valor)
                                        print("\n")
                                        op4=(input("ingrese 'x' para volver al menu: "))
                                        if(op4 == "x" or op4 == "X"):
                                            break
                                elif(xx == "3" or xx == "ingles"):
                                    while(True):
                                        for clave,valor in tareaing.items():
                                            print(clave,valor)
                                        print("\n")
                                        op4=(input("ingrese 'x' para volver al menu: "))
                                        if(op4 == "x" or op4 == "X"):
                                            break
                                elif(xx == "4" or xx == "castellano"):
                                    while(True):
                                        for clave,valor in tareacaste.items():
                                            print(clave,valor)
                                        print("\n")
                                        op4=(input("ingrese 'x' para volver al menu: "))
                                        if(op4 == "x" or op4 == "X"):
                                            break
                                elif(xx == "5" or xx == "naturales"):
                                    while(True):
                                        for clave,valor in tareanatu.items():
                                            print(clave,valor)
                                        print("\n")
                                        op4=(input("ingrese 'x' para volver al menu: "))
                                        if(op4 == "x" or op4 == "X"):
                                            break
                                elif(xx == "6" or xx == "sociales"):
                                    for clave,valor in tareasoci.items():
                                        print(clave,valor)
                                    print("\n")
                                elif(xx == "7" or xx == "salir"):
                                    break
                                else:
                                    print("esta funcion nose encuentra")



                        elif(estu == "3" or estu == "enviar tareas"):
                            system("cls")
                            while(True):
                                print("Asignaturas \n 1. matematicas \n 2. geometria \n 3. ingles  \n 4. castellano \n 5. naturales \n 6. sociales \n 7. salir  ")
                                xx=(input("ingrese aqui: "))
                                if(xx == "1" or xx == "matematica"):
                                    system("cls")
                                    while(True):
                                        print("ingrese la tarea")
                                        o=(input(""))
                                        o1=(input("seguro que quieres enviar"))
                                        if(o1 == "si"):
                                            name=(input("ingrese su nombre: "))
                                            grade=(input("ingrese el grado"))
                                            recibirmate.update({'Nombre':name,'grado':grade,'tarea':o})
                                            print(recibirmate)
                                            print("tarea enviada")
                                            break
                                        elif(o1 == "no"):
                                            pass
                                elif(xx == "2" or xx == "geometria"):
                                    system("cls")
                                    while(True):
                                        print("ingrese la tarea")
                                        o=(input(""))
                                        o1=(input("seguro que quieres enviar"))
                                        if(o1 == "si"):
                                            name=(input("ingrese su nombre: "))
                                            grade=(input("ingrese el grado"))
                                            recibirgeo.update({'Nombre':name,'grado':grade,'tarea':o})
                                            print(recibirgeo)
                                            print("tarea enviada")
                                            break
                                        elif(o1 == "no"):
                                            pass
                                elif(xx == "3" or xx == "ingles"):
                                    system("cls")
                                    while(True):
                                        print("ingrese la tarea")
                                        o=(input(""))
                                        o1=(input("seguro que quieres enviar"))
                                        if(o1 == "si"):
                                            name=(input("ingrese su nombre: "))
                                            grade=(input("ingrese el grado"))
                                            recibiring.update({'Nombre':name,'grado':grade,'tarea':o})
                                            print(recibiring)
                                            print("tarea enviada")
                                            break
                                        elif(o1 == "no"):
                                            pass
                                elif(xx == "4" or xx == "castellano"):
                                    system("cls")
                                    while(True):
                                        print("ingrese la tarea")
                                        o=(input(""))
                                        o1=(input("seguro que quieres enviar"))
                                        if(o1 == "si"):
                                            name=(input("ingrese su nombre: "))
                                            grade=(input("ingrese el grado"))
                                            recibircaste.update({'Nombre':name,'grado':grade,'tarea':o})
                                            print(recibircaste)
                                            print("tarea enviada")
                                            break
                                        elif(o1 == "no"):
                                            pass
                                elif(xx == "5" or xx == "naturales"):
                                    system("cls")
                                    while(True):
                                        print("ingrese la tarea")
                                        o=(input(""))
                                        o1=(input("seguro que quieres enviar"))
                                        if(o1 == "si"):
                                            name=(input("ingrese su nombre: "))
                                            grade=(input("ingrese el grado"))
                                            recibirnatu.update({'Nombre':name,'grado':grade,'tarea':o})
                                            print(recibirgeo)
                                            print("tarea enviada")
                                            break
                                        elif(o1 == "no"):
                                            pass
                                elif(xx == "6" or xx == "sociales"):
                                    system("cls")
                                    while(True):
                                        print("ingrese la tarea")
                                        o=(input(""))
                                        o1=(input("seguro que quieres enviar"))
                                        if(o1 == "si"):
                                            name=(input("ingrese su nombre: "))
                                            grade=(input("ingrese el grado"))
                                            recibirsoci.update({'Nombre':name,'grado':grade,'tarea':o})
                                            print(recibirsoci)
                                            print("tarea enviada")
                                            break
                                        elif(o1 == "no"):
                                            pass
                                elif(xx == "7" or xx == "salir"):
                                    break
                                else:
                                    print("no se encutra esta opcion ")

                        elif(estu == "4" or estu == "salir"):
                            print("saliendo del menu")
                            system("cls")
                            break
                        else:
                            print("esta opcion nose encuentra")
                else:
                    print("usuarios incorrectos, ingrese de nuevo")
                    time.sleep(4.1)

            elif (op2 == "2" or op == "profesor"):
                user=(input("ingrese el usuario: "))
                contraseña=(input("ingrese la contraseña: "))
                if ((user in registrodeprofes) and (contraseña in registrodeprofes[user])) or user==1 or contraseña==1:
                    system("cls")
                    print(f" bienvenido profesor@ {user} disfrute de las opciones que le ofrecemos")
                    
                    print("espere unos segundos")
                    
                    system("cls")
                    while(True):
                        print("======= menu de profesores =======")
                        print("usted es profes@r de \n 1. matematicas \n 2. geometria \n 3. ingles  \n 4. castellano \n 5. naturales \n 6. sociales \n 7. salir  ")
                        x=(input("reponda aqui: "))
                        if(x == "1" or x == "matematicas"):
                            system("cls")
                            op3=(input("ingrese el codigo de acceso: "))
                            if(op3 == codemate):
                                pass
                                while(True):
                                    print("======== menu de opciones ========")
                                    print("\n 1. ingresar notas \n 2. ver notas resgristradas \n 3. ingresar nueva tarea \n 4. recibiento de tarea \n 5. salir ")
                                    x2=(input("ingrese la opcion que desea ejecutar: "))
                                    if (x2 == "1" or x2 == "ingresar notas"):
                                        while(True):
                                            try:
                                                n=(int(input("ingrese la cantidad de que desea registrar: ")))
                                                while n < 0 :
                                                    print("este numero no es correcto")
                                                    n=(int(input("ingrese la cantidad que desea registrar: ")))
                                                break
                                                
                                            except ValueError:
                                                print("esto no es un numero")
                                        while(True):
                                            try:
                                                n2=(int(input("ingrese la cantidad de notas que desea registrar: ")))
                                                while n2 < 0:
                                                    print("esto no es valido")
                                                    n2=(int(input("ingrese la cantidad de notas que desea registrar: ")))
                                                break
                                            except ValueError:
                                                print("esto no es un numero")
                                        a=0
                                        for notas in range(n):
                                            name=(input("ingrese el nombre completo del estudiante: "))
                                            i=1
                                            a=a+1
                                            suma=0
                                            notasw=[]
                                            for notes1 in range(n2):
                                                while(True):
                                                    try:
                                                        notes=(float(input("ingrese la nota " + str(i) + ": ")))
                                                        pro=0
                                                        suma=suma + notes
                                                        pro=suma/n2
                                                        round(pro,2)
                                                        notasw.append(notes)
                                                        while notes <= 0 or notes > 5:
                                                            print("esto no es valido")
                                                            notes=(float(input("ingrese la nota " + str(i) + ": ")))
                                                        break
                                                    except ValueError:
                                                        print("esto no es un numero")
                                                i = i + 1
                                            notasmate[a-1]=(name,round(pro,2),notasw)
                                    elif(x2 == "2" or x2 == "ver registro de notas"):
                                        while(True):
                                            
                                            while True:
                                                for ww in range(n):
                                                    print("")
                                                    print("\n resgistro de notas",a+1,": ")
                                                    print("Nombre:",notasmate[a][0])
                                                    print("Promedio:",notasmate[a][1])
                                                    print("Notas:",*notasmate[a][2])
                                                    a=a+1
                                                break
                                            print("")
                        
                                            u=(input("responde aqui: "))
                                            if (u == "x" or u == "X"):
                                                break
                                            elif(u == "n"or "N"):
                                                pass
                                            else:
                                                print("esta funcion nose encuentra")
                                    elif(x2 == "3" or x2 == "ingresar nueva tarea"):
                                        print("ingrese la tarea")
                                        tarea=(input(""))
                                        nuevataredemaye.append({'tarea': tarea})
                                    elif(x2 == "4" or x2 == "rebimiento de tarea"):
                                        while(True):
                                            for clave1,valor1 in recibirmate.items():
                                                print(clave1,valor1)
                                            print("\n")
                                            oo=(input("ingrese 'x' para salir "))
                                            if(oo == "X" or oo == "x"):
                                                break
                                            else:
                                                print("escribe bien el dijito")
                                    elif(x2 == "5" or x2 == "salir"):
                                        break
                                    else:
                                        print("esta opcion nose encuentra")
                        elif(x == "2" or x == "geometria"):
                                pass
                                while(True):
                                    print("======== menu de opciones ========")
                                    print("\n 1. ingresar notas \n 2. ver notas resgristradas \n 3. ingresar nueva tarea \n 4. recibiento de tarea \n 5. salir ")
                                    x2=(input("ingrese la opcion que desea ejecutar: "))
                                    if (x2 == "1" or x2 == "ingresar notas"):
                                        while(True):
                                            try:
                                                n=(int(input("ingrese la cantidad de estudiante que desea registrar: ")))
                                                while n < 0 :
                                                    print("este numero no es correcto")
                                                    n=(int(input("ingrese la cantidad que desea registrar: ")))
                                                break
                                                
                                            except ValueError:
                                                print("esto no es un numero")
                                        while(True):
                                            try:
                                                n2=(int(input("ingrese la cantidad de notas que desea registrar: ")))
                                                while n2 < 0:
                                                    print("esto no es valido")
                                                    n2=(int(input("ingrese la cantidad de notas que desea registrar: ")))
                                                break
                                            except ValueError:
                                                print("esto no es un numero")
                                        a=0
                                        for notas in range(n):
                                            name=(input("ingrese el nombre completo del estudiante: "))
                                            i=1
                                            a=a+1
                                            suma=0
                                            notasw=[]
                                            for notes1 in range(n2):
                                                while(True):
                                                    try:
                                                        notes=(float(input("ingrese la nota " + str(i) + ": ")))
                                                        pro=0
                                                        suma=suma + notes
                                                        pro=suma/n2
                                                        round(pro,2)
                                                        notasw.append(notes)
                                                        while notes <= 0 or notes > 5:
                                                            print("esto no es valido")
                                                            notes=(float(input("ingrese la nota " + str(i) + ": ")))
                                                        break
                                                    except ValueError:
                                                        print("esto no es un numero")
                                                i = i + 1
                                            notasgeo[a-1]=(name,round(pro,2),notasw)
                                    elif(x2 == "2" or x2 == "ver registro de notas"):
                                        while(True):
                                            a=0
                                            while True:
                                                for ww in range(n):
                                                    print("")
                                                    print("\n resgistro de notas",a+1,": ")
                                                    print("Nombre:",notasgeo[a][0])
                                                    print("Promedio:",notasgeo[a][1])
                                                    print("Notas:",*notasgeo[a][2])
                                                    a=a+1
                                                break
                                            print("")
                                            u=(input("responde aqui: "))
                                            if (u == "x" or u == "X"):
                                                break
                                            elif(u == "n"or "N"):
                                                pass
                                            else:
                                                print("esta funcion nose encuentra")
                                    elif(x2 == "3" or x2 == "ingresar nueva tarea"):
                                        print("ingrese la tarea")
                                        tarea=(input(""))
                                        nuevataredemaye.append({'tarea': tarea})
                                    elif(x2 == "4" or x2 == "rebimiento de tarea"):
                                        while(True):
                                            for clave1,valor1 in recibirgeo.items():
                                                print(clave1,valor1)
                                            print("\n")
                                            oo=(input("ingrese 'x' para salir "))
                                            if(oo == "X" or oo == "x"):
                                                break
                                            else:
                                                print("escribe bien el dijito")
                                    
                                    elif(x2 == "5" or x2 == "salir"):
                                        break
                                    else:
                                        print("esta opcion nose encuentra")    
                        elif(x == "3" or x == "ingles"):
                            system("cls")
                            pass
                            while(True):
                                    print("======== menu de opciones ========")
                                    print("\n 1. ingresar notas \n 2. ver notas resgristradas \n 3. ingresar nueva tarea \n 4. recibiento de tarea \n 5. salir ")
                                    x2=(input("ingrese la opcion que desea ejecutar: "))
                                    if (x2 == "1" or x2 == "ingresar notas"):
                                        while(True):
                                            try:
                                                n=(int(input("ingrese la cantidad de que desea registrar: ")))
                                                while n < 0 :
                                                    print("este numero no es correcto")
                                                    n=(int(input("ingrese la cantidad que desea registrar: ")))
                                                break
                                                
                                            except ValueError:
                                                print("esto no es un numero")
                                        while(True):
                                            try:
                                                n2=(int(input("ingrese la cantidad de notas que desea registrar: ")))
                                                while n2 < 0:
                                                    print("esto no es valido")
                                                    n2=(int(input("ingrese la cantidad de notas que desea registrar: ")))
                                                break
                                            except ValueError:
                                                print("esto no es un numero")
                                        a=0
                                        for notas in range(n):
                                            name=(input("ingrese el nombre completo del estudiante: "))
                                            i=1
                                            a=a+1
                                            suma=0
                                            notasw=[]
                                            for notes1 in range(n2):
                                                while(True):
                                                    try:
                                                        notes=(float(input("ingrese la nota " + str(i) + ": ")))
                                                        pro=0
                                                        suma=suma + notes
                                                        pro=suma/n2
                                                        round(pro,2)
                                                        notasw.append(notes)
                                                        while notes <= 0 or notes > 5:
                                                            print("esto no es valido")
                                                            notes=(float(input("ingrese la nota " + str(i) + ": ")))
                                                        break
                                                    except ValueError:
                                                        print("esto no es un numero")
                                                i = i + 1
                                            notasingles[a-1]=(name,round(pro,2),notasw)
                                    elif(x2 == "2" or x2 == "ver registro de notas"):
                                        system("cls")
                                        while(True):
                                            a=0
                                            while True:
                                                for ww in range(n):
                                                    print("")
                                                    print("\n resgistro de notas",a+1,": ")
                                                    print("Nombre:",notasingles[a][0])
                                                    print("Promedio:",notasingles[a][1])
                                                    print("Notas:",*notasingles[a][2])
                                                    a=a+1
                                                break
                                            print("")
                                            u=(input("responde aqui: "))
                                            if (u == "x" or u == "X"):
                                                break
                                            elif(u == "n"or "N"):
                                                pass
                                            else:
                                                print("esta funcion nose encuentra")
                                    elif(x2 == "3" or x2 == "ingresar nueva tarea"):
                                        system("cls")
                                        print("ingrese la tarea")
                                        tarea=(input(""))
                                        nuevataredemaye.append({'tarea': tarea})
                                    elif(x2 == "4" or x2 == "rebimiento de tarea"):
                                        while(True):
                                            for clave1,valor1 in recibiring.items():
                                                print(clave1,valor1)
                                            print("\n")
                                            oo=(input("ingrese 'x' para salir "))
                                            if(oo == "X" or oo == "x"):
                                                break
                                            else:
                                                print("escribe bien el dijito")
                                    elif(x2 == "5" or x2 == "salir"):
                                        break
                                    else:
                                        print("esta opcion nose encuentra")    
                        elif(x == "4" or x == "castellano"):
                            system("cls")
                            pass
                            while(True):
                                    print("======== menu de opciones ========")
                                    print("\n 1. ingresar notas \n 2. ver notas resgristradas \n 3. ingresar nueva tarea \n 4. recibiento de tarea \n 5. salir ")
                                    x2=(input("ingrese la opcion que desea ejecutar: "))
                                    if (x2 == "1" or x2 == "ingresar notas"):
                                        while(True):
                                            try:
                                                n=(int(input("ingrese la cantidad de que desea registrar: ")))
                                                while n < 0 :
                                                    print("este numero no es correcto")
                                                    n=(int(input("ingrese la cantidad que desea registrar: ")))
                                                break
                                                
                                            except ValueError:
                                                print("esto no es un numero")
                                        while(True):
                                            try:
                                                n2=(int(input("ingrese la cantidad de notas que desea registrar: ")))
                                                while n2 < 0:
                                                    print("esto no es valido")
                                                    n2=(int(input("ingrese la cantidad de notas que desea registrar: ")))
                                                break
                                            except ValueError:
                                                print("esto no es un numero")
                                        a=0
                                        for notas in range(n):
                                            name=(input("ingrese el nombre completo del estudiante: "))
                                            i=1
                                            a=a+1
                                            suma=0
                                            notasw=[]
                                            for notes1 in range(n2):
                                                while(True):
                                                    try:
                                                        notes=(float(input("ingrese la nota " + str(i) + ": ")))
                                                        pro=0
                                                        suma=suma + notes
                                                        pro=suma/n2
                                                        round(pro,2)
                                                        notasw.append(notes)
                                                        while notes <= 0 or notes > 5:
                                                            print("esto no es valido")
                                                            notes=(float(input("ingrese la nota " + str(i) + ": ")))
                                                        break
                                                    except ValueError:
                                                        print("esto no es un numero")
                                                i = i + 1
                                            notascaste[a-1]=(name,round(pro,2),notasw)
                                    elif(x2 == "2" or x2 == "ver registro de notas"):
                                        system("cls")
                                        while(True):
                                            a=0
                                            while True:
                                                for ww in range(n):
                                                    print("")
                                                    print("\n resgistro de notas",a+1,": ")
                                                    print("Nombre:",notascaste[a][0])
                                                    print("Promedio:",notascaste[a][1])
                                                    print("Notas:",*notascaste[a][2])
                                                    a=a+1
                                                break
                                            print("")
                                            u=(input("responde aqui: "))
                                            if (u == "x" or u == "X"):
                                                break
                                            elif(u == "n"or "N"):
                                                pass
                                            else:
                                                print("esta funcion nose encuentra")
                                    elif(x2 == "3" or x2 == "ingresar nueva tarea"):
                                        system("cls")
                                        print("ingrese la tarea")
                                        tarea=(input(""))
                                        nuevataredemaye.append({'tarea': tarea})
                                    elif(x2 == "4" or x2 == "rebimiento de tarea"):
                                        system("cls")
                                        while(True):
                                            for clave1,valor1 in recibircaste.items():
                                                print(clave1,valor1)
                                            print("\n")
                                            oo=(input("ingrese 'x' para salir "))
                                            if(oo == "X" or oo == "x"):
                                                break
                                            else:
                                                print("escribe bien el dijito")
                                    elif(x2 == "5" or x2 == "salir"):
                                        break
                                    else:
                                        print("esta opcion nose encuentra") 
                        elif(x == "5" or x == "naturales"):
                            system("cls")
                            pass
                            while(True):
                                    print("======== menu de opciones ========")
                                    print("\n 1. ingresar notas \n 2. ver notas resgristradas \n 3. ingresar nueva tarea \n 4. recibiento de tarea \n 5. salir ")
                                    x2=(input("ingrese la opcion que desea ejecutar: "))
                                    if (x2 == "1" or x2 == "ingresar notas"):
                                        while(True):
                                            try:
                                                n=(int(input("ingrese la cantidad de que desea registrar: ")))
                                                while n < 0 :
                                                    print("este numero no es correcto")
                                                    n=(int(input("ingrese la cantidad que desea registrar: ")))
                                                break
                                                
                                            except ValueError:
                                                print("esto no es un numero")
                                        while(True):
                                            try:
                                                n2=(int(input("ingrese la cantidad de notas que desea registrar: ")))
                                                while n2 < 0:
                                                    print("esto no es valido")
                                                    n2=(int(input("ingrese la cantidad de notas que desea registrar: ")))
                                                break
                                            except ValueError:
                                                print("esto no es un numero")
                                        a=0
                                        for notas in range(n):
                                            name=(input("ingrese el nombre completo del estudiante: "))
                                            i=1
                                            a=a+1
                                            suma=0
                                            notasw=[]
                                            for notes1 in range(n2):
                                                while(True):
                                                    try:
                                                        notes=(float(input("ingrese la nota " + str(i) + ": ")))
                                                        pro=0
                                                        suma=suma + notes
                                                        pro=suma/n2
                                                        round(pro,2)
                                                        notasw.append(notes)
                                                        while notes <= 0 or notes > 5:
                                                            print("esto no es valido")
                                                            notes=(float(input("ingrese la nota " + str(i) + ": ")))
                                                        break
                                                    except ValueError:
                                                        print("esto no es un numero")
                                                i = i + 1
                                            notasnatu[a-1]=(name,round(pro,2),notasw)
                                    elif(x2 == "2" or x2 == "ver registro de notas"):
                                        system("cls")
                                        while(True):
                                            a=0
                                            while True:
                                                for ww in range(n):
                                                    print("")
                                                    print("\n resgistro de notas",a+1,": ")
                                                    print("Nombre:",notasnatu[a][0])
                                                    print("Promedio:",notasnatu[a][1])
                                                    print("Notas:",*notasnatu[a][2])
                                                    a=a+1
                                                break
                                            print("")
                                            u=(input("responde aqui: "))
                                            if (u == "x" or u == "X"):
                                                break
                                            elif(u == "n"or "N"):
                                                pass
                                            else:
                                                print("esta funcion nose encuentra")
                                    elif(x2 == "3" or x2 == "ingresar nueva tarea"):
                                        print("ingrese la tarea")
                                        tarea=(input(""))
                                        nuevataredemaye.append({'tarea': tarea})
                                    elif(x2 == "4" or x2 == "rebimiento de tarea"):
                                        while(True):
                                            for clave1,valor1 in recibirnatu.items():
                                                print(clave1,valor1)
                                            print("\n")
                                            oo=(input("ingrese 'x' para salir "))
                                            if(oo == "X" or oo == "x"):
                                                break
                                            else:
                                                print("escribe bien el dijito")
                                    elif(x2 == "5" or x2 == "salir"):
                                        break
                                    else:
                                        print("esta opcion nose encuentra")
                        elif(x == "6" or x == "sociales"):
                            system("cls")
                            pass
                            while(True):
                                    print("======== menu de opciones ========")
                                    print("\n 1. ingresar notas \n 2. ver notas resgristradas \n 3. ingresar nueva tarea \n 4. recibiento de tarea \n 5. salir ")
                                    x2=(input("ingrese la opcion que desea ejecutar: "))
                                    if (x2 == "1" or x2 == "ingresar notas"):
                                        while(True):
                                            try:
                                                n=(int(input("ingrese la cantidad de que desea registrar: ")))
                                                while n < 0 :
                                                    print("este numero no es correcto")
                                                    n=(int(input("ingrese la cantidad que desea registrar: ")))
                                                break
                                                
                                            except ValueError:
                                                print("esto no es un numero")
                                        while(True):
                                            try:
                                                n2=(int(input("ingrese la cantidad de notas que desea registrar: ")))
                                                while n2 < 0:
                                                    print("esto no es valido")
                                                    n2=(int(input("ingrese la cantidad de notas que desea registrar: ")))
                                                break
                                            except ValueError:
                                                print("esto no es un numero")
                                        a=0
                                        for notas in range(n):
                                            name=(input("ingrese el nombre completo del estudiante: "))
                                            i=1
                                            a=a+1
                                            suma=0
                                            notasw=[]
                                            for notes1 in range(n2):
                                                while(True):
                                                    try:
                                                        notes=(float(input("ingrese la nota " + str(i) + ": ")))
                                                        pro=0
                                                        suma=suma + notes
                                                        pro=suma/n2
                                                        round(pro,2)
                                                        notasw.append(notes)
                                                        while notes <= 0 or notes > 5:
                                                            print("esto no es valido")
                                                            notes=(float(input("ingrese la nota " + str(i) + ": ")))
                                                        break
                                                    except ValueError:
                                                        print("esto no es un numero")
                                                i = i + 1
                                            notassoci[a-1]=(name,round(pro,2),notasw)
                                    elif(x2 == "2" or x2 == "ver registro de notas"):
                                        system("cls")
                                        while(True):
                                            a=0
                                            while True:
                                                for ww in range(n):
                                                    print("")
                                                    print("\n resgistro de notas",a+1,": ")
                                                    print("Nombre:",notassoci[a][0])
                                                    print("Promedio:",notassoci[a][1])
                                                    print("Notas:",*notassoci[a][2])
                                                    a=a+1
                                                break
                                            print("")
                                            u=(input("responde aqui: "))
                                            if (u == "x" or u == "X"):
                                                break
                                            elif(u == "n"or "N"):
                                                pass
                                            else:
                                                print("esta funcion nose encuentra")
                                    elif(x2 == "3" or x2 == "ingresar nueva tarea"):
                                        print("ingrese la tarea")
                                        tarea=(input(""))
                                        nuevataredemaye.append({'tarea': tarea})
                                    elif(x2 == "4" or x2 == "rebimiento de tarea"):
                                        while(True):
                                            for clave1,valor1 in recibirsoci.items():
                                                print(clave1,valor1)
                                            print("\n")
                                            oo=(input("ingrese 'x' para salir "))
                                            if(oo == "X" or oo == "x"):
                                                break
                                            else:
                                                print("escribe bien el dijito")
                                    elif(x2 == "5" or x2 == "salir"):
                                        break
                                    else:
                                        print("esta opcion nose encuentra") 
                        elif(x == "7" or x == "salir"):
                            time.sleep(2)
                            print("espere un momento")
                            time.sleep(1)
                            system("cls")
                            break
                        else:
                            print("esta opcion nose encuentra")
                else:
                    print("usuarios incorrectos, ingrese de nuevo")
                    time.sleep(4.1)


            elif(op2 == "3" or op == "salir"):
                break
            else:
                print("esta funcion nose encuentra")
    elif(op == "3" or op == "salir"):
        break
    else:
        print("esta funcion nose encuentra")
                



                            







               


