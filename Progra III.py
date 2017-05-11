from tkinter import *
from math import*
arbolactual=[]

app = Tk()
app.title("Evaluador de expresiones")
app.geometry("900x800")
app.resizable(True,True)
app.config(bg="#771100")


lab=Label(app,text="Evalúe su expresión:", bg="#771100", font=("Verdana"),fg="#000000").pack()

def estadísticas1():
    global arbolactual
    doc=open('arbol.txt')
    arbolactual=doc.read()
    doc=open('arbol.txt')
    arbol=doc.read()
##    print(beginarbol(separador(arbol)))
    laresult = Label(app,text="Resultado:",bg="#771100", font=("Times 20 italic"))
    laresult.place(x=5,y=63)
    lare = Label(app,text=eval(arbol),bg="#771100", font=("Times 20 italic"))
    lare.place(x=135,y=63)
    lap=Label(app,text="Prefija:",bg="#771100", font=("Times 20 italic"))
    lap.place(x=5,y=95)
    lapre=Label(app,text=preOrden(beginarbol(separador(arbol))),  bg="#771100", font=("Times 20 italic"))
    lapre.place(x=93,y=95)
    lapo=Label(app,text="Postfija:",bg="#771100", font=("Times 20 italic"))
    lapo.place(x=5,y=130)
    lapost=Label(app,text=postOrden(beginarbol(separador(arbol))),  bg="#771100", font=("Times 20 italic"))
    lapost.place(x=105,y=130)
    laa=Label(app,text="Infija (con paréntesis):",bg="#771100", font=("Times 20 italic"))
    laa.place(x=5,y=165)
    laarbol=Label(app, text=arbol,  bg="#771100", font=("Times 20 italic"))
    laarbol.place(x=270,y=165)
    laac=Label(app,text="Infija (sin paréntesis):",bg="#771100", font=("Times 20 italic"))
    laac.place(x=5,y=200)
    lain=Label(app,text=inOrden(beginarbol(separador(arbol))),  bg="#771100", font=("Times 20 italic"))
    lain.place(x=260,y=200)
    bot =Button(app,text="Visualizar!",bg="silver",fg="red",command=graficar).place(x=430,y=240)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def graficar():
    global arbolactual
    arbolactual=unify()
    try:
        nodo0 = Label(app,text=arbolactual[0],bg="#771100",fg='light blue',font=("Times 12 bold")).place(x=430,y=270)
    except:
        print('None')
    try:
        nodo1 = Label(app,text=arbolactual[1],bg="#771100",fg='light blue',font=("Times 12 bold")).place(x=390,y=300)
    except:
        print('None')
    try:
        nodo2 = Label(app,text=arbolactual[2],bg="#771100",fg='light blue',font=("Times 12 bold")).place(x=470, y=300)
    except:
        print('None')
    try:
        nodo3 = Label(app,text=arbolactual[3],bg="#771100",fg='light blue',font=("Times 12 bold")).place(x=430,y=330)
    except:
        print('None')
    try:
        nodo4 = Label(app,text=arbolactual[4],bg="#771100",fg='light blue',font=("Times 12 bold")).place(x=510,y=330)
    except:
        print('None')
    try:
        nodo5 = Label(app,text=arbolactual[5],bg="#771100",fg='light blue',font=("Times 12 bold")).place(x=470,y=360)
    except:
        print('None')
    try:
        nodo6 = Label(app,text=arbolactual[6],bg="#771100",fg='light blue',font=("Times 12 bold")).place(x=550,y=360)
    except:
        print('None')
    try:
        nodo7 = Label(app,text=arbolactual[7],bg="#771100",fg='light blue',font=("Times 12 bold")).place(x=510,y=390)
    except:
        print('None')
    try:
        nodo8 = Label(app,text=arbolactual[8],bg="#771100",fg='light blue',font=("Times 12 bold")).place(x=590,y=390)
    except:
        print('None')
    try:
        nodo9 = Label(app,text=arbolactual[9],bg="#771100",fg='light blue',font=("Times 12 bold")).place(x=550,y=420)
    except:
        print('None')
    try:
        nodo10 = Label(app,text=arbolactual[10],bg="#771100",fg='light blue',font=("Times 12 bold")).place(x=630,y=420)
    except:
        print('None')
    try:
        nodo11 = Label(app,text=arbolactual[11],bg="#771100",fg='light blue',font=("Times 12 bold")).place(x=590,y=450)
    except:
        print('None')
    try:
        nodo12 = Label(app,text=arbolactual[12],bg="#771100",fg='light blue',font=("Times 12 bold")).place(x=670,y=450)
    except:
        print('None')
    try:
        nodo13 = Label(app,text=arbolactual[13],bg="#771100",fg='light blue',font=("Times 12 bold")).place(x=630,y=480)
    except:
        print('None')
    try:
        nodo14 = Label(app,text=arbolactual[14],bg="#771100",fg='light blue',font=("Times 12 bold")).place(x=710,y=480)
    except:
        print('None')
    try:
        nodo15 = Label(app,text=arbolactual[15],bg="#771100",fg='light blue',font=("Times 12 bold")).place(x=670,y=510)
    except:
        print('None')
    try:
        nodo16 = Label(app,text=arbolactual[16],bg="#771100",fg='light blue',font=("Times 12 bold")).place(x=750,y=510)
    except:
        print('None')
    try:
        nodo17 = Label(app,text=arbolactual[17],bg="#771100",fg='light blue',font=("Times 12 bold")).place(x=710,y=540)
    except:
        print('None')
    try:
        nodo18 = Label(app,text=arbolactual[18],bg="#771100",fg='light blue',font=("Times 12 bold")).place(x=790,y=540)
    except:
        print('None')
    try:
        nodo19 = Label(app,text=arbolactual[19],bg="#771100",fg='light blue',font=("Times 12 bold")).place(x=750,y=570)
    except:
        print('None')
    try:
        nodo20 = Label(app,text=arbolactual[20],bg="#771100",fg='light blue',font=("Times 12 bold")).place(x=830,y=570)
    except:
        print('None')
    try:
        nodo21 = Label(app,text=arbolactual[21],bg="#771100",fg='light blue',font=("Times 12 bold")).place(x=710,y=600)
    except:
        print('None')
    try:
        nodo22 = Label(app,text=arbolactual[22],bg="#771100",fg='light blue',font=("Times 12 bold")).place(x=870,y=600)
    except:
        print('None')
    
def unify():
    global arbolactual
    arbolactual=preOrden(beginarbol(separador(arbolactual)))
    result=[]
    result2=[]
    for i in arbolactual:
        if type(i)!=list:
            result=result+[i]
        else:
            for j in i:
                result=result+[j]
    for i in result:
        if i=='(' or i==')':
            continue
        else:
            result2=result2+[i]
    arbolactual=result2
    return result2

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


#ARBOL ORDENADO


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
        return arbol[ele,[],[]]
    if raiz(arbol)>ele:
        return insertar(raiz(arbol),hijoizq(ele,arbol),hijoder(arbol))
    else:
        return insertar(raiz(arbol),hijoizq(arbol), hijoder(ele,arbol))


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
    


#*ALGORITMO SEPARA FUNCIONES



def cantdig(string):
    len(string)
    return(len(string))



def separador(string):
    final=[]
    cant=cantdig(string)
    for i in range(len(string)):
        if i==" ":
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
                final+=[string[i]+string[i+1]+string[i+2]] 
                cant-=1
                continue 
            pass
        cant-=1
    return list(rlista(final))


def rlista(lista):
    final=[]
    op=False
    for i in lista: 
        if  isnumero(i)==True:
            if op==False:
                final+=[i]
                op=True
            else:
                final[-1]+=str(i)
        else:
            final+=[i] 
            op=False
    return final


def isnumero(i):
    i=str(i)
    for j in "0123456789":
        j=str(j)
        if j==i:
            return True
    else:
        return False
    


def isoperador(i):
    for j in "+-*/^()":
        if j==i:
            return True
    for j in ["++","sq"]: 
        if j==i:
            return True
    for j in ["cos","sin","abs"]: 
        if j==i:
            return True
    return False



def enumero(i):
    try:
        i=eval(i)
        if type(i)==int or type(i)==float:
            return True
        else:
            return False
    except:
        return False


def entradaop(i):
    if str(i) in ["cos","sin","abs","sq","++"]:
        return True
    else:
        return False

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

def creararbol(num,op):
    num.reverse()
    op.reverse()
    final=[]
    inicio=0
    totalop=0 
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


def addarbol(elemento,arb):
    if hijoizq(arb)==[]:
        return arbol(raiz(arb),elemento,hijoder(arb))
    else:
        return arbol(raiz(arb),hijoizq(arb),elemento)
            
    

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

boton = Button(app,text="Evaluar!",bg="silver",fg="red",command=estadísticas1)
boton.pack()

app.mainloop()         
