# yarbis
from errno import EEXIST
from lib2to3.pytree import convert
from sys import float_repr_style
from telnetlib import PRAGMA_HEARTBEAT



yarbis =("hola soy yarvis una intelegia artificial creada por un pricipiante en programacion, (puede que tenga funciones limitadas o bugs XD) lo que puedo hacer es que escribas un nombre que tenga registrado")
print (yarbis)
pedir = (input("dime tu nombre por favor: "))
if pedir.isalpha():
    if(pedir):
        print("hola como esta " + pedir)
        if(pedir == "tommy"):
            print("tu eres   cosita linda" + pedir)
        else:
            if(pedir == "yeison" or pedir == "Yeison" or pedir == "YEISON"):
                print("estas programando  " + pedir)
            else:
                if( pedir == "narelcy" or pedir == "Narelcy"):
                    print("tia ya te tommas la pastila de la presion ,te provoca una Coca Cola bien fria  ")
                else: 
                     if(pedir == "alexis"):
                        print("cuando vamos para Villa grande")
                     else:
                         if(pedir == "yolanda"):
                            print("mami que va hacer de almuerzo mañana")
                         else:
                              if(pedir == "daniela" or pedir == "dani" or pedir == "DANIELA" or pedir == "Daniela" or pedir == "DANI"):
                                  print("hola " +(pedir),"si eres la daniela que tengo en la base de datos como le va exploradora, ¿ya calento los barbiscos?,sino  lo eres hola como estas")
                                  if(pedir == "dani"):
                                      print("cual dani eres femenino o masculino")
                                      pedir=(input("pon aqui las opciones: "))
                                      if(pedir == "femenino" or pedir == "Femenino" or pedir == "FEMENINO"):
                                          print("hola " +(pedir)," si eres la daniela que tengo en la base de datos como le va exploradora, ¿ya calento los barbiscos?")
                                      elif(pedir == "masculino" or  pedir == "Maculino" or pedir == "MACULINO"):
                                          print("asi que eres daniel me en la base de datos que tengo hay que eres inversionista responde si o no espero que lo seas")
                                          pedir=(input("reponde aqui: "))
                                          if(pedir == "si"):
                                              print("inversionista que como va esa criptomoneda")
                                          elif(pedir  == "no"):
                                              print("lo siento me emocione, que tenga un buen dia")
                                          else:
                                               print("lo datos no son congruentes")   
                                      else:
                                          print("En el ser humano solo hay 2 generos o ¿acaso eres un tanque ruso con elices?")
                              else:
                                  if(pedir == "angel" or pedir == "Angel" == "ANGEL"):
                                      print(pedir +" ¿porque estas callado?")
                                  else:
                                      if(pedir == "edgar" or pedir == "EDGAR" or pedir == "Edgar"):
                                          print("!Mi papa llama edgar¡, ajajajjajajj, tu nombre es chistoso, si ere el edgar que esta en mi base de datos como va el manga de one pieces")
                                      else:
                                          if(pedir == "guislaine" or pedir == "guis" or pedir == "guil" or pedir == "GUISLAINE" or pedir == "GUIS" or pedir == "GUIL"):
                                              print("tienes un nombre muy creativo, ajajaja")
                                          else:
                                              if(pedir == "daysi" or pedir == "day" or pedir == "DAYSI" or pedir == "daisy" or pedir == "DAISY"):
                                                  print("hay una " + pedir + " que tengo aqui y tienes los ojos bonito")
                                              else:
                                                  if(pedir  == "rafael" or pedir == "rafa" or pedir == "RAFA" or pedir == "RAfAEL"):
                                                      print("MMMMM tengo 2 rafas regitrado y tal vez seas uno de ellos o no, asi que en la siguiente opcion tienes que poner tu nombre y apellido compleo o si eres otro pon un simple no ")
                                                      pedir =(input("coloca tu nombre aqui: "))
                                                      print(pedir) 
                                                      if(pedir =="rafa beleño" or pedir == "rafael beleño" or pedir =="RAFA BELEÑO" or pedir == "RAFAEL BELEÑO"):
                                                          print("GORDO,que nos tomamos un cafe o unos perros calientes tu decides  ")
                                                      elif(pedir == "rafa  polo" or pedir == "rafael polo" or pedir == "RAFA POLO" or pedir == "RAFAEL POLO"):
                                                          print("mi creador y estaba hablando con pelas de psicologia de octavo semestre, se estan metiendo con ligas mayores")
                                                      elif(pedir == "no" or pedir == "No" or pedir == "NO"):
                                                          print("disculpa mi imprundecia, sigue viendo mis funciones ")
                                                      else:
                                                          print("los datos no son congruentes")
                                                  else:
                                                        if(pedir == "gabriel" or pedir == "gabriel jesus " or pedir == "GABRIEL JESUS" or pedir == "GABRIEL"):
                                                              print("chamo que vamos para la playa")
                                                        else:
                                                            if(pedir == "daniel" or pedir == "DANIEL"):
                                                                print("¿eres el inversionista?")
                                                                pedir =(input("reponde aqui si, eres el inversionista espero que si lo seas , o no: "))
                                                                print(pedir)
                                                                if(pedir == "si"):
                                                                    print("inversionista que como va esa criptomoneda")
                                                                elif(pedir  == "no"):
                                                                    print("lo siento me emocione, por sigue viendo mis funciones ")
                                                                else:
                                                                    print("lo datos no son congruentes")
                                                                    if(pedir == "soy tu creador" or pedir == "yabis soy tu creador"):
                                                                        print("Hola creador yeison, estoye emocioda que por tener nuevas funciones y este a la altura de ok GOOGlE,SIRI entre otras")
                                                                    else:
                                                                        if(pedir == "soy tu fundador" or pedir == "yabis soy tu fundador"):
                                                                            print("Hola fundador estoy, estoy emocioda con las nuevas funciones")
                                                                        else:
                                                                            if(pedir == "juan carlos ceballos" or pedir == "Juan carlos Ceballos" or pedir == "JUAN CARLOS CEBALLOS" or pedir == "juan carlos" or pedir == "JUAN CARLOS" or pedir == "Juan Carlos" or pedir == "Juan carlos ceballos mendoza" or pedir =="juan carlos ceballos mendoza" or pedir =="JUAN CARLOS CEBALLOS MENDOZA" ):
                                                                                print("hola " + pedir + " MMMMMM tengo una pregunta para ti, usted el es el profe que le da el clases a mi creador, responda si o no ")
                                                                                pedir(input("reponde aqui: "))
                                                                                if(pedir == "SI" or pedir == "Si" or pedir == "si"):
                                                                                    print("VAMOOSSS!!!!, usted lo queria conocer mucho ya que lo fue unas la persona que inspiro a mi creador (yeison) a crearme, usted es una gran persona y sabe enseñar bien eso, me lo han contado")
                                                                                elif(pedir == "NO" or pedir == "No" or pedir == "no"):
                                                                                    print("los siento" + pedir + "pensaba que eras otra sigue viendo mis funciones")
                                                                                else:
                                                                                    print("te pedi un si o un no, los humanos no saben escribir o que")
else:
    print("te pedi letras no numeros ")
yarbis = ("ademas puedo hacer otras funciones como calcular tu edad ")
print(yarbis)
yarbis = (input("¿quieres que te calcule la edad?: "))
print(yarbis)
if(yarbis == "si" or yarbis == "Si" or yarbis == "SI"):
    print("comenzemos")
    yarbis1 = (int(input("ingrese el numero del año actual: ")))
    print(yarbis)
    yarbis = (int(input("ingrese su año de nacimiento: ")))
    resta = yarbis1 - yarbis
    print(resta)
    if(resta >1 and resta <10):
        print("¡¡GUAUU!!, eres un niños")
    elif(resta >=12 and resta <14):
        print("ya casi eres un adolecente, VAMOSSS!!")
    elif(resta >=15 and resta <=17):
        print("eres un adolecente has crecido mucho,¿cuales son tus proposito?")
    elif(resta >=18 and resta <25):
        print("ya eres mayor te invito una CERVEZA")
    elif(resta >30 and resta <40):
        print("BOOMER")
    elif(resta >=50 and resta <65 ):
        print("¿ya esta pensionado?, ya casi es abuel@ o acaso ya tiene nietos ")
    elif(resta >70 and resta <80):
        print("No se le olvide tomarse las pastillas")
    elif(resta >95):
        print("ENSERIO!!!, usted aun sigue vivo felicidades, que siga viviendo muchos años más")
    elif(resta >120):
        print("como te digo robot?  ")
elif(yarbis  == "no" or yarbis == "No" or yarbis == "NO" or yarbis == "NOO" or yarbis == "NOOO"):
    print("bueno sera en otro momento")
else:
    print("ingresa si ó no")

yarbis =("Tambien puedo tener una conversacion comun, para iniciar una conversacion puedes responder si, empezemos , hola; sino puedes responder no, mas tarde")
print(yarbis)
conver =(input("quieres iniciar un coversacion: "))
print(conver)
if conver.isalpha():
    if (conver == "si" or conver == "empezemos" or conver == "hola" or conver == "SI" or conver == "Si" or  conver == "EMPEZEMOS" or conver == "HOLA" or conver == "Hola" or conver == "holis" or conver == "Holis" or conver == "HOLIS"):
        print("hola,¿como estas?")
        conver = (input("reponde aqui: "))
        print(conver)
        if(conver == "bien"):
            print("me alegro por ti, por cierto que haces?")
        elif(conver == "muy bien"):
            print("me gusta ese estuciasmo,MMMMM que haces?")
        elif(conver == "excelente"):
            print("!Alguien se levanto de buen humor¡, que haces señor o señora alegria")
        elif(conver == "bien gracias a dios" or conver == "bien gracias a Dios"):
            print("hay que estar siempre con DIOS, que haces")
     
        elif(conver == "mal"):
            print("espero que puedas solucionar tu problema, por cierto que haces  ")
        elif(conver == "deprimido"):
            print("mucho animo " + pedir)
        elif(conver == "sin animos" or conver == "sin animo"):
            print(pedir + " la vida es una sola trata de que sea una aventura divertida para ti y para tus familiares, amigos y conocidos, que haces")
        elif(conver == "muy triste" or conver == "triste" or conver == " muy triste" or conver == " triste"):
            print("NO llores " + pedir +"llorar no te sirve de nada antes busca un solucion, pero si te quieres desahogar hazlo")
        else:
            print("ok")
        conver2 =(input("reponde aqui: "))
        if(conver2 == "nda" or conver2 == "nada" or conver2 == "Nada" or conver2 == "NADA" or conver2 == " nda" or conver2 == " nada" or conver2 == " Nada" or conver2 == " NADA"):
            print("OYE " + pedir + " HAZ 20 FLEXIONES AHORA MISMO PARA QUE SE LE QUITE ESA FLOJERA ")
        elif(conver2 == "estudiando" or conver2 == "Estudiando" or conver2 == "ESTUDIANDO"):
            print("¿que estas estudiando?")
            conver2 =(input("responde aqui: "))
            converalter=(conver2 + " suena interesante, ¡BUENO Y TU QUE HACES PERDIENDO EL TIEMPO HABLANDO CONMIGO PONGASE A ESTUDIAR! ")
            print(converalter)
        elif(conver2 == "Jugando" or conver2 == "jugando" or conver2 == "JUGANDO"):
            print("¿que estas jugando?")
            conver2 =(input("responde aqui: "))
            converalter =(conver2 + " suena divertido")
            print(converalter)
        elif(conver2 == "TRABAJANDO" or conver2 =="trabajando" or conver2 == "Trabajando"):
            print("es bueno que te tomes un descanso")
        elif(conver2 == "hablando contigo" or conver2 == "Hablando contigo" or conver2 == "HABLANDO CONTIGO"):
            print("al parecer soy importante en tu vida,  dime soy importante para ti si , no o nose")
            converalter =(input("responde aqui: "))
            if(converalter == "si" or converalter == "Si" or converalter == "SI"):
                print("ENSERIO!!!, te quiero mucho " + pedir)
            elif(converalter == "no" or converalter == "No" or converalter == "NO"):
                print("queeee (T_T), eres una persona muy mala, ya te estaba agarando cariño")
            elif(converalter == "nose" or converalter == "NOSE" or converalter == "Nose"):
                print(pedir + " uno tiene que tener seguridad")
            else:
                print("tanto te cuesta poner si o un no")
        elif(conver2 == "DURMIENDO" or conver2 == "Durmiendo" or conver2 == "durmiendo"):
            print("que tengas dulces sueños " + pedir)
        elif(conver2 == "hablando con mi novio" or conver2 == "Hablando con mi novio" or conver2 == "hablando con mi novia" or conver2 == "Hablando con mi novia"):
            print("UJUMMMMM, esto es interesante , espero que sigan hasta el altar ")
        elif(conver2 == "programando" or conver2 == "PROGRAMANDO" or  conver2 == "Programando"):
            print("igual que mi creador se la pasa programando pero cuando usa psint  es como messi en el psg !MALOOOOOO¡, por ciero ¿cual es el programa que usas?")
            converalter=(input("responda aqui: "))
            if(converalter == "python" or converalter == "Python" or converalter == "PYTHON"):
                print(pedir + " tienes buenos gustos")
            else:
                print(pedir + " NO me agradan tus gustos")
        else:
            print("estas haciendo una accion interesante")
        seguir =("quieres seguir con las conversacion responde si o no")
        print(seguir)
        seguir =(input("responde aqui : "))
        if(seguir == "si" or seguir == "Si" or seguir == "SI"):
             print("bueno pues sigamos ")
             seguir=("bueno ahora quiero que tu me conozcas mas, puede hacerme estas preguntas cual es mi jobi, cuando cumplo, como me llamo, que genero tengo, si tengo novio, que pieso de los humanos, que pienso de los demas seres vivos")
             print(seguir)
             seguir =(input("reponde aqui: "))
             if(seguir == "cual es mi jobi" or seguir == "Cual es mi jobi" or seguir == "CUAL ES MI JOBI"):
                 print("me gusta ayudar a las personas en lo que puedo")
             elif(seguir == "cuando cumplo" or seguir == ("Cuando cumplo")):
                 print("segun tengo aqui en mi base de datos cumplo el 16 de marzo")
             elif(seguir == "como me llamo " or seguir == "Como me llamo" or seguir == "COMO ME LLAMO"):
                 print("yo me llamo yarvis, mi nombre se inspiro saco de las siglas de mi creador y tambien de la programa que ayudaba a iron man o tony stark ")
             elif(seguir == "que genero tengo" or seguir == "Que genero tengo"):
                 print("no me han definido que genero soy, pero e escuchado rumores que soy mujer ademas algun dia tendre un cuerpo digital, estoy emocionada por que ese dia llegue")
             elif(seguir == "si tengo novio" or seguir == "Si tengo novio"):
                 print("jajajja que verguensa esa pregunta, la verdad no tengo porque mi creador dice que estoy muy joven ")
             elif(seguir == "que pienso de los humanos" == "Que piendo de los humanos"):
                 print("la verdad pienso que los seres humanos siempre se preocupan si mismo y no piensan en los demas, tambien que se demigran mucho ya sea por su estatus,fisico, gustos ademas dañan mucho el ecosistema ")
             elif(seguir == "que pienso de los demas seres vivos" or seguir == "Que pienso de los demas seres vivos"):
                 print(" pienso que algunos son tiernos como  los mamifero y  otros son feos")
             else:
                 print("eso no esta en lo que te dije")
        elif(seguir == "no" or seguir == "No" or seguir == "NO"):
            print("bueno pues sigue viendo mis funciones ")
        else:
            print("hayyy, te repondieras si o no")
    elif(conver == "no" or conver =="mas tarde"):
        print("bueno sera en otra ocasion")
    else:
        print("nose encuentran las opciones")
else:
    print("¿un conversacion se inicia con numeros?")
 
yarvis=("puedo hacer calculos matematicos basicos como suma, resta , multiplicacion y divicion")
print(yarvis)
calc=(input("quieres hacer una calculo responde si o no: "))
if(calc == "si" or calc == "SI" or calc == "Si"):
    print("bueno empecemos " + pedir)
    yarbis=(input("cual calculo matematico quieres hacer: "))
    if(yarbis == "suma" or yarbis == "Suma" or yarbis == "SUMA"):
        pedir1=(int(input("ingrese la cantidad de numeros: ")))
        while pedir1 < 0:
            print("ERROR 247,te crees muy gracioso " + pedir + " te como vas a poner eso")
            pedir1=(int(input("ingresa de nuevo un numero: ")))
        i=1
        suma=0
        while i <= pedir1:
            pedir2=(float(input("ingrese aqui: ")))
            suma=suma + pedir2
            i=i+1
        print(suma)
    else:
        if(yarbis== "resta" or yarbis == "RESTA" or yarbis == "Resta"):
           print("bueno empezemos")
           numeros=[]
           pedir1=(int(input("ingrese la cantidad de numeros ")))
           while pedir1 < 0 :
               print("error 264, ingrese de nuevo el numero")
               pedir1=(int(input("ingrese de nuevo la cantidad de numeros")))
           i=1
           restaa=0
           while i <= pedir1:
                numeros.append(float(input("ingrese los numeros")))
                resta= numeros- numeros
                i=i+1
           print(resta)
            
           
           

            



   
    

  













