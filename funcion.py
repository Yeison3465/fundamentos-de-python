from glob import glob
from os import system
import time

from tracemalloc import stop
system('cls')

class Usuario:
  def __init__(self, nombre, apellido,correo,usuario,contrasena):
    self.nombre = nombre
    self.apellido = apellido
    self.correo = correo
    self.usuario = usuario
    self.contrasena = contrasena

session_iniciada=None
usuarios = list()
usu_registra = {}
codigos = {}
menfar = {1: 'Registrar producto nuevo.',
          2: 'Inventario Total.',
          3: 'Buscar producto.',
          4: 'Eliminar producto.',
          5: 'Salir completamente.'}
def message(title):
    system('cls')
    print(title)
    time.sleep(0.1)
def message1(title):
    system('cls')
    print(title)

#DEFINO LOS ATRIBUTOS DEL USUARIO
def mostrarMenu(men2):
    for opt in men2:
        print(opt,'-', men2[opt]) 

def iniciar_s():#INICIO DE SESION
    
    message1('+--------Iniciar Sesion--------+')
    usuario = input('Ingrese el Ususario: ')
    contraseña = input('Ingrese la cotraseña: ')
    if (x for x in usuarios if x.usuario == usuario) and (x for x in usuarios if x.contrasena == contraseña):
        pass 
        while (True):
            system('cls')
            session_iniciada=True
            print('BIENVENIDO AL CONTROL DE VENTAS E INVENTARIO PARA  LA FARMACIA',farmacia, '\n|=================BIENVENIDO AL MENÚ DE LA FARMACIA===============|''\n')
            mostrarMenu(menfar)
            try:
                opmenfarm = int(input('\nEscoja una opción: '))
                if (opmenfarm==1):#REGISTRO DE MEDICAMENTOSok                    
                    system('cls')
                    while(True):
                        try:                       
                            message1('|----------------- REGISTRO DE MEDICAMENTO-----------------|')
                            nombre = input('Nombre del Fármaco: ')
                            n_gene = input('Nombre Generico: ')
                            Cat_desc = input('Categoría/Descripción: ')
                            Prove = input('Proveedores: ')
                            t = input('Introduzca el Tipo de Fármaco: ')                                                                
                            cand= int(input('Introduzca la Cantidad: '))
                            unid = int(input('Introduzca la unidad del Fármaco: '))
                            v_rio = float(input('Introduzca el Valor Unitario del Fármaco: '))                                                                                                                 
                            v_tl = float(input('Introduzca el Valor Total: '))    
                            while(nombre.isalpha or nombre.isspace()) and (n_gene.isalpha or n_gene.isspace()) and (Cat_desc.isalpha or Cat_desc.isspace()) and (Prove.isalpha or Prove.isspace()) and (t.isalpha or t.isspace()) and (codigo.isnumeric()) :
                                if all(x.isalpha or x.isspace()for x in nombre) and all(x.isalpha or x.isspace() for x in n_gene) and all(x.isalpha or x.isspace() for x in Cat_desc) and all(x.isalpha or x.isspace() for x in Prove) and all(x.isalpha or x.isspace() for x in t) and (codigo in codigos and codigo.isnumeric()):
                                    message1('\nIntoduzca el Codigo del Fármaco: {}'.format(codigo),'\nNombre del Farmaco: {}'.format(nombre),'\nNombre Genercio: {}'.format(n_gene),'\nCategoría/Descripción: {}'.format(Cat_desc),'\nProveedores: {}'.format(Prove),
                                            '\nIntroduzca el Tipo de Fármaco: {}'.format(t),'\nIntroduzca la Cantidad: {}'.format(cand),'\nIntroduzca la unidad del Fármaco: {}'.format(unid),
                                            '\nIntroduzca el Valor Unitario del Fármaco: {} '.format(v_rio),'\nIntroduzca el Valor Total: {}'.format(v_tl))
                                else:
                                    message1('Error...datos no válidos...')
                                    break 
                        except:                        
                            codigo = input('Intoduzca el Codigo del Fármaco: ')
                            if codigo in codigos:
                                for x in range(3):
                                    message('Validando Informacion.''\nPor favor espere.')
                                    message('Validando Informacion..''\nPor favor espere..')
                                    message('Validando Informacion...''\nPor favor espere...')
                                message1('El Codigo ya se encuentra registrado''\nPor favor ingrese uno que no se encuentre registrado')                                                  
                                continue
                            else:                                                                                                      
                                print('Datos no valido''\nPor favor ingresar datos validos')
                                break
                        codigos[codigo]=nombre,n_gene,Cat_desc,Prove,t,cand,unid,v_rio,v_tl
                        yu = input('¿Desea Registar un nuevo Fármaco? (si) o (no): ')
                        if yu == '1' or yu == 'SI' or yu == 'Si' or yu== 'sí' or yu == 'sI' or yu == 'S' or yu == 'yes':
                            print('Cargando Formulario de Registro.')
                            for x in range(3):
                                message('Cargando Formulario de Registro.')
                                message('Cargando Formulario de Registro..')
                                message('Cargando Formulario de Registro...')
                            continue
                        elif yu == '2' or yu == 'NO' or yu == 'No' or yu =='no' or yu == 'nO' or yu == 'N':
                            print('Redirigiendo al inicio')
                            for x in range(3):
                                message('Redirigiendo al inicio.')
                                message('Redirigiendo al inicio..')
                                message('Redirigiendo al inicio...')
                        else:
                            print('Ingrese un opcion valida')
                elif (opmenfarm==2):#LISTAR MEDICAMENTOSok
                    for codigo in codigos:
                        print(
                    '''
                        codigo      :{}
                        nombre      :{}
                        n_gene      :{}    
                        Cat_desc    :{}
                        Prove       :{}
                        t           :{}
                        cand        :{}
                        unid        :{}
                        v_rio       :{}
                        v_tl        :{}
                    '''.format(codigo,codigos[codigo][0],codigos[codigo][1],codigos[codigo][2],codigos[codigo][3],codigos[codigo][4],codigos[codigo][5],codigos[codigo][6],
                    codigos[codigo][7],codigos[codigo][8]))
                elif (opmenfarm==3):#ELIMINAR MEDICAMENTO
                    A=77
                elif (opmenfarm==4):#SALIR COMPLEMENTAMENTE DEL PROGRAMAok
                    message('ADIOS! QUE TENGA BUEN RESTO DE DIA')
                    time.sleep(20000)
            except ValueError:
                print('\nDato no Valido.')
                time.sleep(0.5)
def listar_usu():#LISTAR USUARIOSok
    if (len(usuarios)>0):
        for user in usuarios:
                print(
            '''
                usuario:     {}
                nombre:   {}
                apellido:   {}
                mail: {}
                contraseña: {}
            '''.format(user.nombre,user.apellido,user.correo,user.usuario,user.contrasena))
    else: 
        message1('No hay usuarios registrados')
    enter=('Presione enter para salir: ')
    print(' ')
    time.sleep(5) 
def borrar_usuario():#ELIMINAR USUARIO
    if (len(usuarios)>0):
        message1('+--------Eliminar usuario--------+')
        correo = input('Ingrese el correo del usuario que quiere eliminar: ') 
        for usuario_borrar in usuarios:
            if correo == usuario_borrar.correo:
                usuarios.remove(usuario_borrar)
                break
     
        message1('Usuario Eliminado')       
        enter = input('Presionar enter')
        print('')
    else: 
        message1('No hay usuarios registrados')
    
def registro_usu():#REGISTRO USUARIOok
    print('')
    system('cls')
    while (True):
        try: 
            message1('|-----------------FORMULARIO DE REGISTRO-----------------|')##<-------INICIO PARA REGISRTO DE USUARIO 
            nombre = input('Ingrese el Nombre : ') #inserta dentro del marcador de posición de la cadena. El marcador de posición se define mediante corchetes: {}
            apellido = input('Ingrese el Apellido: ')  #COLOCAMOS LOS LIMITES PARA NOMBRE, APELLIDO (CON ISALPHA Y .ISSPACE PARA QUE SEA ALPHABETICO)
            correo = input('Ingrese un Correo: ')      #Y A CORREO .FIN PARA DECIRLE AL CORREO QUE TIENE QUE TENER @ Y PUNTO (.)
            while(nombre.isalpha or nombre.isspace()) and (apellido.isalpha or apellido.isspace()) and (correo.find('@')>=0 and correo.find('.')>=0):
                if all(x.isalpha or x.isspace()for x in nombre) and all(x.isalpha or x.isspace() for x in apellido) and (correo.find('@')>=0 and correo.find('.')>=0):
                    message1('Ingrese el Nombre : {}'.format(nombre),'\nIngrese el Apellido: {}'.format(apellido),'\nIngrese un Correo: {}'.format(correo))        
                else:
                    message1('Error...datos no válido...')
                    break
        except:
            usu = input('Ingrese el Usuario:')
            if usu in usu_registra:
                
                message1('El usuario ya se encuentra registrado''\nPor favor ingrese un usuario que no se encuentre registrado')
                continue
            else:                
                contraseña = input('Ingrese una contraseña:')
                message('Registrado con exito.')
                time.sleep(0.5)
                
            usu_registra[usu]=nombre,apellido,correo,contraseña 
            nuevo_usuario=Usuario(nombre,apellido,correo,usu,contraseña )
            usuarios.append(nuevo_usuario)
            g = input('¿Desea Registar un nuevo usuario? (si) o (no): ')
            if g == '1' or g == 'SI' or g == 'Si' or g== 'sí' or g == 'sI' or g == 'si' or g =='s' or g =='S' or g== 'SÍ' or g == 'yes':
                print('Cargando Formulario de Registro')
                for x in range(3):
                    message('Cargando Formulario de Registro.')
                    message('Cargando Formulario de Registro..')
                    message('Cargando Formulario de Registro...')
                    system('cls')
                continue
            elif g == '2' or g == 'NO' or g == 'No' or g=='no' or g== 'nO' or g =='n' or g =='N' or g=='O':
                print('Por favor espere.')
                for x in range(3):
                    message('Redirigiendo al Menú Principal.')
                    message('Redirigiendo al Menú Principal..')
                    message('Redirigiendo al Menú Principal...')
                break
            else:               
                print('Ingrese un opcion valida.2')
                system('cls')
                break                  
def modificar_usuario():
    if (len(usuarios)>0):
        message1('+--------Modificar usuario--------+')
        correo = input('Ingrese el correo del usuario que quiere modificar: ')  
        for usuario in usuarios:
            if correo == usuario.correo:
                usuario.nombre = input('Ingrese nuevo Nombre : ')
                usuario.apellido = input('Ingrese nuevo Apellido: ') 
                usuario.correo = input('Ingrese nuevo Correo: ')  
                usuario.usuario = input('Ingrese nuevo usuario ') 
                usuario.contrasena = input('Ingrese nueva contraseña: ') 
            
            else:
                message('usuario no encontrado.')
    else: 
        message1('No hay usuarios registrados')
def salir_s():#SALIRok
    message('ADIOS! QUE TENGA BUEN RESTO DE DIA')
    time.sleep(2000)
     
#DESDE AQUI COMENZARA A CORRER EL CODGIO 
while True:#ok   
    system('cls')
    print('SISTEMA DE CONTROL PARA INVENTARIO DE FARMACIAS')  #RESGISTRO DE LA FARMACIA PARA PODER DAR INGRESO
    print('===============================================')
    while True:
        try:
            far = input('Registre el Nombre de la Farmacia: ')
            if all(x.isalpha or x.isspace()for x in far) == True: ## .isalpha es para alphabetico y .isspace para el espacio entre escritura
                message1('Registre el Nombre de la Farmacia: ')# SI NO REGISTRA LA FARMACIA NO PODRA CONTINUAR 
            else:
                message1('Has ingresaso un dato no valido.')
                time.sleep(0.6)
                break
        except: 
            print('')
        farmacia = far 
        
        print('\nBIENVENIDO AL CONTROL DE VENTAS E INVENTARIO PARA  LA FARMACIA', far)
        time.sleep(0.5)
        message('Registrado con exito.')
        time.sleep(0.5)
        message('Redirigiendo al Menú Principal.')
        
        while True:#MOSTRAMOS MENU
            message('\n|-------------MENU PRINCIPAL-------------|'
                    '\n1.------------Iniciar Sesion.------------|'
                    '\n2.------------Registrar Usuarios---------|'
                    '\n3.------------Eliminar Usuarios----------|'
                    '\n4.------------Listar Usuarios------------|'
                    '\n5.------------Modificar Usuarios------------|'
                    '\n0.------------Suspender sistema----------|')
            try:
                op = int(input('\nEscoja una opción: '))
                if op == 1:
                    iniciar_s()
                elif op == 2:
                    registro_usu()
                elif op == 3:
                    borrar_usuario()
                elif op == 4:
                    listar_usu()
                elif op == 5:
                    modificar_usuario()
                elif op == 0:
                    salir_s()
                else:
                    print('Error...ingrese una opción válida...')
            except:
                time.sleep(1)
                message1('---------------------------------------''\nError...volviendo al menu principal...')

            






               

