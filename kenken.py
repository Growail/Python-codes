#para iniciar el juego se debe llamar a la funcion main()#
#importa tkinter
from tkinter import *
#importa los mensajes o advertencias
from tkinter import messagebox
#importa los hilos
import threading
#importa funciones de tiempo
import time
#importa para crear combinaciones#
import itertools

#importa para acceder a intenet#

import webbrowser
#importa ramdom
import random
#importa musica
import winsound
#importa el guardar y buscar como..
from tkinter.filedialog import *
#importamos el modulo para trabajar con sockets
import socket
flag = False
#guarda el nimbre del jugador actual#
nombre=""
#el tiempo que ya paso#
tiempo_pasado=0
#si hay algun error matematico#
error=0
#para saber si hay un error en fila o columna#
error2=0
#para saber que juegos se han usado
ya_usados=[]
SudokuBoard=[]
#para saber el nivel seleccionado
usado=[]
#para saber que juego es el actual
actual=[]
#carga crea un matriz con text y color por jaulas#
juego2=[]
#almacenan los juegos de los respectivos niveles#
nivel3=[]
nivel4=[]
nivel5=[]
nivel6=[]
nivel7=[]
nivel8=[]
nivel9=[]
#es la matriz grafica #
boton=[]
#matriz logica#
matriz=[]
#para saber el tamaño de la matriz#
filas=0
#para saber si el reloj esta activo o el timer#
reloj=0
#para saber si los botones van a la derecha o a la izquierda#
posicion=0
#para saber si hay sonido al final o no
sonido=0
#ancho y largo son valores para el tamaño de los botones#
ancho=0
largo=0
#fill,col para saber el boton seleccionado#
fil=""
col=""
matriz3=[[0,0,0],[0,0,0],[0,0,0]]
matriz4=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#para saber los segundos#
segundos=0
#para saber los minutos#
minutos=0
#para saber las horas#
horas=0
#para ver si el juego ya inicio #
inicio=False
#para saber si esta en pausa #
pausa=True
#variable para guardar los valores del undo#
deshacer=[]
#rehacer: variable para hacer el redo#
rehacer=[]
#saber si se esta jugando en modo sobrevivir#
activar_sobrevivir=0
#posibles me guarda los disponobles#
posibles=[]
#####################################
##backtraking3

##################################33
#esta funcion retorna un true o un False dependiendo de que si la matriz posee errores o no#
def es_correcto3(board):
    global error,matriz
    
    inicio_de_validacion3(board)
    
    
    
    if error ==1:
        error=0
        return False
    elif error==0:
        return True
#esta funcion toma el diccionario actual y lo trabaja#
def inicio_de_validacion3(board):
    global actual
    a=actual
    for i in a.values():
        validar_de_verdad3(i,board)
    return
#agrara un elemento del diccionario y separa el operador del numero, tambien agarra los valores de la matriz en la tuple de la llave#
def validar_de_verdad3(i,board):
        opera=""
        numero=""
        resul=[]
        lugar=[]
        for j in i:
            if type(j)==str:
                if operador3(j)!="":
                    opera=operador3(j)
                    numero=obtener_numero3(j)
                else:
                    opera="#"
                    numero=obtener_numero3(j)
            elif type(j)==tuple:
                lugar+=[j]
                resul+=[board[j[0]][j[1]]]
            
        resul.sort(reverse=True)
        return comprobar3(resul,lugar,numero,opera,board)

#obtiene el numero de in string#
def obtener_numero3(string):
    resul=""
    for j in string:
        if j=="0" or j=="1" or j=="2" or j=="3" or j=="4" or j=="5" or j=="6" or j=="7" or j=="8" or j=="9":
            resul+=j
    return resul
    
                
            

#saca el operador de un string#    
def operador3(string):
    resul=""
    for i in string:
        if i=="+":
            resul="+"
        elif i=="/":
            resul="/"
        elif i=="x":
            resul="x"
        elif i=="-":
            resul="-"
    return resul
#esta funcion agarra los valoresde la matriz y ve que si operados dan el numero#
def comprobar3(resultados,lugar,numero,oper,board):
    global error,error2
    if oper=="-":
        final=0
        for i in resultados:
            final-=int(i)
            final=abs(final)
        if int(final)==int(numero):
            None
        else:
            error=1
    
    elif oper=="+":
        final=0
        for i in resultados:
            final+=i
        if int(final)==int(numero):
            None
        else:
            error=1
        
    elif oper=="x":
        final=1
        
        for i in resultados:
            final*=i
        
        if int(final)==int(numero):
            None
        else:
            
            error=1
            
        
    elif oper=="/":
        if 0 in resultados:
            error=1
        else:
            final=0
        
            for i in resultados:
                if final==0:
                    final+=int(i)
                else:
                    final/=int(i)
            
            if final==int(numero):
                None
            else:
                error=1
    elif oper=="#":
        final=0
        i=lugar[0][0]
        j=lugar[0][1]
        final=board[i][j]
        if int(final)==int(numero):
            None
        else:
            error=1
#funcion para saber si la matriz esta llena en caso de encontrar un 0 retorna False#
def isFull3(board) :
    for x in range(0, 3):
        for y in range (0, 3):
            if board[x][y] == 0:
                return False
    return True
    
# Función para encontrar todos los números posibles

def possibleEntries3(board, i, j):
    #creo diccionario para guardar posibles#
    possibilityArray = {}
    
    for x in range (1, 4):
        possibilityArray[x] = 0
    
    #sirve para los valores horizontales
    for y in range (0, 3):
        if not board[i][y] == 0: 
            possibilityArray[board[i][y]] = 1
     
    #sirve para los valores verticales
    for x in range (0, 3):
        if not board[x][j] == 0: 
            possibilityArray[board[x][j]] = 1
            
       
    
    for x in range (1, 4):
        if possibilityArray[x] == 0:
            possibilityArray[x] = x
        else:
            possibilityArray[x] = 0
    
    return possibilityArray

#funcion solo para imprimir la matriz#
def printBoard3(board):
    print(board)
#funcion principal, en la cual se comprueba si la matriz esta llena y es la correcta#    
def sudokuSolver3(board):
    global matriz,boton
    
    i = 0
    j = 0
    
    possiblities = {}
    
    # si la mtriz esta llena y es la correcta pues es la que se pone en los botones
    if isFull3(board) and es_correcto3(board):
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                matriz[i][j]=board[i][j]
                boton[i][j].config(text=str(board[i][j]))
        return
    else:
        # encunentra la primer posicion que este en 0
        for x in range (0, 3):
            for y in range (0, 3):
                if board[x][y] == 0:
                    i = x
                    j = y
                    break
            else:
                continue
            break
        
        # obtine todos los i,j que pueda tener lamatriz
        possiblities = possibleEntries3(board, i, j)
        
        #pasa por toda la funcion y llena la matriz una y otra vez
        for x in range (1, 4):
            if not possiblities[x] == 0:
                board[i][j] = possiblities[x]
                
                sudokuSolver3(board)
        # backtraking: lo devuelve a 0 en caso de no prometer
        board[i][j] = 0
#funcion para llamara todos los demas, la matriz se creade esta forma porque deotra manera no agarraba los valores#
def main3():
    global SudokuBoard
    SudokuBoard = [[0 for x in range(3)] for x in range(3)] 
    SudokuBoard[0][0] = 0
    SudokuBoard[0][1] = 0
    SudokuBoard[0][2] = 0

    SudokuBoard[1][0] = 0
    SudokuBoard[1][1] = 0
    SudokuBoard[1][2] = 0
   
    SudokuBoard[2][0] = 0
    SudokuBoard[2][1] = 0
    SudokuBoard[2][2] = 0


    #llamo a la funcion#
    sudokuSolver3(SudokuBoard)

    

#################3
#backtraking4
#esta funcion tiene los mismo conceptos de la 3 por eso no se comenta
####################33

def es_correcto4(board):
    global error,matriz
    
    inicio_de_validacion4(board)
    
    
    
    if error ==1:
        error=0
        return False
    elif error==0:
        return True
def inicio_de_validacion4(board):
    global actual
    a=actual
    for i in a.values():
        validar_de_verdad4(i,board)
    return
#agrara un elemento del diccionario y separa el operador del numero, tambien agarra los valores de la matriz en la tuple de la llave#
def validar_de_verdad4(i,board):
        opera=""
        numero=""
        resul=[]
        lugar=[]
        for j in i:
            if type(j)==str:
                if operador4(j)!="":
                    opera=operador4(j)
                    numero=obtener_numero4(j)
                else:
                    opera="#"
                    numero=obtener_numero4(j)
            elif type(j)==tuple:
                lugar+=[j]
                resul+=[board[j[0]][j[1]]]
            
        resul.sort(reverse=True)
        return comprobar4(resul,lugar,numero,opera,board)

#obtiene el numero de in string#
def obtener_numero4(string):
    resul=""
    for j in string:
        if j=="0" or j=="1" or j=="2" or j=="3" or j=="4" or j=="5" or j=="6" or j=="7" or j=="8" or j=="9":
            resul+=j
    return resul
    
                
            

#saca el operador de un string#    
def operador4(string):
    resul=""
    for i in string:
        if i=="+":
            resul="+"
        elif i=="/":
            resul="/"
        elif i=="x":
            resul="x"
        elif i=="-":
            resul="-"
    return resul
#esta funcion agarra los valoresde la matriz y ve que si operados dan el numero#
def comprobar4(resultados,lugar,numero,oper,board):
    global error,error2
    if oper=="-":
        final=0
        for i in resultados:
            final-=int(i)
            final=abs(final)
        if int(final)==int(numero):
            None
        else:
            error=1
    
    elif oper=="+":
        final=0
        for i in resultados:
            final+=i
        if int(final)==int(numero):
            None
        else:
            error=1
        
    elif oper=="x":
        final=1
        
        for i in resultados:
            final*=i
        
        if int(final)==int(numero):
            None
        else:
            
            error=1
            
        
    elif oper=="/":
        if 0 in resultados:
            error=1
        else:
            final=0
        
            for i in resultados:
                if final==0:
                    final+=int(i)
                else:
                    final/=int(i)
            
            if final==int(numero):
                None
            else:
                error=1
    elif oper=="#":
        final=0
        i=lugar[0][0]
        j=lugar[0][1]
        final=board[i][j]
        if int(final)==int(numero):
            None
        else:
            error=1
                
def isFull4(board) :
    for x in range(0, 4):
        for y in range (0, 4):
            if board[x][y] == 0:
                return False
    return True
    

def possibleEntries4(board, i, j):
    
    possibilityArray = {}
    
    for x in range (1, 5):
        possibilityArray[x] = 0
    
    for y in range (0, 4):
        if not board[i][y] == 0: 
            possibilityArray[board[i][y]] = 1
     
    
    for x in range (0, 4):
        if not board[x][j] == 0: 
            possibilityArray[board[x][j]] = 1
            
       
    
    for x in range (1, 5):
        if possibilityArray[x] == 0:
            possibilityArray[x] = x
        else:
            possibilityArray[x] = 0
    
    return possibilityArray


def printBoard4(board):
    print(board)
def sudokuSolver4(board):
    global matriz,boton
    
    i = 0
    j = 0
    
    possiblities = {}
    
    
    if isFull4(board) and es_correcto4(board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                matriz[i][j]=board[i][j]
                boton[i][j].config(text=str(board[i][j]))
        return
    else:
        
        for x in range (0, 4):
            for y in range (0, 4):
                if board[x][y] == 0:
                    i = x
                    j = y
                    break
            else:
                continue
            break
        
        
        possiblities = possibleEntries4(board, i, j)
        
        for x in range (1, 5):
            if not possiblities[x] == 0:
                board[i][j] = possiblities[x]                
                sudokuSolver4(board)
        board[i][j] = 0

def main4():
    global SudokuBoard
    SudokuBoard = [[0 for x in range(4)] for x in range(4)] 
    SudokuBoard[0][0] = 0
    SudokuBoard[0][1] = 0
    SudokuBoard[0][2] = 0
    SudokuBoard[0][3] = 0

    SudokuBoard[1][0] = 0
    SudokuBoard[1][1] = 0
    SudokuBoard[1][2] = 0
    SudokuBoard[1][3] = 0

    SudokuBoard[2][0] = 0
    SudokuBoard[2][1] = 0
    SudokuBoard[2][2] = 0
    SudokuBoard[2][3] = 0

    SudokuBoard[3][0] = 0
    SudokuBoard[3][1] = 0
    SudokuBoard[3][2] = 0
    SudokuBoard[3][3] = 0



    #printBoard(SudokuBoard)
    sudokuSolver4(SudokuBoard)
    #file.close()

############################
#backtracking para 5
def es_correcto5(board):
    global error,matriz
    
    inicio_de_validacion5(board)
    
    
    
    if error ==1:
        error=0
        return False
    elif error==0:
        return True
def inicio_de_validacion5(board):
    global actual
    a=actual
    for i in a.values():
        validar_de_verdad5(i,board)
    return
#agrara un elemento del diccionario y separa el operador del numero, tambien agarra los valores de la matriz en la tuple de la llave#
def validar_de_verdad5(i,board):
        opera=""
        numero=""
        resul=[]
        lugar=[]
        for j in i:
            if type(j)==str:
                if operador5(j)!="":
                    opera=operador5(j)
                    numero=obtener_numero5(j)
                else:
                    opera="#"
                    numero=obtener_numero5(j)
            elif type(j)==tuple:
                lugar+=[j]
                resul+=[board[j[0]][j[1]]]
            
        resul.sort(reverse=True)
        return comprobar5(resul,lugar,numero,opera,board)

#obtiene el numero de in string#
def obtener_numero5(string):
    resul=""
    for j in string:
        if j=="0" or j=="1" or j=="2" or j=="3" or j=="4" or j=="5" or j=="6" or j=="7" or j=="8" or j=="9":
            resul+=j
    return resul
    
                
            

#saca el operador de un string#    
def operador5(string):
    resul=""
    for i in string:
        if i=="+":
            resul="+"
        elif i=="/":
            resul="/"
        elif i=="x":
            resul="x"
        elif i=="-":
            resul="-"
    return resul
#esta funcion agarra los valoresde la matriz y ve que si operados dan el numero#
def comprobar5(resultados,lugar,numero,oper,board):
    global error,error2
    if oper=="-":
        final=0
        for i in resultados:
            final-=int(i)
            final=abs(final)
        if int(final)==int(numero):
            None
        else:
            error=1
    
    elif oper=="+":
        final=0
        for i in resultados:
            final+=i
        if int(final)==int(numero):
            None
        else:
            error=1
        
    elif oper=="x":
        final=1
        
        for i in resultados:
            final*=i
        
        if int(final)==int(numero):
            None
        else:
            
            error=1
            
        
    elif oper=="/":
        if 0 in resultados:
            error=1
        else:
            final=0
        
            for i in resultados:
                if final==0:
                    final+=int(i)
                else:
                    final/=int(i)
            
            if final==int(numero):
                None
            else:
                error=1
    elif oper=="#":
        final=0
        i=lugar[0][0]
        j=lugar[0][1]
        final=board[i][j]
        if int(final)==int(numero):
            None
        else:
            error=1
                
def isFull5(board) :
    for x in range(0, 5):
        for y in range (0, 5):
            if board[x][y] == 0:
                return False
    return True
    

def possibleEntries5(board, i, j):
    
    possibilityArray = {}
    
    for x in range (1, 6):
        possibilityArray[x] = 0
    
    
    for y in range (0, 5):
        if not board[i][y] == 0: 
            possibilityArray[board[i][y]] = 1
     

    for x in range (0, 5):
        if not board[x][j] == 0: 
            possibilityArray[board[x][j]] = 1
            
       
    
    for x in range (1, 6):
        if possibilityArray[x] == 0:
            possibilityArray[x] = x
        else:
            possibilityArray[x] = 0
    
    return possibilityArray


def printBoard5(board):
    print(board)
def sudokuSolver5(board):
    global flag,matriz,boton
    if flag == True:
        return matriz
    
    i = 0
    j = 0
    
    possiblities = {}
    
    
    if isFull5(board) and es_correcto5(board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                matriz[i][j]=board[i][j]
                boton[i][j].config(text=str(board[i][j])) 

        
        flag = True
        return
    else:
      
        for x in range (0, 5):
            for y in range (0, 5):
                if board[x][y] == 0:
                    i = x
                    j = y
                    break
            else:
                continue
            break
        
       
        possiblities = possibleEntries5(board, i, j)
        
        
        for x in range (1, 6):
            if not possiblities[x] == 0:
                board[i][j] = possiblities[x]
                
                sudokuSolver5(board)
   
        board[i][j] = 0

def main5():
    global SudokuBoard
    SudokuBoard = [[0 for x in range(5)] for x in range(5)] 
    SudokuBoard[0][0] = 0
    SudokuBoard[0][1] = 0
    SudokuBoard[0][2] = 0
    SudokuBoard[0][3] = 0
    SudokuBoard[0][4] = 0

    SudokuBoard[1][0] = 0
    SudokuBoard[1][1] = 0
    SudokuBoard[1][2] = 0
    SudokuBoard[1][3] = 0
    SudokuBoard[1][4] = 0

    SudokuBoard[2][0] = 0
    SudokuBoard[2][1] = 0
    SudokuBoard[2][2] = 0
    SudokuBoard[2][3] = 0
    SudokuBoard[2][4] = 0

    SudokuBoard[3][0] = 0
    SudokuBoard[3][1] = 0
    SudokuBoard[3][2] = 0
    SudokuBoard[3][3] = 0
    SudokuBoard[3][4] = 0
    
    SudokuBoard[4][0] = 0
    SudokuBoard[4][1] = 0
    SudokuBoard[4][2] = 0
    SudokuBoard[4][3] = 0
    SudokuBoard[4][4] = 0



    sudokuSolver5(SudokuBoard)
 
##############################
#funcion para conextarnos al server#
def amigo1():
    #Creamos un objeto socket para el servidor. Podemos dejarlo sin parametros pero si 
    #quieren pueden pasarlos de la manera server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s = socket.socket()
     
    #Nos conectamos al servidor con el metodo connect. Tiene dos parametros
    #El primero es la IP del servidor y el segundo el puerto de conexion
    s.connect(("localhost", 9999))
     
    #Creamos un bucle para retener la conexion
    while True:
        #Instanciamos una entrada de datos para que el cliente pueda enviar mensajes
        mensaje = input("Mensaje a enviar >> ")
        print("Yo:",mensaje)
        #Con la instancia del objeto servidor (s) y el metodo send, enviamos el mensaje introducido
        s.send(mensaje.encode("utf-8"))
        mensaje=s.recv(1024).decode("utf-8")
        print("Amigo:",mensaje)
        #Si por alguna razon el mensaje es close cerramos la conexion
        if mensaje == "close":
            break
     
    #Imprimimos la palabra Adios para cuando se cierre la conexion
    print ("Adios.")
     
    #Cerramos la instancia del objeto servidor
    s.close()
##########################################
##########################################

            
                    
                
    
#elimina un elemento una tupla
def eliminar_elemento(ele,tupla):
    a=list(tupla)
    resultado=[]
    for i in a :
        if i != ele:
            resultado+=[i]
    resultado=tuple(resultado)        
    return resultado

#########################################
#########################################
#funcion que carga los archivos del nivel 3#
def lee3(): 
    res=[]
    f=open("nivel3.txt","r")
    for linea in f.readlines():
        palabra=""
        for i in linea:
            if i=="\n":
               res+=[eval(palabra)]
            else:
                palabra+=i
    f.close()
    if len(res)>10:
        res=res[:10]
    res=ordena_cargados2(res)
    return cambiar_a_hora(res,"Nivel 3 ")
#cambia a horas los segundos#
def cambiar_a_hora(res,nivel):
    for i in res:
        i[1]=hora(int(i[1]))
    return imprimir(res,nivel)
#ordenas los ddatoscargados#
def ordena_cargados2(lista): #Burbuja
    global top
    for i in range (1, len(lista)):
        for j in range (0, (len(lista) - i)):
            if lista[j][1] > lista [j+1][1]:
                Temp = lista [j+1]
                lista[j+1] = lista[j]
                lista[j] = Temp
    return lista
#escribe segun el nivel#
def imprimir(res,nivel):
    if res==[]:
        archivo=open("imprimir.txt","a")
        archivo.write(str(nivel)+" No hay jugadores en esta categoria ")
        archivo.write("\n")
        archivo.write("_________________________________________________________")
        archivo.write("\n")
        archivo.close()
    elif res!=[]:
        archivo=open("imprimir.txt","a")
        archivo.write(str(nivel))
        archivo.write("\n")
        for i in res:
            archivo.write(str(i[0])+" "+str(i[1]))
            archivo.write("\n")
        archivo.write("_________________________________________________________")
        archivo.write("\n")
        archivo.close()


#convierte los segundos en horas minu y segundos #
def hora(segundos):
    h=0
    m=0
    s=0
    h+=(segundos//3600)
    segundos=segundos%3600
    m+=(segundos//60)
    segundos=segundos%60
    s=segundos
    return (str(h)+str(":")+str(m)+str(":")+str(s))
#carga los datosdel nivel 4#
def lee4(): 
    res=[]
    f=open("nivel4.txt","r")
    for linea in f.readlines():
        palabra=""
        for i in linea:
            if i=="\n":
               res+=[eval(palabra)]
            else:
                palabra+=i
    f.close()
    if len(res)>10:
        res=res[:10]
    res=ordena_cargados2(res)
    return cambiar_a_hora(res,"Nivel 4 ")
#carga los datosdel nivel 5#
def lee5(): 
    res=[]
    f=open("nivel5.txt","r")
    for linea in f.readlines():
        palabra=""
        for i in linea:
            if i=="\n":
               res+=[eval(palabra)]
            else:
                palabra+=i
    f.close()
    if len(res)>10:
        res=res[:10]
    res=ordena_cargados2(res)
    return cambiar_a_hora(res,"Nivel 5 ")
#carga los datosdel nivel 6#

def lee6(): 
    res=[]
    f=open("nivel6.txt","r")
    for linea in f.readlines():
        palabra=""
        for i in linea:
            if i=="\n":
               res+=[eval(palabra)]
            else:
                palabra+=i
    f.close()
    if len(res)>10:
        res=res[:10]
    res=ordena_cargados2(res)
    return cambiar_a_hora(res,"Nivel 6 ")
#carga los datosdel nivel 7#
def lee7(): 
    res=[]
    f=open("nivel7.txt","r")
    for linea in f.readlines():
        palabra=""
        for i in linea:
            if i=="\n":
               res+=[eval(palabra)]
            else:
                palabra+=i
    f.close()
    if len(res)>10:
        res=res[:10]
    res=ordena_cargados2(res)
    return cambiar_a_hora(res,"Nivel 7 ")
#carga los datosdel nivel 8#
def lee8(): 
    res=[]
    f=open("nivel8.txt","r")
    for linea in f.readlines():
        palabra=""
        for i in linea:
            if i=="\n":
               res+=[eval(palabra)]
            else:
                palabra+=i
    f.close()
    if len(res)>10:
        res=res[:10]
    res=ordena_cargados2(res)
    return cambiar_a_hora(res,"Nivel 8 ")
#carga los datosdel nivel 9#
def lee9(): 
    res=[]
    f=open("nivel9.txt","r")
    for linea in f.readlines():
        palabra=""
        for i in linea:
            if i=="\n":
               res+=[eval(palabra)]
            else:
                palabra+=i
    f.close()
    if len(res)>10:
        res=res[:10]
    res=ordena_cargados2(res)
    return cambiar_a_hora(res,"Nivel 9 ")

def imprim():
    lee3()
    lee4()
    lee5()
    lee6()
    lee7()
    lee8()
    lee9()
#funcion para iniciar los valores antes de jugar#
def asignacion():
    global boton,juego2,matriz,segundos,actual,usado,filas,posicion,ancho,largo,posibles
    if len(usado)>1:
        actual=usado[0]
        ancho=posibles[0][1][0]
        largo=posibles[0][1][1]
        filas=posibles[0][0]
        todo_a_seg()
        crear_matriz_logica()
        crear_matriz_botones()
        crear_matriz_juego()
        matriz_con_color(actual)
        usado=usado[1:]
        posibles=posibles[1:]
        pantalla()
    elif len(usado)==1:
        actual=usado[0]
        ancho=posibles[0][1][0]
        largo=posibles[0][1][1]
        filas=posibles[0][0]
        todo_a_seg()
        crear_matriz_logica()
        crear_matriz_botones()
        crear_matriz_juego()
        matriz_con_color(actual)
        usado=usado[1:]
        posibles=posibles[1:]
        pantalla()
        messagebox.showinfo("Ultimo Nivel","Estas a punto de lograrlo, Suerte.")
    else:
        messagebox.showinfo("Ultimo Nivel","Estas a punto de lograrlo, haz ganado.")
        main()
        
#funcion que me agrega un juegode cada nivel a la lsta de usados#
def nuevo_usado():
    global nivel13,nivel14,nivel5,nivel6,nivel7,nivel8,nivel9,usado,posibles
    if nivel3!=[]:
        usado+=[nivel3[0]]
        posibles+=[[3,(10,5)]]
    elif nivel!=[]:
        pass
    if nivel4!=[]:
        usado+=[nivel4[0]]
        posibles+=[[4,(8,5)]]
    elif nivel4!=[]:
        pass
    if nivel5!=[]:
        usado+=[nivel5[0]]
        posibles+=[[5,(7,4)]]
    elif nivel5!=[]:
        pass
    if nivel6!=[]:
        usado+=[nivel6[0]]
        posibles+=[[6,(6,3)]]
    elif nivel6!=[]:
        pass
    if nivel7!=[]:
        usado+=[nivel7[0]]
        posibles+=[[7,(4,2)]]
    elif nivel7!=[]:
        pass
    if nivel8!=[]:
        usado+=[nivel8[0]]
        posibles+=[[8,(3,2)]]
    elif nivel8!=[]:
        pass
    if nivel9!=[]:
        usado+=[nivel9[0]]
        posibles+=[[9,(3,2)]]
    elif nivel9!=[]:
        pass
    acomodo_rest()
    return
#guarda el top 10 del nivel3#
def crear_3():
    global nombre,segundos,tiempo_pasado,reloj
    print(reloj)
    print(tiempo_pasado)
    print(segundos)
    if reloj==1:
        archivo=open("nivel3.txt","a")
        archivo.write(str([nombre,segundos]))
        archivo.write("\n")
        archivo.close()
    elif reloj==3:
        a=int(segundos)-int(tiempo_pasado)
        archivo=open("nivel3.txt","a")
        archivo.write(str([nombre,a]))
        archivo.write("\n")
        archivo.close()
        
#guarda el top 10 del nivel4#
def crear_4():
    global nombre,segundos,tiempo_pasado,reloj
    if reloj==1:
        archivo=open("nivel4.txt","a")
        archivo.write(str([nombre,segundos]))
        archivo.write("\n")
        archivo.close()
    elif reloj==3:
        a=int(segundos)-int(tiempo_pasado)
        archivo=open("nivel4.txt","a")
        archivo.write(str([nombre,a]))
        archivo.write("\n")
        archivo.close()
#guarda el top 10 del nivel5#
def crear_5():
    global nombre,segundos,tiempo_pasado,reloj
    if reloj==1:
        archivo=open("nivel5.txt","a")
        archivo.write(str([nombre,segundos]))
        archivo.write("\n")
        archivo.close()
    elif reloj==3:
        a=int(segundos)-int(tiempo_pasado)
        archivo=open("nivel5.txt","a")
        archivo.write(str([nombre,a]))
        archivo.write("\n")
        archivo.close()
#guarda el top 10 del nivel6#
def crear_6():
    global nombre,segundos,tiempo_pasado,reloj
    if reloj==1:
        archivo=open("nivel6.txt","a")
        archivo.write(str([nombre,segundos]))
        archivo.write("\n")
        archivo.close()
    elif reloj==3:
        a=int(segundos)-int(tiempo_pasado)
        archivo=open("nivel6.txt","a")
        archivo.write(str([nombre,a]))
        archivo.write("\n")
        archivo.close()
#guarda el top 10 del nivel7#
def crear_7():
    global nombre,segundos
    global nombre,segundos,tiempo_pasado,reloj
    if reloj==1:
        archivo=open("nivel7.txt","a")
        archivo.write(str([nombre,segundos]))
        archivo.write("\n")
        archivo.close()
    elif reloj==3:
        a=int(segundos)-int(tiempo_pasado)
        archivo=open("nivel7.txt","a")
        archivo.write(str([nombre,a]))
        archivo.write("\n")
        archivo.close()
#guarda el top 10 del nivel8#
def crear_8():
    global nombre,segundos,tiempo_pasado,reloj
    if reloj==1:
        archivo=open("nivel8.txt","a")
        archivo.write(str([nombre,segundos]))
        archivo.write("\n")
        archivo.close()
    elif reloj==3:
        a=int(segundos)-int(tiempo_pasado)
        archivo=open("nivel8.txt","a")
        archivo.write(str([nombre,a]))
        archivo.write("\n")
        archivo.close()
#guarda el top 10 del nivel9#
def crear_9():
    global nombre,segundos,tiempo_pasado,reloj
    if reloj==1:
        archivo=open("nivel9.txt","a")
        archivo.write(str([nombre,segundos]))
        archivo.write("\n")
        archivo.close()
    elif reloj==3:
        a=int(segundos)-int(tiempo_pasado)
        archivo=open("nivel9.txt","a")
        archivo.write(str([nombre,a]))
        archivo.write("\n")
        archivo.close()

######################################
#agarra un diccionario y lo pasa a validar#
def inicio_de_validacion():
    global actual
    a=actual
    for i in a.values():
        validar_de_verdad(i)
    return
#agrara un elemento del diccionario y separa el operador del numero, tambien agarra los valores de la matriz en la tuple de la llave#
def validar_de_verdad(i):
        opera=""
        numero=""
        resul=[]
        lugar=[]
        for j in i:
            if type(j)==str:
                if operador(j)!="":
                    opera=operador(j)
                    numero=obtener_numero(j)
                else:
                    opera="#"
                    numero=obtener_numero(j)
            elif type(j)==tuple:
                lugar+=[j]
                resul+=[matriz[j[0]][j[1]]]
            
        resul.sort(reverse=True)
        return comprobar(resul,lugar,numero,opera)

#obtiene el numero de in string#
def obtener_numero(string):
    resul=""
    for j in string:
        if j=="0" or j=="1" or j=="2" or j=="3" or j=="4" or j=="5" or j=="6" or j=="7" or j=="8" or j=="9":
            resul+=j
    return resul
    
                
            

#saca el operador de un string#    
def operador(string):
    resul=""
    for i in string:
        if i=="+":
            resul="+"
        elif i=="/":
            resul="/"
        elif i=="x":
            resul="x"
        elif i=="-":
            resul="-"
    return resul
#esta funcion agarra los valoresde la matriz y ve que si operados dan el numero#
def comprobar(resultados,lugar,numero,oper):
    
    global boton,error
    error=0
    print("entre")
    print(oper)
    print(resultados)
    print(lugar)
    if oper=="-":
        final=0
        for i in resultados:
            if final==0:
                final+=i
            else:
                final-=i
        if int(final)==int(numero):
            None
        else:
            error=1
            for i in lugar:

                boton[i[0]][i[1]].config(bg="red")
                print("soyF",final)
    elif oper=="+":
        final=0
        for i in resultados:
            if final==0:
                final+=i
            else:
                final+=i
        if int(final)==int(numero):
            None
        else:
            error=1
            for i in lugar:
                print("soyF",final)

                boton[i[0]][i[1]].config(bg="red")
    elif oper=="x":
        final=1
        for i in resultados:
            if final==1:
                final*=i
            else:
                final*=i
        if int(final)==int(numero):
            None
        else:
            error=1
            for i in lugar:
                print("soyF",final)
                boton[i[0]][i[1]].config(bg="red")
    elif oper=="/":
        final=0
        for i in resultados:
            if final==0:
                final+=i
            else:
                final//=i
        if int(final)==int(numero):
            None
        else:
            error=1
            for i in lugar:
                print("soyF",final)

                boton[i[0]][i[1]].config(bg="red")
    elif oper=="#":
        final=int(numero)
        print(final)
        if int(final)==int(numero):
            None
        else:
            error=1
            for i in lugar:
                boton[i[0]][i[1]].config(bg="red")

########################################
#genera un ramdom con los jegos de un nivel#
def generar_random():
    global usado,actual,ya_usados
    actual=random.choice(usado)
    if actual not in ya_usados:
        ya_usados+=[actual]
    elif actual in ya_usados:
        a=random.choice(usado)
    elif len(ya_usados)==len(usado):
        ya_usados=[]
        ya_usados+=[actual]
#agarra y crea una matriz con el color y el texto que va a tener#
def matriz_con_color(dicci):
    d=dicci
    global juego2
    resultado=[]
    colores=["blue","green","olive","yellow","orange","pink","purple","lime","violet","aqua","teal","brown","ivory","navy","gray"]
    for i in d.values():
        a=random.choice(colores)
        if a not in resultado:
            resultado+=[a]
        elif a in resultado:
            a=random.choice(colores)
        elif len(resultado)==len(colores):
            resultado=[]
            resultado+=[a]
            
        texto=""
        for j in i:
            if type(j)==str:
                texto=j
            elif type(j)==tuple:
                juego2[j[0]][j[1]]=[texto,a]
    return
#carga los juegos en el archivo kenken_configuracion#
def lee(): 
    res=[]
    f=open("kenken_configuración.dat","w")
    f.close()
    f=open("kenken_configuración.dat","r")
    for linea in f.readlines():
        palabra=""
        for i in linea:
            if i=="\n":
               res+=[eval(palabra)]
            else:
                palabra+=i
    f.close()
    return acomodar(res)
##
def acomodar(res):
    for i in res:
        mayor(i)
    return res
#acomoda los valores enlos nivel correctos#
def mayor(dicci):
    global nivel3,nivel4,nivel5,nivel6,nivel7,nivel8,nivel9
    d=dicci
    cont=0
    for i in d.values():
        for j in i:
            if type(j)==tuple and max(j)> cont:
                cont=max(j)
    if cont==3:
        nivel3+=[d]
    elif cont==4:
        nivel4+=[d]
    elif cont==5:
        nivel5+=[d]
    elif cont==6:
        nivel6+=[d]
    elif cont==7:
        nivel7+=[d]
    elif cont==8:
        nivel8+=[d]
    elif cont==9:
        nivel9+=[d]
    return
#toma los elemntos en la lista y losmanda a resta#
def acomodo_rest():
    global usado
    for i in usado:
        restar(i)
#le resta un vslor a ls elementos de la tupla para que puedan encajar en la matriz#
def restar(dicci):
    d=dicci
    for i in d.keys():
        resultado=[]
        for j in d[i]:
            if type(j)==str:
                resultado+=[j]
            elif type(j)==tuple:
                a=list(j)
                a[0]-=1
                a[1]-=1
                j=tuple(a)
                resultado+=[j]
        d[i]= tuple(resultado)
    return d
#convierte los datos introducidos a segundos#
def todo_a_seg():
    global horas,segundos,minutos
    cont=0
    cont+=(horas*3600)
    cont+=(minutos*60)
    cont+=segundos
    segundos=cont
    return cont
#pasa de segundos a horas
def hora(segundos):
    h=0
    m=0
    s=0
    h+=(segundos//3600)
    segundos=segundos%3600
    m+=(segundos//60)
    segundos=segundos%60
    s=segundos
    return (str(h)+str(":")+str(m)+str(":")+str(s))
#crea el tiempo predeterminado a las partidas#
def crear_tiempo():
    
        global filas,segundos,reloj
        if reloj==3 and filas==3:
            segundos=300
        elif reloj==3 and filas==4:
            segundos=900
        elif reloj==3 and filas==5:
            segundos=1200
        elif reloj==3 and filas==6:
            segundos=1800
        elif reloj==3 and filas==7:
            segundos=2400
        elif reloj==3 and filas==8:
            segundos=3000
        elif reloj==3 and filas==9:
            segundos=3600
#funcion para seleccionar un nivel#
def nivel_seleccionado():
    lee()
    global filas
    nivel=Tk()
    nivel.geometry("450x400")
    nivel.title("Seleccione el Nivel")
    nivel.config(bg="white")
    label=Label(nivel,text="Selecione un nivel.",font="Arial 14",bg="white").place(x=0,y=0)
    num=IntVar()
    X3=Radiobutton(nivel,text="3x3",value=3,variable=num,font="Arial 14",bg="white").place(x=170,y=20)
    X4=Radiobutton(nivel,text="4x4",value=4,variable=num,font="Arial 14",bg="white").place(x=170,y=60)
    X5=Radiobutton(nivel,text="5x5",value=5,variable=num,font="Arial 14",bg="white").place(x=170,y=100)
    X6=Radiobutton(nivel,text="6x6",value=6,variable=num,font="Arial 14",bg="white").place(x=170,y=140)
    X7=Radiobutton(nivel,text="7x7",value=7,variable=num,font="Arial 14",bg="white").place(x=170,y=180)
    X8=Radiobutton(nivel,text="8x8",value=8,variable=num,font="Arial 14",bg="white").place(x=170,y=220)
    X9=Radiobutton(nivel,text="9x9",value=9,variable=num,font="Arial 14",bg="white").place(x=170,y=260)
    X10=Radiobutton(nivel,text="Multinivel",value=10,variable=num,font="Arial 14",bg="white").place(x=170,y=300)
    
    def valor():
        global filas,ancho,largo,nivel3,usado,nivel4,nivel5,nivel6,nivel7,nivel8,nivel9
        numero=num.get()
        if numero==3 and nivel3!=[]:
            filas=3
            ancho=10
            largo=5
            usado=nivel3
            acomodo_rest()
            generar_random()
            nivel.destroy()
            activar_reloj()
        elif numero==3 and nivel3==[]:
            messagebox.showerror("Verifique los datos","No hay juegos en este nivel.")
            return
        
        elif numero==4 and nivel4!=[]:
            filas=4
            ancho=8
            largo=5
            usado=nivel4
            acomodo_rest()
            generar_random()
            nivel.destroy()
            activar_reloj()
        elif numero==4 and nivel4==[]:
            messagebox.showerror("Verifique los datos","No hay juegos en este nivel.")
            return
            
        elif numero==5 and nivel5!=[]:
            filas=5
            ancho=7
            largo=4
            usado=nivel5
            acomodo_rest()
            generar_random()
            nivel.destroy()
            activar_reloj()
        elif numero==5 and nivel5==[]:
            messagebox.showerror("Verifique los datos","No hay juegos en este nivel.")
            return
        elif numero==6 and nivel6!=[]:
            filas=6
            ancho=5
            largo=3
            usado=nivel6
            acomodo_rest()
            generar_random()
            nivel.destroy()
            activar_reloj()
        elif numero==6 and nivel6==[]:
            messagebox.showerror("Verifique los datos","No hay juegos en este nivel.")
            return
        elif numero==7 and nivel7!=[]:
            filas=7
            ancho=4
            largo=2
            usado=nivel7
            acomodo_rest()
            generar_random()
            nivel.destroy()
            activar_reloj()
        elif numero==7 and nivel7==[]:
            messagebox.showerror("Verifique los datos","No hay juegos en este nivel.")
            return
        elif numero==8 and nivel8!=[]:
            filas=8
            ancho=3
            largo=2
            usado=nivel8
            acomodo_rest()
            generar_random()
            nivel.destroy()
            activar_reloj()
        elif numero==8 and nivel8==[]:
            messagebox.showerror("Verifique los datos","No hay juegos en este nivel.")
            return
        elif numero==9 and nivel9!=[]:
            filas=9
            ancho=3
            largo=2
            usado=nivel9
            acomodo_rest()
            generar_random()
            nivel.destroy()
            activar_reloj()
        elif numero==9 and nivel9==[]:
            messagebox.showerror("Verifique los datos","No hay juegos en este nivel.")
            return
        elif numero==10:
            global activar_sobrevivir
            activar_sobrevivir=1
            nivel.destroy()
            activar_reloj()
        elif numero==9 and nivel9==[]:
            messagebox.showerror("Verifique los datos","No hay juegos en este nivel.")
            return
            
    def continuar():
        numero=num.get()
        if numero !=0:
            valor()
        elif numero ==0:
            messagebox.showerror("Verifique los datos","Debe seleccionar una opcion.")
        
    buton=Button(nivel,text="Continuar",font="Arial 16",bg="green",command=continuar).place(x=150,y=350)
    nivel.mainloop()
#funcion para wditar el tiempo de una partida#
def nuevo_tiempo():
    nuevo=Tk()
    nuevo.geometry("400x250")
    nuevo.config(bg="white")
    hora=Label(nuevo,text="horas",bg="white").place(x=100,y=20)
    X1=Entry(nuevo,bg="red",fg="black")
    X1.place(x=140,y=20)
    hora=Label(nuevo,text="Minutos",bg="white").place(x=80,y=40)
    X2=Entry(nuevo,bg="red",fg="black")
    X2.place(x=140,y=40)
    hora=Label(nuevo,text="Segundos",bg="white").place(x=80,y=60)
    X3=Entry(nuevo,bg="red",fg="black")
    X3.place(x=140,y=60)
    
   
    hora=Label(nuevo,text="Segundos",bg="white").place(x=80,y=60)
    
    def continuar():
        global segundos,minutos,horas
        horas=int(X1.get())
        minutos=int(X2.get())
        segundos=int((X3.get()))
        nuevo.destroy()
        posicion_botones()      
    buton=Button(nuevo,text="Continuar",font="Arial 16",bg="green",command=continuar).place(x=150,y=120)
    nuevo.mainloop()
#funcion en caso de querer modificar el tiempo predeterminado#
def decidir_tiempo():
    deci=Tk()
    deci.geometry("400x250")
    deci.title("Confugurar Timer")
    deci.config(bg="white")
    ele=IntVar()
    label=Label(deci,text="Decidir.",font="Arial 14",bg="white").place(x=0,y=0)
    X3=Radiobutton(deci,text="Predeterminado",value=1,variable=ele,font="Arial 14",bg="white").place(x=100,y=40)
    X4=Radiobutton(deci,text="Nuevo Valor",value=2,variable=ele,font="Arial 14",bg="white").place(x=100,y=80)
    def continuar():
        global activar_sobrevivir,segundos
        numero=ele.get()
        if numero==0:
            messagebox.showerror("Error","Debe seleccionsr uns opcion")
        elif numero ==1 and activar_sobrevivir==1:
            segundos=7200
            deci.destroy()
            posicion_botones()
        elif numero ==1 and activar_sobrevivir==0:
            crear_tiempo()
            deci.destroy()
            posicion_botones()
        elif  numero ==2:
            deci.destroy()
            nuevo_tiempo()

    buton=Button(deci,text="Continuar",font="Arial 16",bg="green",command=continuar).place(x=150,y=170)
    deci.mainloop()
#funcion para saber si va a haber reloj o timer#
def activar_reloj():
    activado=Tk()
    activado.geometry("400x250")
    activado.title("Activar Reloj")
    activado.config(bg="white")
    label=Label(activado,text="Tiempo.",font="Arial 14",bg="white").place(x=0,y=0)
    var=IntVar()
    X3=Radiobutton(activado,text="Si",value=1,variable=var,font="Arial 14",bg="white").place(x=170,y=20)
    X4=Radiobutton(activado,text="No",value=2,variable=var,font="Arial 14",bg="white").place(x=170,y=60)
    X5=Radiobutton(activado,text="Timer",value=3,variable=var,font="Arial 14",bg="white").place(x=170,y=100)
    def valor():
        global filas,segundos,reloj,activar_sobrevivir,segundos
        numero=var.get()
        if numero==1:
            reloj=1
        elif numero==2:
            reloj=2
        elif numero==3:
            reloj=3
    def continuar():
        numero=var.get()
        if(numero ==1 or numero==2):
            valor()
            activado.destroy()
            posicion_botones()
        elif  numero ==3:
            valor()
            
            activado.destroy()
            decidir_tiempo()
        elif numero ==0:
            messagebox.showerror("Verifique los datos","Debe seleccionar una opcion.")
    buton=Button(activado,text="Continuar",font="Arial 16",bg="green",command=continuar).place(x=150,y=170)
    activado.mainloop()


    
#funcion para saber la posicion en que vana ir los botones#
def posicion_botones():
    pos=Tk()
    pos.geometry("400x250")
    pos.title("Seleccionar Posicion de botones")
    pos.config(bg="white")
    ele=IntVar()
    label=Label(pos,text="Posicion de numeros y borrador.",font="Arial 14",bg="white").place(x=0,y=0)
    X3=Radiobutton(pos,text="Derecha",value=1,variable=ele,font="Arial 14",bg="white").place(x=170,y=40)
    X4=Radiobutton(pos,text="Izquierda",value=2,variable=ele,font="Arial 14",bg="white").place(x=170,y=80)
    def valor():
        numero=ele.get()
        global posicion
        if numero==1:
            posicion=1
        elif numero==2:
            posicion=2
    def continuar():
        numero=ele.get()
        if  numero !=0:
            valor()
            pos.destroy()
            activar_volumen()
            
        elif numero ==0:
            messagebox.showerror("Verifique los datos","Debe seleccionar una opcion.")
    buton=Button(pos,text="Continuar",font="Arial 16",bg="green",command=continuar).place(x=150,y=170)
    pos.mainloop()
#funcion para activar sonido#
def activar_volumen():
    song=Tk()
    song.geometry("400x250")
    song.title("Seleccionar Posicion de botones")
    song.config(bg="white")
    vol=IntVar()
    label=Label(song,text="Sonido al terminar.",font="Arial 14",bg="white").place(x=0,y=0)
    X3=Radiobutton(song,text="Si",value=1,variable=vol,font="Arial 14",bg="white").place(x=170,y=30)
    X4=Radiobutton(song,text="No",value=2,variable=vol,font="Arial 14",bg="white").place(x=170,y=70)
    def valor():
        numero=vol.get()
        global sonido
        if numero==1:
            sonido=1
        elif numero==2:
            sonido=2
    def continuar():
        numero=vol.get()
        if numero !=0:
            valor()
            song.destroy()
            player_name()
        elif numero ==0:
            messagebox.showerror("Verifique los datos","Debe seleccionar una opcion.")
    buton=Button(song,text="Continuar",font="Arial 16",bg="green",command=continuar).place(x=150,y=170)
    song.mainloop()

    
#funcion que pide el nombre del jugador#
def player_name():
    name=Tk()
    name.geometry("400x250")
    name.config(bg="white")
    na=Label(name,text="Nombre",bg="white",font="Arial 12").place(x=160,y=40)
    X1=Entry(name,bg="red",fg="black")
    X1.place(x=140,y=20)
    def continuar():
        global nombre,activar_sobrevivir
        if activar_sobrevivir==0:
            nombre=X1.get()
            name.destroy()
            crear_matriz_logica()
            crear_matriz_botones()
            crear_matriz_juego()
            matriz_con_color(actual)
            pantalla()
        elif activar_sobrevivir==1:
            nombre=X1.get()
            name.destroy()
            nuevo_usado()
            asignacion()
            
            
    buton=Button(name,text="Continuar",font="Arial 16",bg="green",command=continuar).place(x=150,y=120)
    name.mainloop()
#crea la matriz logica#   
def crear_matriz_logica():
    global matriz
    for i in range(filas):
        matriz.append([0]*filas)
    return
#crea la matriz de botnoes#
def crear_matriz_botones():
    global boton,filas
    for i in range(filas):
        boton.append([0]*filas)
    return
#crea la matriz del juego#
def crear_matriz_juego():
    global juego2,filas
    for i in range(filas):
       juego2.append([0]*filas)

#############################################################
    #todas la funciones cargarn() sirven para cargar el top10 de cada nivel
########################################################
def cargar3():
    res=[]
    f=open("nivel3.txt","r")
    for linea in f.readlines():
        palabra=""
        for i in linea:
            if i=="\n":
               res+=[eval(palabra)]
            else:
                palabra+=i
    f.close()
    return ordena_cargados(res)

def cargar4():
    res=[]
    f=open("nivel4.txt","r")
    for linea in f.readlines():
        palabra=""
        for i in linea:
            if i=="\n":
               res+=[eval(palabra)]
            else:
                palabra+=i
    f.close()
    return ordena_cargados(res)

def cargar5():
    res=[]
    f=open("nivel5.txt","r")
    for linea in f.readlines():
        palabra=""
        for i in linea:
            if i=="\n":
               res+=[eval(palabra)]
            else:
                palabra+=i
    f.close()
    return ordena_cargados(res)

def cargar6():
    res=[]
    f=open("nivel6.txt","r")
    for linea in f.readlines():
        palabra=""
        for i in linea:
            if i=="\n":
               res+=[eval(palabra)]
            else:
                palabra+=i
    f.close()
    return ordena_cargados(res)

def cargar7():
    res=[]
    f=open("nivel7.txt","r")
    for linea in f.readlines():
        palabra=""
        for i in linea:
            if i=="\n":
               res+=[eval(palabra)]
            else:
                palabra+=i
    f.close()
    return ordena_cargados(res)

def cargar8():
    res=[]
    f=open("nivel8.txt","r")
    for linea in f.readlines():
        palabra=""
        for i in linea:
            if i=="\n":
               res+=[eval(palabra)]
            else:
                palabra+=i
    f.close()
    return ordena_cargados(res)

def cargar9():
    res=[]
    f=open("nivel9.txt","r")
    for linea in f.readlines():
        palabra=""
        for i in linea:
            if i=="\n":
               res+=[eval(palabra)]
            else:
                palabra+=i
    f.close()
    return ordena_cargados(res)
#ordena de mejor a peor los tiempos#
def ordena_cargados(lista): #Burbuja
    global top
    for i in range (1, len(lista)):
        for j in range (0, (len(lista) - i)):
            if lista[j][1] > lista [j+1][1]:
                Temp = lista [j+1]
                lista[j+1] = lista[j]
                lista[j] = Temp
    return lista_seleccionada(lista)
#ventana para seleccionar una categoria a verel top 10 #
def medallero():
    medalla=Tk()
    medalla.geometry("120x250")
    medalla.config(bg="white")
    medalla.title("Seleccione una categoria")
    def llamar_3():
        medalla.destroy()
        cargar3()
    def llamar_4():
        medalla.destroy()
        cargar4()
    def llamar_5():
        medalla.destroy()
        cargar5()
    def llamar_6():
        medalla.destroy()
        cargar6()
    def llamar_7():
        medalla.destroy()
        cargar7()
    def llamar_8():
        medalla.destroy()
        cargar8()
    def llamar_9():
        medalla.destroy()
        cargar9()
    def llamar():
        medalla.destroy()
        main()
    b1=Button(medalla,text="3x3",font="Cosmic 12",bg="yellow",command=llamar_3).place(x=10,y=10)
    b1=Button(medalla,text="4x4",font="Cosmic 12",bg="yellow",command=llamar_4).place(x=10,y=50)
    b1=Button(medalla,text="5x5",font="Cosmic 12",bg="yellow",command=llamar_5).place(x=10,y=90)
    b1=Button(medalla,text="6x6",font="Cosmic 12",bg="yellow",command=llamar_6).place(x=60,y=10)
    b1=Button(medalla,text="7x7",font="Cosmic 12",bg="yellow",command=llamar_7).place(x=60,y=50)
    b1=Button(medalla,text="8x8",font="Cosmic 12",bg="yellow",command=llamar_8).place(x=60,y=90)
    b1=Button(medalla,text="9x9",font="Cosmic 12",bg="yellow",command=llamar_9).place(x=30,y=130)
    b1=Button(medalla,text="Salir",font="Cosmic 12",bg="Red",command=llamar).place(x=30,y=170)
    medalla.mainloop()

#hace un listbox con los jugadores de esta categoria#
def lista_seleccionada(acomodo):
    
    select5= Tk()
    select5.geometry("395x200")
    select5.config(bg="black")
    scrollbar = Scrollbar(select5)
    scrollbar.pack( side = RIGHT, fill=Y )
    lista=Listbox(select5,yscrollcommand = scrollbar.set)
    
    lista = Listbox(selectmode=BROWSE)
    lista.config(width=62)
    if acomodo==[]:
        messagebox.showinfo("informacion", "No se ha registrado ningun juego en esta categoria")
    elif len(acomodo)>10:
        acomodo=acomodo[:10]
        for i in range(len(acomodo)):
            lista.insert(i,str(i+1)+"   "+str(acomodo[i][0])+ "   "+str(hora(acomodo[i][1])))
    else:
        for i in range(len(acomodo)):
            lista.insert(i,str(i+1)+"   "+str(acomodo[i][0])+ "   "+str(hora(acomodo[i][1])))
    def validar():
        select5.destroy()
        medallero()
    

    boton3=Button(select5,text="regresar",fg="Red",command=validar)
    boton3.place(x=0,y=170)
    lista.place(x=0,y=0)
    scrollbar.config( command = lista.yview )
    select5.mainloop()

#acerca de#
def acerca_de():
    modi11=Tk()
    modi11.geometry("200x200")
    modi11.resizable(False,False)
    modi11.title("Acerca de.")
    modi11.config(bg="yellow")
    label=Label(modi11,text= "Creado por: Minor Sancho",bg="yellow").place(x=10,y=10)
    label=Label(modi11,text= "Nombre: KEN_KEN",bg="yellow").place(x=10,y=30)
    label=Label(modi11,text= "Version: 5.1 ",bg="yellow").place(x=10,y=50)
    label=Label(modi11,text= "Programa No.2 ",bg="yellow").place(x=10,y=70)
    def validar():
        modi11.destroy()
        main()
    botonA=Button(modi11,text="Menu",bg="orange",fg="white",command=validar).place(x=10, y=170)
    modi11.mainloop()
#ventana de ayuda#
def ayuda():
    modi10=Tk()
    modi10.geometry("150x100")
    modi10.resizable(False,False)
    modi10.title("Ayuda")
    modi10.config(bg="yellow")
    def manual():
        archivo=os.popen('kenken_manual_de_usuario.pdf')
        return archivo
    def validar():
        modi10.destroy()
        manual()
    def validar1():
        modi10.destroy()
        acerca_de()
    
    
    botonA=Button(modi10,text="Acerca de",bg="orange",fg="white",command=validar1).place(x=10, y=40)
    botonA=Button(modi10,text="Manual",bg="green",command=validar).place(x=80, y=40)
    modi10.mainloop()
###########################################################
#funcion principal es el juego en si#
#############################################################
#ventana donde se crea el juego#
def pantalla():
    juego=Tk()
    juego.geometry("570x570")
    juego.resizable(False,False)
    #crea los botones como objetos#
    def botones():
        global matriz,ancho,largo,juego2
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                #print(juego2[i][j][0],juego2[i][j][1])
                btn = Button(juego,width=ancho,height =largo,bg=juego2[i][j][1], command=lambda a=i,b=j :[seleccionado(a,b)])
                
                # se coloca el boton en la matriz, en la posicion i,j
                btn.grid(row=i+1, column=j+1)
                boton[i][j] = btn
                if matriz[i][j]==0:
                    btn.config(text=str(juego2[i][j][0]))
                else:
                    btn.config(text=str(juego2[i][j][0])+"\n"+str(matriz[i][j]))
    #para saber que boton fue seleccionado#                
    def seleccionado(i,j):
        global boton,fil,col,inicio,error,pausa,deshacer
        if pausa=="#":
             messagebox.showerror("Error","El juego ya termino.")
        elif inicio==False:
            messagebox.showerror("Error","Debe iniciar el juego.")
        elif inicio=="":
            messagebox.showerror("Error","El juego esta pausado.")
        else:
            
            fil=i
            col=j
            deshacer=[[matriz[i][j],juego2[i][j][0],i,j]]+deshacer
            (boton[i][j]).config(bg="sky blue")
    #funcion que cambia el text segun el boton seleccionado#
    def numeros():
        def numero1():
            global fil,col
            if col!="" and fil!="":
                matriz[fil][col]=1
                boton[fil][col].config(bg=juego2[fil][col][1],text=juego2[fil][col][0]+"\n"+"1")
                fil=""
                col=""
            else:
                messagebox.showerror("Verifique los datos","Debe seleccionar una celda.")
        def numero2():
            global fil,col
            if col!="" and fil!="":
                matriz[fil][col]=2
                boton[fil][col].config(bg=juego2[fil][col][1],text=juego2[fil][col][0]+"\n"+"2")
                fil=""
                col=""
            else:
                messagebox.showerror("Verifique los datos","Debe seleccionar una celda.")
        def numero3():
            global fil,col
            if col!="" and fil!="":
                matriz[fil][col]=3
                boton[fil][col].config(bg=juego2[fil][col][1],text=juego2[fil][col][0]+"\n"+"3")
                fil=""
                col=""
            else:
                messagebox.showerror("Verifique los datos","Debe seleccionar una celda.")
        def numero4():
            global fil,col
            if col!="" and fil!="":
                matriz[fil][col]=4
                boton[fil][col].config(bg=juego2[fil][col][1],text=juego2[fil][col][0]+"\n"+"4")
                fil=""
                col=""
            else:
                messagebox.showerror("Verifique los datos","Debe seleccionar una celda.")
        def numero5():
            global fil,col
            if col!="" and fil!="":
                matriz[fil][col]=5
                boton[fil][col].config(bg=juego2[fil][col][1],text=juego2[fil][col][0]+"\n"+"5")
                fil=""
                col=""
            else:
                messagebox.showerror("Verifique los datos","Debe seleccionar una celda.")
        def numero6():
            global fil,col
            if col!="" and fil!="":
                matriz[fil][col]=6
                boton[fil][col].config(bg=juego2[fil][col][1],text=juego2[fil][col][0]+"\n"+"6")
                fil=""
                col=""
            else:
                messagebox.showerror("Verifique los datos","Debe seleccionar una celda.")
        def numero7():
            global fil,col
            if col!="" and fil!="":
                matriz[fil][col]=7
                boton[fil][col].config(bg=juego2[fil][col][1],text=juego2[fil][col][0]+"\n"+"7")
                fil=""
                col=""
            else:
                messagebox.showerror("Verifique los datos","Debe seleccionar una celda.")
        def numero8():
            global fil,col
            if col!="" and fil!="":
                matriz[fil][col]=8
                boton[fil][col].config(bg=juego2[fil][col][1],text=juego2[fil][col][0]+"\n"+"8")
                fil=""
                col=""
            else:
                messagebox.showerror("Verifique los datos","Debe seleccionar una celda.")
        def numero9():
            global fil,col
            if col!="" and fil!="":
                matriz[fil][col]=9
                boton[fil][col].config(bg=juego2[fil][col][1],text=juego2[fil][col][0]+"\n"+"9")
                fil=""
                col=""
            else:
                messagebox.showerror("Verifique los datos","Debe seleccionar una celda.")
        #borrador#
        def numeroC():
            global fil,col
            if col!="" and fil!="":
                matriz[fil][col]=0
                boton[fil][col].config(text=juego2[fil][col][0],bg=juego2[fil][col][1])
                fil=""
                col=""
            else:
                messagebox.showerror("Verifique los datos","Debe seleccionar una celda.")
        #estos if sirven para colocar los botones sea a la derecha o a la izquierda#
        if filas==3 and posicion==2:
            boton1=Button(juego,text="1",width=5,height =3,command=numero1).place(x=10,y=10)
            boton2=Button(juego,text="2",width=5,height =3,command=numero2).place(x=10,y=70)
            boton3=Button(juego,text="3",width=5,height =3,command=numero3).place(x=10,y=130)
            botonC=Button(juego,text="C",width=5,height =3,command=numeroC).place(x=10,y=190)
        elif filas==3 and posicion==1:
            boton1=Button(juego,text="1",width=5,height =3,command=numero1).place(x=500,y=10)
            boton2=Button(juego,text="2",width=5,height =3,command=numero2).place(x=500,y=70)
            boton3=Button(juego,text="3",width=5,height =3,command=numero3).place(x=500,y=130)
            botonC=Button(juego,text="C",width=5,height =3,command=numeroC).place(x=500,y=190)
            
        elif filas==4 and posicion==2:
            boton1=Button(juego,text="1",width=5,height =3,command=numero1).place(x=10,y=10)
            boton2=Button(juego,text="2",width=5,height =3,command=numero2).place(x=10,y=70)
            boton3=Button(juego,text="3",width=5,height =3,command=numero3).place(x=10,y=130)
            boton4=Button(juego,text="4",width=5,height =3,command=numero4).place(x=10,y=190)
            botonC=Button(juego,text="C",width=5,height =3,command=numeroC).place(x=10,y=250)
        elif filas==4 and posicion==1:
            boton1=Button(juego,text="1",width=5,height =3,command=numero1).place(x=500,y=10)
            boton2=Button(juego,text="2",width=5,height =3,command=numero2).place(x=500,y=70)
            boton3=Button(juego,text="3",width=5,height =3,command=numero3).place(x=500,y=130)
            boton4=Button(juego,text="4",width=5,height =3,command=numero4).place(x=500,y=190)
            botonC=Button(juego,text="C",width=5,height =3,command=numeroC).place(x=500,y=250)
        elif filas==5 and posicion==2:
            boton1=Button(juego,text="1",width=5,height =3,command=numero1).place(x=10,y=10)
            boton2=Button(juego,text="2",width=5,height =3,command=numero2).place(x=10,y=70)
            boton3=Button(juego,text="3",width=5,height =3,command=numero3).place(x=10,y=130)
            boton4=Button(juego,text="4",width=5,height =3,command=numero4).place(x=10,y=190)
            boton5=Button(juego,text="5",width=5,height =3,command=numero5).place(x=10,y=250)
            botonC=Button(juego,text="C",width=5,height =3,command=numeroC).place(x=10,y=300)
        elif filas==5 and posicion==1:
            boton1=Button(juego,text="1",width=5,height =3,command=numero1).place(x=500,y=10)
            boton2=Button(juego,text="2",width=5,height =3,command=numero2).place(x=500,y=70)
            boton3=Button(juego,text="3",width=5,height =3,command=numero3).place(x=500,y=130)
            boton4=Button(juego,text="4",width=5,height =3,command=numero4).place(x=500,y=190)
            boton5=Button(juego,text="5",width=5,height =3,command=numero5).place(x=500,y=250)
            botonC=Button(juego,text="C",width=5,height =3,command=numeroC).place(x=500,y=250)
        elif filas==6 and posicion==2:
            boton1=Button(juego,text="1",width=5,height =3,command=numero1).place(x=10,y=10)
            boton2=Button(juego,text="2",width=5,height =3,command=numero2).place(x=10,y=70)
            boton3=Button(juego,text="3",width=5,height =3,command=numero3).place(x=10,y=130)
            boton4=Button(juego,text="4",width=5,height =3,command=numero4).place(x=10,y=190)
            boton5=Button(juego,text="5",width=5,height =3,command=numero5).place(x=10,y=250)
            boton6=Button(juego,text="6",width=5,height =3,command=numero6).place(x=10,y=310)
            botonC=Button(juego,text="C",width=5,height =3,command=numeroC).place(x=10,y=360)
        elif filas==6 and posicion==1:
            boton1=Button(juego,text="1",width=5,height =3,command=numero1).place(x=500,y=10)
            boton2=Button(juego,text="2",width=5,height =3,command=numero2).place(x=500,y=70)
            boton3=Button(juego,text="3",width=5,height =3,command=numero3).place(x=500,y=130)
            boton4=Button(juego,text="4",width=5,height =3,command=numero4).place(x=500,y=190)
            boton5=Button(juego,text="5",width=5,height =3,command=numero5).place(x=500,y=250)
            boton6=Button(juego,text="6",width=5,height =3,command=numero6).place(x=500,y=310)
            botonC=Button(juego,text="C",width=5,height =3,command=numeroC).place(x=500,y=360)
        elif filas==7 and posicion==2:
            boton1=Button(juego,text="1",width=4,height =2,command=numero1).place(x=10,y=10)
            boton2=Button(juego,text="2",width=4,height =2,command=numero2).place(x=10,y=55)
            boton3=Button(juego,text="3",width=4,height =2,command=numero3).place(x=10,y=100)
            boton4=Button(juego,text="4",width=4,height =2,command=numero4).place(x=10,y=145)
            boton5=Button(juego,text="5",width=4,height =2,command=numero5).place(x=10,y=190)
            boton6=Button(juego,text="6",width=4,height =2,command=numero6).place(x=10,y=235)
            boton7=Button(juego,text="7",width=4,height =2,command=numero7).place(x=10,y=280)
            botonC=Button(juego,text="C",width=5,height =3,command=numeroC).place(x=10,y=325)
        elif filas==7 and posicion==1:
            boton1=Button(juego,text="1",width=4,height =2,command=numero1).place(x=500,y=10)
            boton2=Button(juego,text="2",width=4,height =2,command=numero2).place(x=500,y=55)
            boton3=Button(juego,text="3",width=4,height =2,command=numero3).place(x=500,y=100)
            boton4=Button(juego,text="4",width=4,height =2,command=numero4).place(x=500,y=145)
            boton5=Button(juego,text="5",width=4,height =2,command=numero5).place(x=500,y=190)
            boton6=Button(juego,text="6",width=4,height =2,command=numero6).place(x=500,y=235)
            boton7=Button(juego,text="7",width=4,height =2,command=numero7).place(x=500,y=280)
            botonC=Button(juego,text="C",width=5,height =3,command=numeroC).place(x=500,y=325)
        elif filas==8 and posicion==2:
            boton1=Button(juego,text="1",width=4,height =2,command=numero1).place(x=10,y=10)
            boton2=Button(juego,text="2",width=4,height =2,command=numero2).place(x=10,y=55)
            boton3=Button(juego,text="3",width=4,height =2,command=numero3).place(x=10,y=100)
            boton4=Button(juego,text="4",width=4,height =2,command=numero4).place(x=10,y=145)
            boton5=Button(juego,text="5",width=4,height =2,command=numero5).place(x=10,y=190)
            boton6=Button(juego,text="6",width=4,height =2,command=numero6).place(x=10,y=235)
            boton7=Button(juego,text="7",width=4,height =2,command=numero7).place(x=10,y=280)
            boton8=Button(juego,text="8",width=4,height =2,command=numero8).place(x=10,y=325)
            botonC=Button(juego,text="C",width=5,height =3,command=numeroC).place(x=10,y=370)
        elif filas==8 and posicion==1:
            boton1=Button(juego,text="1",width=4,height =2,command=numero1).place(x=500,y=10)
            boton2=Button(juego,text="2",width=4,height =2,command=numero2).place(x=500,y=55)
            boton3=Button(juego,text="3",width=4,height =2,command=numero3).place(x=500,y=100)
            boton4=Button(juego,text="4",width=4,height =2,command=numero4).place(x=500,y=145)
            boton5=Button(juego,text="5",width=4,height =2,command=numero5).place(x=500,y=190)
            boton6=Button(juego,text="6",width=4,height =2,command=numero6).place(x=500,y=235)
            boton7=Button(juego,text="7",width=4,height =2,command=numero7).place(x=500,y=280)
            boton8=Button(juego,text="8",width=4,height =2,command=numero8).place(x=500,y=325)
            botonC=Button(juego,text="C",width=5,height =3,command=numeroC).place(x=10,y=370)
        elif filas==9 and posicion==2:
            boton1=Button(juego,text="1",width=3,height =2,command=numero1).place(x=10,y=10)
            boton2=Button(juego,text="2",width=3,height =2,command=numero2).place(x=10,y=55)
            boton3=Button(juego,text="3",width=3,height =2,command=numero3).place(x=10,y=100)
            boton4=Button(juego,text="4",width=3,height =2,command=numero4).place(x=10,y=145)
            boton5=Button(juego,text="5",width=3,height =2,command=numero5).place(x=10,y=190)
            boton6=Button(juego,text="6",width=3,height =2,command=numero6).place(x=10,y=235)
            boton7=Button(juego,text="7",width=3,height =2,command=numero7).place(x=10,y=280)
            boton8=Button(juego,text="8",width=3,height =2,command=numero8).place(x=10,y=325)
            boton9=Button(juego,text="9",width=3,height =2,command=numero9).place(x=10,y=370)
            botonC=Button(juego,text="C",width=5,height =3,command=numeroC).place(x=10,y=410)
        elif filas==9 and posicion==1:
            boton1=Button(juego,text="1",width=4,height =2,command=numero1).place(x=500,y=10)
            boton2=Button(juego,text="2",width=4,height =2,command=numero2).place(x=500,y=55)
            boton3=Button(juego,text="3",width=4,height =2,command=numero3).place(x=500,y=100)
            boton4=Button(juego,text="4",width=4,height =2,command=numero4).place(x=500,y=145)
            boton5=Button(juego,text="5",width=4,height =2,command=numero5).place(x=500,y=190)
            boton6=Button(juego,text="6",width=4,height =2,command=numero6).place(x=500,y=235)
            boton7=Button(juego,text="7",width=4,height =2,command=numero7).place(x=500,y=280)
            boton8=Button(juego,text="8",width=4,height =2,command=numero8).place(x=500,y=325)
            boton9=Button(juego,text="9",width=4,height =2,command=numero9).place(x=500,y=370)
            botonC=Button(juego,text="C",width=5,height =3,command=numeroC).place(x=500,y=410)


       

        
    label=Label(juego,text="                                     ")
    label.grid(row=0, column=0)
#valida repetidos en fila
    def validar_fila():
        global matriz,boton,inicio
        if inicio==False:
            messagebox.showerror("Error","Debe iniciar el juego")
        else:
            for i in range(len(matriz)):
                lista=[]
                for j in range(len(matriz[i])):
                    if matriz[i][j] not in lista:
                        lista+=[matriz[i][j]]
                    else:
                        boton[i][j].config(bg="red")
                lista=[]
            return validar_columna()
    #valida repetidos en columna#
    def validar_columna():
        global matriz,boton,filas,pausa,error2
        cont2=0
        cont=0
        error2=0
        while cont2<len(matriz[cont]):
            lista=[]
            
            while cont<len(matriz):
                if matriz[cont][cont2] not in lista:
                    lista+=[matriz[cont][cont2]]
                    cont+=1
                    error2+=1
                else:
                    boton[cont][cont2].config(bg="red")
                    cont+=1
            cont=0
            cont2+=1
        if error2!=(filas*filas):
            messagebox.showerror("Error","Hay errores por corregir")
            
        return
#funcion que crea le temporizador#
    def tempor():
        todo_a_seg()
        global segundos,pausa,tiempo_pasado,reloj
        cont=segundos
        while cont>=0:
            if pausa==True:
                lt.config(text=hora(cont))
                cont-=1
                time.sleep(1)
            elif pausa==True:
                lt.config(text=hora(cont))
            elif pausa=="#":
                tiempo_pasado=cont
                return
        messagebox.showerror("Error","su tiempo se acabo")
        a=messagebox.askquestion("Cancelar","Desea continuar jugando")
        if a=="yes":
            reloj=1
            llamar_reloj()
        else:
            terminar_juego()
    #crea el reloj#
    def reloj():
        global segundos,pausa,tiempo_pasado
        cont=segundos+1
        while cont>0:
            if pausa==True:
                lt.config(text=hora(segundos))
                segundos+=1
                time.sleep(1)
            elif pausa==True:
                lt.config(text=hora(segundos))
            elif pausa=="#":
                tiempo_pasado=segundos
                return
        #hilo del temporizador#
    def llamar_temp():
        b=threading.Thread(target=tempor,name="Temporizador",args=())
        b.start()
        #hilo del reloj#
    def llamar_reloj():
        c=threading.Thread(target=reloj,name="Reloj",args=())
        c.start()
        #carga la musica#
    def musica():
        file = "sample_sample.wav"
        winsound.PlaySound(file,winsound.SND_FILENAME|winsound.SND_NOWAIT,)
        return
    #hilo de la musica
    def llamar_musica():
        c=threading.Thread(target=musica,name="music",args=())
        c.start()
    #inicia el juego
    def inicio_juego():
        global inicio
        if inicio==True or inicio=="":
            messagebox.showerror("Error","El juego ya fue iniciado")
        else:
            inicio=True
            t.config(state="disabled")
    #inicia el reloj o el tempo#
    def star():
        global reloj
        if reloj==3:
            inicio_juego()
            llamar_temp()
        elif reloj ==1:
            inicio_juego()
            llamar_reloj()
        else:
            inicio_juego()
            
    lt= Label(juego)
    lt.place(x=20,y=510)

    
    t=Button(juego,text="Iniciar",command=star)
    t.place(x=40,y=530)
    #funcion para saber si se ha ganado o no
    def lachele():
        global  error,error2,pausa,filas,tiempo_pasado,reloj,activar_sobrevivir
        validar_fila()
        inicio_de_validacion()
        if activar_sobrevivir==0:
            if error==0 and error2==(filas*filas) and sonido==1 and filas==3:
                pausa="#"
                llamar_musica()
                messagebox.showinfo("Felicidades","Haz Ganado")
                crear_3()
                terminar_juego2()
                
            elif error==0 and error2==(filas*filas) and sonido==2 and filas==3:
                 pausa="#"
                 print("tiempo",tiempo_pasado)
                 messagebox.showinfo("Felicidades","Haz Ganado")
                 crear_3()
                 terminar_juego2()
            elif error==0 and error2==(filas*filas) and sonido==1 and filas==4:
                pausa="#"
                llamar_musica()
                messagebox.showinfo("Felicidades","Haz Ganado")
                crear_4()
                terminar_juego2()
            elif error==0 and error2==(filas*filas) and sonido==2 and filas==4:
                 pausa="#"
                 messagebox.showinfo("Felicidades","Haz Ganado")
                 crear_4()
                 terminar_juego2()
            elif error==0 and error2==(filas*filas) and sonido==1 and filas==5:
                pausa="#"
                messagebox.showinfo("Felicidades","Haz Ganado")
                llamar_musica()
                crear_5()
                terminar_juego2()
                
            elif error==0 and error2==(filas*filas) and sonido==2 and filas==5:
                 pausa="#"
                 messagebox.showinfo("Felicidades","Haz Ganado")
                 crear_5()
                 terminar_juego2()
            elif error==0 and error2==(filas*filas) and sonido==1 and filas==6:
                pausa="#"
                llamar_musica()
                messagebox.showinfo("Felicidades","Haz Ganado")
                crear_6()
                terminar_juego2()
            elif error==0 and error2==(filas*filas) and sonido==2 and filas==6:
                 pausa="#"
                 messagebox.showinfo("Felicidades","Haz Ganado")
                 crear_6()
                 terminar_juego2()
            elif error==0 and error2==(filas*filas) and sonido==1 and filas==7:
                pausa="#"
                llamar_musica()
                messagebox.showinfo("Felicidades","Haz Ganado")
                crear_7()
                terminar_juego2()
                
            elif error==0 and error2==(filas*filas) and sonido==2 and filas==7:
                 pausa="#"
                 
                 messagebox.showinfo("Felicidades","Haz Ganado")
                 crear_7()
                 terminar_juego2()
            elif error==0 and error2==(filas*filas) and sonido==1 and filas==8:
                pausa="#"
                
                llamar_musica()
                messagebox.showinfo("Felicidades","Haz Ganado")
                crear_8()
                terminar_juego2()
            elif error==0 and error2==(filas*filas) and sonido==2 and filas==8:
                 pausa="#"
                 
                 messagebox.showinfo("Felicidades","Haz Ganado")
                 crear_8()
                 terminar_juego2()
            elif error==0 and error2==(filas*filas) and sonido==1 and filas==9:
                pausa="#"
                
                llamar_musica()
                messagebox.showinfo("Felicidades","Haz Ganado")
                crear_9()
                terminar_juego2()
            elif error==0 and error2==(filas*filas) and sonido==2 and filas==9:
                 pausa="#"
                 messagebox.showinfo("Felicidades","Haz Ganado")
                 crear_9()
                 terminar_juego2()
            else:
                messagebox.showerror("Error","Aun no ganas")
        elif activar_sobrevivir==1:
            if error==0 and error2==(filas*filas) and sonido==1 and filas==3:
                pausa="#"
                llamar_musica()
                messagebox.showinfo("Felicidades","Haz Ganado")
                crear_3()
                terminar_juego3()
                asignacion()
                
            elif error==0 and error2==(filas*filas) and sonido==2 and filas==3:
                 global matriz,juego2
                 pausa="#"
                 print("tiempo",tiempo_pasado)
                 messagebox.showinfo("Felicidades","Haz Ganado")
                 crear_3()
                 terminar_juego3()
                 
                 print(juego2,matriz)

                 asignacion()
            elif error==0 and error2==(filas*filas) and sonido==1 and filas==4:
                pausa="#"
                llamar_musica()
                messagebox.showinfo("Felicidades","Haz Ganado")
                crear_4()
                terminar_juego3()
                
                asignacion()
            elif error==0 and error2==(filas*filas) and sonido==2 and filas==4:
                 pausa="#"
                 messagebox.showinfo("Felicidades","Haz Ganado")
                 crear_4()
                 terminar_juego3()
                 
                 asignacion()
            elif error==0 and error2==(filas*filas) and sonido==1 and filas==5:
                pausa="#"
                messagebox.showinfo("Felicidades","Haz Ganado")
                llamar_musica()
                crear_5()
                terminar_juego3()
                
                asignacion()
                
            elif error==0 and error2==(filas*filas) and sonido==2 and filas==5:
                 pausa="#"
                 messagebox.showinfo("Felicidades","Haz Ganado")
                 crear_5()
                 terminar_juego3()
                 asignacion()
            elif error==0 and error2==(filas*filas) and sonido==1 and filas==6:
                pausa="#"
                llamar_musica()
                messagebox.showinfo("Felicidades","Haz Ganado")
                crear_6()
                terminar_juego3()
                asignacion()
            elif error==0 and error2==(filas*filas) and sonido==2 and filas==6:
                 pausa="#"
                 messagebox.showinfo("Felicidades","Haz Ganado")
                 crear_6()
                 terminar_juego3()
                 asignacion()
            elif error==0 and error2==(filas*filas) and sonido==1 and filas==7:
                pausa="#"
                llamar_musica()
                messagebox.showinfo("Felicidades","Haz Ganado")
                crear_7()
                terminar_juego3()
               
                asignacion()
                
            elif error==0 and error2==(filas*filas) and sonido==2 and filas==7:
                 pausa="#"
                 
                 messagebox.showinfo("Felicidades","Haz Ganado")
                 crear_7()
                 terminar_juego3()
                 asignacion()
            elif error==0 and error2==(filas*filas) and sonido==1 and filas==8:
                pausa="#"
                
                llamar_musica()
                messagebox.showinfo("Felicidades","Haz Ganado")
                crear_8()
                terminar_juego3()
                asignacion()
            elif error==0 and error2==(filas*filas) and sonido==2 and filas==8:
                 pausa="#"
                 
                 messagebox.showinfo("Felicidades","Haz Ganado")
                 crear_8()
                 terminar_juego3()
                 asignacion()
            elif error==0 and error2==(filas*filas) and sonido==1 and filas==9:
                pausa="#"
                llamar_musica()
                messagebox.showinfo("Felicidades","Haz Ganado")
                crear_9()
                terminar_juego2()
            elif error==0 and error2==(filas*filas) and sonido==2 and filas==9:
                 pausa="#"
                 messagebox.showinfo("Felicidades","Haz Ganado")
                 crear_9()
                 terminar_juego3()
                 asignacion()
            else:
                messagebox.showerror("Error","Aun no ganas")
    boton_val=Button(juego,text="Validar",command=lachele).place(x=100,y=530)
    #reinicia el juego setea matrices#
    def reiniciar():
        global matriz,boton,segundos,inicio,reloj,actual,pausa
        pausa="#"
        time.sleep(1)
        inicio=False
        matriz=[]
        boton=[]
        segundos=segundos
        crear_matriz_logica()
        crear_matriz_botones()
        actual=actual
        reloj=reloj
        juego.destroy()
        pausa=True
        pantalla()

    reini=Button(juego,text="Reiniciar",command=reiniciar).place(x=160,y=530)
    #pausa el tempo o el reloj#
    def pausar():
        global pausa,inicio
        if inicio==False:
            messagebox.showerror("Error","Debe iniciar el juego")
        elif pausa==False:
            pausa=True
            inicio=True
        else:
            pausa=False
            inicio=""
            
    #boton de pausa#
    def boton_pausa():
        global reloj ,pausa,inicio
        if reloj==3 and pausa==True:
            pause=Button(juego,text="Pausar",command=pausar).place(x=80,y=490)
        if reloj==1 and pausa==True:
            pause=Button(juego,text="Pausar",command=pausar).place(x=80,y=490)
#esta funcion setea todo para terminar el juego#
    def terminar_juego():
        a=messagebox.askquestion("Cancelar","Desea terminar la partida")
        if a =="yes":
            global error,error2,actual,ya_usados,usado,nombre,juego2,nivel3,nivel4,nivel5,nivel6,nivel7,nivel8,nivel9,matriz,boton,filas,reloj,posicion,sonido,ancho,largo,fil,col,segundos,minutos,horas,inicio,pausa,rehacer,deshacer
            nombre=""
            pausa="#"
            time.sleep(1)
            error=0
            error2=0
            ya_usados=[]
            usado=[]
            actual=[]
            juego2=[]
            nivel3=[]
            nivel4=[]
            nivel5=[]
            nivel6=[]
            nivel7=[]
            nivel8=[]
            nivel9=[]
            boton=[]
            matriz=[]
            filas=0
            reloj=0
            posicion=0
            sonido=0
            ancho=0
            largo=0
            rehacer=[]
            deshacer=[]
            fil=""
            col=""
            segundos=0
            minutos=0
            horas=0
            inicio=False
            juego.destroy()
            pausa=True
            main()
        else:
            None
        #no pregunta solo termina el juego#
    def terminar_juego2():
        global error,error2,actual,ya_usados,usado,nombre,juego2,nivel3,nivel4,nivel5,nivel6,nivel7,nivel8,nivel9,matriz,boton,filas,reloj,posicion,sonido,ancho,largo,fil,col,segundos,minutos,horas,inicio,pausa,rehacer,deshacer,tiempo_pasado
        nombre=""
        pausa="#"
        time.sleep(1)
        print(tiempo_pasado)
        error=0
        error2=0
        ya_usados=[]
        usado=[]
        actual=[]
        juego2=[]
        nivel3=[]
        nivel4=[]
        nivel5=[]
        nivel6=[]
        nivel7=[]
        nivel8=[]
        nivel9=[]
        boton=[]
        matriz=[]
        filas=0
        reloj=0
        posicion=0
        sonido=0
        ancho=0
        largo=0
        rehacer=[]
        deshacer=[]
        fil=""
        col=""
        segundos=0
        minutos=0
        horas=0
        inicio=False
        juego.destroy()
        pausa=True
        main()

    def terminar_juego3():
        global error,error2,actual,ya_usados,usado,nombre,juego2,nivel3,nivel4,nivel5,nivel6,nivel7,nivel8,nivel9,matriz,boton,filas,reloj,posicion,sonido,ancho,largo,fil,col,segundos,minutos,horas,inicio,pausa,rehacer,deshacer,tiempo_actual
        if reloj==3:
            pausa="#"
            time.sleep(1)
            segundos=tiempo_pasado
            error=0
            error2=0
            actual=[]
            boton=[]
            matriz=[]
            juego2=[]
            rehacer=[]
            deshacer=[]
            fil=""
            col=""
            minutos=0
            horas=0
            inicio=False
            juego.destroy()
            pausa=True
        elif reloj==1:
            pausa="#"
            time.sleep(1)
            segundos=tiempo_pasado
            error=0
            error2=0
            actual=[]
            boton=[]
            matriz=[]
            juego2=[]
            rehacer=[]
            deshacer=[]
            fil=""
            col=""
            minutos=0
            horas=0
            inicio=False
            juego.destroy()
            pausa=True
            time.sleep(1)
            
    reini=Button(juego,text="Teminar",command=terminar_juego).place(x=220,y=530)
    def guardar():
        obtener_tiempo_pasado()
        printq()
        guardarpartida()
        terminar_juego2()
    #funcion que obtiene el tiempo pasado
    def obtener_tiempo_pasado():
        global pausa,tiempo_pasado
        pausa="#"
        time.sleep(2)
        return
    def printq():
        global tiempo_pasado
        return tiempo_pasado
    #funcion para guarada una partida
    def guardarpartida():
        global nombre,tiempo_pasado,matriz,reloj,filas,actual,posicion,sonido,ancho,largo,juego2,segundos,rehacer,deshacer
        
        listasave = (nombre,tiempo_pasado,matriz,reloj,filas,actual,posicion,sonido,ancho,largo,juego2,segundos,False,rehacer,deshacer)
        archivo = asksaveasfilename(defaultextension=".minor")
        try:
            save = open(archivo,"a")
            save.write(str(listasave))
            save.close()
            return 
        except:
            return
    guardar=Button(juego,text="Guardar",command=guardar).place(x=280,y=530)
    #jugar otra vez otro juego pero en el mismo nivel#
    def Otro_juego():
        global matriz,boton,juego2,matriz,boton,segundos,inicio,reloj,actual,pausa
        a=messagebox.askquestion("Cancelar","Desea terminar la partida")
        if a =="yes":
            pausa="#"
            time.sleep(1)
            matriz=[]
            boton=[]
            juego2=[]
            inicio=False
            segundos=segundos
            reloj=reloj
            pausa=True
            generar_random()
            crear_matriz_logica()
            crear_matriz_botones()
            crear_matriz_juego()
            matriz_con_color(actual)
            juego.destroy()
            pantalla()

            
        
        else:
            None
    
    def validar_primero():#funcion para ver si ya se selecciono una celda#
        global col,fil
        if col=="" or fil=="":
            messagebox.showerror("Error","Seleccione una celda")
        else:
            buscar_celda()
    def llamar_celda():
        c=threading.Thread(target=buscar_celda,name="posimi",args=())
        c.start()
    #funcion para ver las jaulas que componen la celda seleccionado#
    def buscar_celda():
        global fil,col,actual
        d=actual
        resultado=()
        for i in d.values():
            if tuple([fil,col]) in i:
                resultado=i
        return separar(resultado)

    #funcion para separar tuplas de str #
    def separar(tupla):
        numero=""
        tuplas=[]
        for i in tupla:
            if type(i)==str:
                numero=i
            elif type(i)==tuple:
                tuplas+=[i]
        return conseguir_operador(numero,tuplas)

    #funcion para separar el numero del operador, tambien asigna la lista donde se haran las combinaciones#
    def conseguir_operador(numero,tuplas):
        global filas
        num=""
        operador=""
        lista=""
        for i in numero:
            if i in ["-","/","x","+"]:
                operador=i
            elif i in ["1","2","3","4","5","6","7","8","9","0"]:
                num+= i
        if filas==3:
            lista=[1,2,3]
        elif filas==4:
            lista=[1,2,3,4]
        elif filas==5:
            lista=[1,2,3,4,5]
        elif filas==6:
            lista=[1,2,3,4,5,6]
        elif filas==7:
            lista=[1,2,3,4,5,6,7]
        elif filas==8:
            lista=[1,2,3,4,5,6,7,8]
        elif filas==9:
            lista=[1,2,3,4,5,6,7,8,9]
        
            
        return crear_combinaciones(int(num),operador,tuplas,lista)

    #funcion para crear las combinaciones segun la cantidad de celdas de la jaula#
    def crear_combinaciones(num,operador,tuplas,lista):
        combinaciones=[]
        if len(tuplas)==1:
            combinaciones+=[(num)]
            return select_opcion(tuplas,combinaciones)
            
        else:   
            combinaciones=list(itertools.product(lista, repeat=len(tuplas)))
            return desechar_combinaciones(num,operador,tuplas,combinaciones)
            
    #funcion que deja en la combinaciones solo os que sirven#

    def desechar_combinaciones(num,operador,tuplas,combinaciones):
        resultado=[]
        if operador=="+":
            final=0
            for i in combinaciones:
                for j in i:
                    final+=j
                if int(final)==int(num):
                    resultado+=[i]
                final=0
            return select_opcion(tuplas,resultado)
        elif operador=='x':
            
            final=1
            for i in combinaciones:
                
                for j in i:
                    final*=int(j)
                
                if int(final)==int(num):
                    resultado+=[i]
                final=1
            return select_opcion(tuplas,resultado)
        elif operador=="/":
            final=0
            for i in combinaciones:
                b=i
                i=list(i)
                i=sorted(i, reverse = True)
                for j in i:
                    if final==0:
                        final+=int(j)
                    else:
                        final/=int(j)
                    
                if final==int(num):
                    resultado+=[b]
                final=0
            return select_opcion(tuplas,resultado)
            
        elif operador=="-":
            final=0
            for i in combinaciones:
                b=i
                for j in i:
                    final-=int(j)
                    final=abs(final)
                if int(final)==int(num):
                    resultado+=[b]
                final=0
            return select_opcion(tuplas,resultado)
        else:
            final=0
            for i in combinaciones:
                if int(i[0])==int(num):
                    resultado+=[i]
                final=0
            return select_opcion(tuplas,resultado)
    #funcion para seleccionar una opcion#
    def select_opcion(tuplas,resultado):
        select5= Tk()
        select5.geometry("140x197")
        select5.config(bg="black")
        scrollbar = Scrollbar(select5)
        scrollbar.pack( side = RIGHT, fill=Y )
        lista=Listbox(select5)
        lista.config(width=20,yscrollcommand = scrollbar.set,selectmode=BROWSE)
##        lista = Listbox()
        for i in range(len(resultado)):
            lista.insert(i,resultado[i])
        def callback():
            select2=""
            select2 =lista.curselection()
            select2=select2[0]
            a=resultado[select2]
            b=tuplas
            
            return asignar_de_nuevo(a,b)
        def validar16():
            callback()
            select5.destroy()
        #funcion para asignar la opcio escojida    
        def asignar_de_nuevo(a,b):
            global matriz,boton,juego2,fil,col
            if type(a)==int:
                matriz[b[0][0]][b[0][1]]=a
                boton[b[0][0]][b[0][1]].config(bg=juego2[b[0][0]][b[0][1]][1],text=str(juego2[b[0][0]][b[0][1]][0])+"\n"+str(matriz[b[0][0]][b[0][1]]))
                fil=""
                col=""
            else:
                for i in range(len(a)):
                    matriz[b[i][0]][b[i][1]]=a[i]
                    boton[b[i][0]][b[i][1]].config(bg=juego2[b[i][0]][b[i][1]][1],text=str(juego2[b[i][0]][b[i][1]][0])+"\n"+str(matriz[b[i][0]][b[i][1]]))
                fil=""
                col=""
                return
                                        
        boton2=Button(select5,text="continuar",fg="Red",command=validar16)
        boton2.place(x=60,y=170)
        lista.place(x=0,y=0)
        scrollbar.config( command = lista.yview )
        select5.mainloop()
        

    posi=Button(juego,text="Posibles",command=validar_primero).place(x=340,y=500)
    new_game=Button(juego,text="Otro juego",command=Otro_juego).place(x=340,y=530)
    #funcion usada para hacer el undo#
    def undo():
        global boton,matriz,juego2,deshacer,rehacer
        if deshacer==[]:
            messagebox.showerror("Error","No se han registrado cambios")
        elif deshacer[0][0]==0:
            fil=deshacer[0][2]
            col=deshacer[0][3]
            rehacer=[[matriz[fil][col],"3",fil,col]]+rehacer
            matriz[fil][col]=0
            boton[fil][col].config(text=str(juego2[fil][col][0]),bg=juego2[fil][col][1])
            deshacer = deshacer[1:]
        elif deshacer[0][0]!=0:
            fil=deshacer[0][2]
            col=deshacer[0][3]
            rehacer=[[matriz[fil][col],"3",fil,col]]+rehacer
            matriz[fil][col]=deshacer[0][0]
            boton[fil][col].config(text=str(juego2[fil][col][0])+"\n"+str(matriz[fil][col]),bg=juego2[fil][col][1])
            deshacer = deshacer[1:]

    def redo():
        global boton,matriz,juego2,deshacer,rehacer
        if rehacer==[]:
            messagebox.showerror("Error","No se han registrado cambios")
        elif rehacer[0][0]==0:
            fil=rehacer[0][2]
            col=rehacer[0][3]
            deshacer=[[matriz[fil][col],"3",fil,col]]+deshacer
            matriz[fil][col]=0
            boton[fil][col].config(text=str(juego2[fil][col][0]),bg=juego2[fil][col][1])
            rehacer = rehacer[1:]
        elif rehacer[0][0]!=0:
            fil=rehacer[0][2]
            col=rehacer[0][3]
            deshacer=[[matriz[fil][col],"3",fil,col]]+deshacer
            matriz[fil][col]=rehacer[0][0]
            boton[fil][col].config(text=str(juego2[fil][col][0])+"\n"+str(matriz[fil][col]),bg=juego2[fil][col][1])
            rehacer = rehacer[1:]
    def llamar_main5():
        b=threading.Thread(target=main5,name="5x5",args=())
        b.start()
    def escoger_segun_fila():
        global filas,error
        error=0
        if filas==3:
            main3()
            messagebox.showinfo("JARVIS","Esa es la solucion")
            terminar_juego2()
            return
        elif filas==4:
            main4()
            messagebox.showinfo("JARVIS","Esa es la solucion")
            terminar_juego2()
            return
        elif filas==5:
            main5()
            messagebox.showinfo("JARVIS","Esa es la solucion")
            terminar_juego2()
            return
        
    solucion=Button(juego,text="Solucion",command=escoger_segun_fila).place(x=415,y=500)        
    undo=Button(juego,text="Undo",command=undo).place(x=415,y=530)
    redo=Button(juego,text="Redo",command=redo).place(x=465,y=530)
    
        
    numeros()
    botones()
    boton_pausa()
    juego.mainloop()


#pantalla menu
def main():
    principal=Tk()
    principal.geometry("490x310")
    principal.title("Ken Ken")
    principal. config(bg="yellow")
    principal.resizable(False,False)
    #inicia la configuracion#

    def validar1():
        principal.destroy()
        nivel_seleccionado()
    boton1= Button(principal,text="Configuración Del Juego",fg="red",font="Cosmic 14",bg="black",command=validar1).place(x=10,y=5)
    def validar2():
        global nombre , sonido,nombre,tiempo_pasado,reloj,filas,actual,posicion,sonido,ancho,largo,segundos,pausa,inicio,nivel6,usado
        if nombre=="" and sonido==0:
            lee()
            filas=6
            ancho=5
            largo=3
            reloj=1
            posicion=1
            sonido=2
            usado=nivel6
            acomodo_rest()
            actual=usado[0]
            principal.destroy()
            player_name()
        else:
            crear_matriz_logica()
            crear_matriz_botones()
            crear_matriz_juego()
            matriz_con_color(actual)
            principal.destroy()
            pantalla()
        
    boton1= Button(principal,text="Jugar",fg="red",font="Cosmic 14",bg="black",command=validar2).place(x=10,y=55)
    #lleva al medallero#
    def validar3():
        principal.destroy()
        medallero()
        
    boton1= Button(principal,text="Top 10",fg="red",font="Cosmic 14",bg="black",command=validar3).place(x=10,y=105)
    #perimite cargar una partida#
    def cargarpartida():
        load = askopenfilename(filetypes=[("Archivos Minor","*.minor")])
        if load == "":
            return
        else:
            saved = open(load,"r")
            f=saved.read()
            a=eval(f)
            saved.close()
            return renombrar(a)
#asigna glbales de nuevo#
    def renombrar(lista):
        global nombre,tiempo_pasado,matriz,reloj,filas,actual,posicion,sonido,ancho,largo,juego2,segundos,pausa,inicio,rehacer,deshacer
        nombre=lista[0]
        tiempo_pasado=lista[1]
        matriz=lista[2]
        reloj=lista[3]
        filas=lista[4]
        actual=lista[5]
        posicion=lista[6]
        sonido=lista[7]
        ancho=lista[8]
        largo=lista[9]
        juego2=lista[10]
        segundos=lista[11]
        rehacer=lista[13]
        deshacer=lista[14]
        pausa=True
        inicio=False
        segundos=int(tiempo_pasado)
        return
    #crea matriz, carga y nos lleva al juego#
    def validar4():
        
        cargarpartida()
        crear_matriz_botones()
        principal.destroy()
        pantalla()
    
    boton1= Button(principal,text="Cargar",fg="red",font="Cosmic 14",bg="black",command=validar4).place(x=10,y=155)
    def validar4():
        principal.destroy()
        ayuda()
        
    boton1= Button(principal,text="Ayuda",fg="red",font="Cosmic 14",bg="black",command=validar4).place(x=10,y=205)
    boton1= Button(principal,text="Imprimir",fg="red",font="Cosmic 14",bg="black",command=imprim).place(x=90,y=205)
    boton1= Button(principal,text="Salir",fg="red",font="Cosmic 14",bg="black",command=principal.destroy).place(x=10,y=255)
    def llamar_amigo1():
        c=threading.Thread(target=amigo1,name="Contactar",args=())
        c.start()
    def verrec():
        webbrowser.open("https://www.youtube.com/watch?v=4vG_CF4GcY4")
    boton1= Button(principal,text="Contactenos",fg="red",font="Cosmic 14",bg="black",command=llamar_amigo1).place(x=90,y=255)
    boton1= Button(principal,text="Tutorial",fg="red",font="Cosmic 14",bg="black",command=verrec).place(x=220,y=255)
    
    
    
    principal.mainloop()
