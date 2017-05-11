##IMPORTA GLIBRERIA TKINTER
from tkinter import *
from math import*

##CREACION DE LA APLICACION
app = Tk()
app.title("Evaluador de expresiones")
app.geometry("500x500")
app.resizable(True,False)
app.config(bg="#00FFFF")

##LABEL 1
lab=Label(app,text="Ingrese la Expresión en Notacion Infija:", bg="#00FFFF", font=("Algerian"),fg="#0B615E").place(x=80,y=5)

##ENTRYBOX
input_tk = Entry(app,bg="white", fg="black", width=80)
input_tk.place(x=8,y=35)

def estadísticas():
##    arbol=input_tk.get()
    arbol=input_tk.get()
    print(arbol)
    laarbol = Label(app,text=beginarbol(separador(arbol)), bg="#00FFFF", font=("Times 13 italic"))
    laarbol.place(x=5,y=359)
##    lalt = Label(app,text="Altura del árbol:",bg="green", font=("Times 13 italic"))
##    lalt.place(x=5,y=235)
    lanod = Label(app,text="Nodos del árbol:",bg="#00FFFF", font=("Times 13 italic"))
    lanod.place(x=5,y=256)
    lahoj = Label(app,text="Hojas del árbol:",bg="#00FFFF", font=("Times 13 italic"))
    lahoj.place(x=5,y=277)
    lanodin = Label(app,text="Nodos internos del árbol:",bg="#00FFFF", font=("Times 13 italic"))
    lanodin.place(x=5,y=298)
##    laltura = Label(app,text=altura(beginarbol(separador(arbol))), bg="green", font=("Times 13 italic"))
##    latura.place(x=150,y=235)
    lahojas = Label(app, text=hojas(beginarbol(separador(arbol))),bg="#00FFFF", font=("Times 13 italic"))
    lahojas.place(x=125,y=277)
    lanodos = Label(app,text=nodos(beginarbol(separador(arbol))),bg="#00FFFF", font=("Times 13 italic"))
    lanodos.place(x=125,y=256)
    lanodosin = Label(app,text=nodosinternos(beginarbol(separador(arbol))),bg="#00FFFF", font=("Times 13 italic"))
    lanodosin.place(x=190,y=298)
    laresult = Label(app,text="Resultado:",bg="#00FFFF", font=("Times 13 italic"))
    laresult.place(x=5,y=318)
    lare = Label(app,text=eval(input_tk.get()),bg="#00FFFF", font=("Times 13 italic"))
    lare.place(x=85,y=318)

def cambiolabel():
    nuevotexto = input_tk.get()
    texto.config(text=nuevotexto)

def getlabel():
    nuevotexto = input_tk.get()
    return nuevotexto

##ENTRADA: STRING
##SALIDA: STRING
##LABEL INFIJA
def cambiarlab1():
    texto = Label(app,bg="#00FFFF",fg="black")
    nuevotexto = input_tk.get()
    texto.config(text=tostring(inOrden(beginarbol(separador(nuevotexto)))), font=("Arial 15 bold"))
    texto.place(x=150,y=160)

##ENTRADA: STRING
##SALIDA: STRING
##LABEL PREFIJA
def cambiarlab2():
    texto = Label(app,bg="#00FFFF",fg="black")
    nuevotexto = input_tk.get()
    texto.config(text=tostring(preOrden(beginarbol(separador(nuevotexto)))), font=("Arial 15 bold"))
    texto.place(x=150,y=160)

##ENTRADA: STRING
##SALIDA: STRING
##LABEL POSFIJA
def cambiarlab3():
    texto = Label(app,bg="#00FFFF",fg="black")
    nuevotexto = input_tk.get()
    texto.config(text=tostring(postOrden(beginarbol(separador(nuevotexto)))), font=("Arial 15 bold"))
    texto.place(x=150,y=160)
    
    
def arbol (raiz, hijoi, hijod):
    return [raiz,hijoi,hijod]

def hijoderecho(arbol):
    try:
        if arbol[1]==[]:
            return []
        else:
            return arbol[1]
    except:
        return[]
    
def hijoizquierdo(arbol):
    try:
        if arbol[2]==[]:
            return []
        else:
            finallabel=arbol[1]
            return arbol[1]
    except:
        return[]
    
def raiz(arbol):
    try:
        if arbol==[]:
            return []
        else:
            return arbol[0]
    except:
        return arbol
    
def hoja(arbol):
    if hijoderecho(arbol)==[] and hijoizquierdo(arbol)==[]:
        return True
    elif type(arbol)==int:
        return True
    else:
        return False
    

    
def altura(arbol):
    if arbol==[]:
        return 0
    elif hijoderecho==[]:
        return altura(hijoizquierdo(arbol))
    elif hijoizquierdo==[]:
        return altura(hijoderecho(arbol))
    else:
        return 1+altura(hijoderecho(arbol))+altura(hijoizquierdo(arbol))
    
def hojas(arbol):
    if arbol == []:
        return 0
    elif hoja(arbol):
        return 1
    else:
        return hojas(hijoderecho(arbol))+hojas(hijoizquierdo(arbol))

def nodos(arbol):
    if arbol == []:
        return 0
    else:
        return 1 + nodos(hijoderecho(arbol))+nodos(hijoizquierdo(arbol))

def nodosinternos(arbol):
    if arbol == []:
        return 0
    elif hoja(arbol):
        return 0
    else:
        return 1 + nodosinternos(hijoderecho(arbol))+nodosinternos(hijoizquierdo(arbol))








#///////////////////////////#
#/FUNCIONES VISTAS EN CLASE/#
#///////////////////////////#
def arbol(raiz,hijoizq=[], hijoder=[]):
    if hijoizq==[] and hijoder==[]:
        return raiz
    else:
        return [raiz]+[hijoizq]+[hijoder]


def atomo(x):
    if type(x)!=list:
        return True
    else:
        return False

def raiz(arbol):
    if atomo(arbol):
        return arbol
    else:
        return arbol[0]

def hijoizq(arbol):
    if atomo(arbol):
        return []
    else:
        return arbol[1]

def hijoder(arbol):
    if atomo(arbol):
        return []
    else:
        return arbol[2]

def hoja(arbol):
    if arbol==[]:
        return False
    elif atomo(arbol):
        return True
    elif hijoizq(arbol)==[] and hijoder==[]:
        return True
    else:
        return False

def inOrden(arbol):
    if arbol==[]:
        return []
    elif atomo(arbol):
        return [arbol]
    else:
        return inOrden(hijoizq(arbol))+[raiz(arbol)]+inOrden(hijoder(arbol))

def preOrden(arbol):
    if arbol==[]:
        return []
    elif atomo(arbol):
        return [raiz(arbol)]
    else:
        return [raiz(arbol)]+preOrden(hijoizq(arbol))+preOrden(hijoder(arbol))

def buscar(ele,arbol):
    if arbol==[]:
        return False
    elif raiz(arbol)==ele:
        return True
    else: 
        return buscar(ele,hijoizq(arbol)) or buscar(ele,hijoder(arbol))
    
def postOrden(arbol):
    if arbol==[]:
        return []
    elif atomo(arbol):
        return [raiz(arbol)]
    else:
        return postOrden(hijoizq(arbol))+postOrden(hijoder(arbol))+[raiz(arbol)]

#/////////////////////////////////////////////////////////////////////////
#-----------------------------ARBOL ORDENADO------------------------------
#/////////////////////////////////////////////////////////////////////////

def buscarABB(ele,arbol):
    if arbol==[]:
        return False
    elif raiz(arbol)==ele:
        return True
    elif raiz(arbol)>ele:
        return buscarABB(ele,hijoizq(arbol))

def mayor(arbol):
    if arbol==[]:
        return "Error"
    elif hijoder(arbol)==[]:
        return raiz(arbol)
    else:
        return mayor(hijoder(arbol))
    
        return buscarABB(ele,hijoder(arbol))

def insertar(ele,arbol):
    if arbol==[]:
        return arbol+arbol[ele,[],[]]
    if raiz(arbol)>ele:
        return raiz(arbol)+insertar(ele,hijoder(arbol))
    else:
        return raiz(arbol)+insertar(ele,hijoizq(arbol))


def CantNodos(arbol):
    if arbol==[]:
        return 0
    else:
        return 1+ContNodos(hijoizq(arbol))+CantNodos(hijoder(arbol))

def altura(arbol):
    if arbol==[]:
        return 0
    else:
        return 1+max(altura(hijoizq(arbol))),(altura(hijoder(arbol)))

def mayor(arbol):
    if arbol==[]:
        return "Error"
    elif hijoder(arbol)==[]:
        return raiz(arbol)
    else:
        return mayor(hijoder(arbol))
    

#********************************#
#*ALGORITMO SEPARA FUNCIONES*****#
#********************************#

##CUENTA CANTIDAD DE UN STRING
##ENTRADA: STRING
##SALIDA: NUMERO
##RESTRICCIONES: STRING
def cantdig(string):
    len(string)
    return(len(string))


##ENTRADA DE RLISTA, CONVIERTE EN LISTA
##ENTRADA: STRING
##SALIDA: LISTA
##RESTRICCIONES: SOLO STRING DE EXPRESION MATEMATICA
def separador(string):
    final=[]
    cant=cantdig(string)
    for i in range(len(string)):
        if i==" ": #Error tiene que haber un espacio (Ya lo puse)
            cant-=1
            continue
        if cant>=2:
            if isoperador(string[i]+string[i+1])==True:
                final+=[string[i]+string[i+1]]
                cant-=1
                continue
            pass
        if  isnumero(string[i])==True:
            final+=[string[i]]
            cant-=1
            continue
        if isoperador(string[i])==True:
            final+=[string[i]]
            cant-=1
            continue
        if cant>3:
            if isoperador(string[i]+string[i+1]+string[i+2])==True:
                final+=[string[i]+string[i+1]+string[i+2]] #Arreglado
                cant-=1
                continue #Arreglado y agregado el continue y el pass diferente identacion
            pass
        cant-=1
    return list(rlista(final))

##CONVIERTE BIEN LA LISTA
##ENTRADA: LISTA
##SALIDA: LISTA
##RESTRICCIONES: SOLO LISTA
def rlista(lista):
    final=[]
    op=False
    for i in lista: 
        if  isnumero(i)==True:
            if op==False:
                final+=[i]
                op=True
            else:
                final[-1]+=str(i)## Aca había otro errorcito :P
        else:
            final+=[i] ## Aca estaba el error :) me imagino que este era :P
            op=False
    return final

##VE SI ES UN NUMERO
##ENTRADA: STRING
##SALIDA: BOOLEAN
##RESTRICCIONES:SOLO NUMEROS
def isnumero(i):
    i=str(i)
    for j in "0123456789":
        j=str(j)
        if j==i:
            return True
    else:
        return False
    

##VE SI ES UN OPERADOR
##ENTRADA: STRING
##SALIDA: BOOLEAN
##RESTRICCIONES: SOLO OPERADORES
def isoperador(i):
    for j in "+-*/^()":
        if j==i:
            return True
    for j in ["++","sq"]: ##SI ES UN OPERADOR DE 2 CARACTERES//sq = raiz cuadrada
        if j==i:
            return True
    for j in ["cos","sin","abs"]: ##VE SI ES UN OPERADOR DE TRES CARACTERES/abs= valos absoluto
        if j==i:
            return True
    return False


##NUMERO O NO
##ENTRADA: STRING
##SALIDA: BOOLEAN
##RESTRICCIONES: SOLO NUMEROS
def enumero(i):
    try:
        i=eval(i)
        if type(i)==int or type(i)==float:
            return True
        else:
            return False
    except:
        return False

##OPERACION DE 1 O 2 ENTRADAS// TRUE=1 ENTRADA EJ: SEN(20)// FALSE=2 ENTRY EJ:2+3
##ENTRADA: STRING
##SALIDA: BOOLEAN
##RESTRICCIONES: OPERADORES
def entradaop(i):
    if str(i) in ["cos","sin","abs","sq","++"]:
        return True
    else:
        return False

##CREA ARBOL
##ENTRADA: LISTA PULIDA
##SALIDA: LISTA
##RESTRICCIONES: SOLO LISTAS
def beginarbol(lista):
    lista=eval(str(lista))
    finalnums= []
    finaloperadores= [] 
    for i in lista:
        if enumero(i):
            finalnums+=[str(i)]
            continue
        else:
            if str(i) in ["(",")"]:
                continue
            else:
                if isoperador(i):
                    finaloperadores+=[str(i)]
                    continue
    return creararbol(finalnums,finaloperadores)


##CREA EL ARBOL
##ENTRADA: NUMEROS Y OPERADORES
##RESTRICCIONES: NUMEROS Y OPERADORES
def creararbol(num,op):
    num.reverse()
    op.reverse()
    final=[]
    inicio=0
    totalop=0 #ENTRADAS DE UN NUMERO
    while True:
        if op==[] and num==[]:
            return final
        elif final==[] or (inicio==0 and totalop==0):
            final=arbol(op[0],[],final)
            inicio=1
            if entradaop(op[0]):
                totalop=1
                op=op[1:]
                continue
            else:
                totalop=2
                op=op[1:]
                continue
        else:
            if hijoder(final)!=[] and hijoizq(final)!=[]:
                totalop-=1
                inicio=0
                continue
            else:
                final= addarbol(num[0],final)
                num=num[1:]
                totalop-=1
                if totalop==0:
                    inicio=0
                    continue
                else:
                    continue

##AGREGA UN ELEMENTO AL ARBOL
##ENTRADA: NUMERO, OPERADORES, ARBOL
##SALIDA: NUEVO ARBOL
##RESTRICCIONES: SOLO NUMEROS, OPERADORES Y ARBOLES
def addarbol(elemento,arb):
    if hijoizq(arb)==[]:
        return arbol(raiz(arb),elemento,hijoder(arb))
    else:
        return arbol(raiz(arb),hijoizq(arb),elemento)
            
    
                
##CONVIERTE EN STRING
##ENTRADA: LISTA
##SALIDA: STRING
##RESTRICCIONES: SOLO LISTAS
def tostring(lista, listares=[]):
    if lista==[]:
        return stringer(listares)
    elif lista[0]=="1" or lista[0]=="2" or lista[0]=="3" or lista[0]=="4" or lista[0]=="5" or lista[0]=="6" or lista[0]=="7" or lista[0]=="8" or lista[0]=="9" or lista[0]=="0":
        return tostring(lista[1:],listares+[int(lista[0])])
    else:
        return tostring(lista[1:],listares+[lista[0]])
    
def stringer(lista,resultado=""):
    for i in lista:
        resultado=resultado+str(i)
    return resultado

boton = Button(app,text="Estadísticas del árbol",bg="light blue",fg="magenta",command=estadísticas)
boton.place(x=170,y=200)
texto = Label(app,bg="#00FFFF",fg="black")
texto.config(font=("Arial 15 bold"))
texto.place(x=150,y=160)

var = IntVar()
R1 = Radiobutton(app,bg="#00FFFF", text="Infija", variable=var, value=1,command=cambiarlab1)
R1.place(x=190,y=85)

R2 = Radiobutton(app,bg="#00FFFF", text="Prefija", variable=var, value=2, command=cambiarlab2)
R2.place(x=190,y=105)

R3 = Radiobutton(app,bg="#00FFFF", text="Postfija", variable=var, value=3, command=cambiarlab3)
R2.place(x=190,y=105)

R3.place(x=190,y=125)






    


##app.mainloop()         
 
