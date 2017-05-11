import tkinter
from tkinter import *
import time
import random

largo=0
ancho=0
X=0
Y=0
matriz=[[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]

temporal=[[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]

bifurcador=True

def redirect(fila,columna):
    global temporal
    global bifurcador
    if bifurcador==True:
        bifurcador=False
        check(fila,columna)
    elif checkfinal(fila,columna):
        bifurcador=True
    elif checkfinal2(fila,columna):
        bifurcador=True
    else:
        print("Movimento Inválido")

                  
def cambionumero(fila,columna):
    global temporal
    temporal[fila][columna]=1
    print (temporal)

def check(fila,columna):
    global temporal
    global matriz
    matriz[fila][columna]=1
    temporal[fila][columna]=1
    print('b',matriz)

def check2(fila,columna):
    global temporal
    global matriz
    matriz[fila][columna]=1
    temporal=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    print('b2',matriz)

def checkfinal(fila, columna):
    global temporal
    print("a",temporal)
    cont=0
    cont2=0
    for i in temporal:
        if cont==fila:
            for j in i:
                try:
                    if cont2==columna:
                            if i[cont2+1]==1 or i[cont2-1]==1:
                                temporal[fila][columna]=1
                                check2(fila,columna)
                                return True
                    elif cont2==columna and cont2==0:
                        if j==1:
                            temporal[fila][columna]=1
                            check2(fila,columna)
                            return True
                    else:
                            cont2+=1
                except:
                    try:
                        if cont2==columna:
                            if i[cont2-1]==1:
                                temporal[fila][columna]=1
                                check2(fila,columna)
                                return True
                        elif cont2==columna and cont2==0:
                            if j==1:
                                temporal[fila][columna]=1
                                check2(fila,columna)
                                return True
                        else:
                                cont2+=1
                    except:
                        if cont2==columna:
                            if i[cont2+1]==1:
                                temporal[fila][columna]=1
                                check2(fila,columna)
                                return True
                        elif cont2==columna and cont2==0:
                            if j==1:
                                temporal[fila][columna]=1
                                check2(fila,columna)
                                return True
                        else:
                                cont2+=1
                        
                
        else:
            cont+=1


def checkfinal2(fila, columna):
    global temporal
    cont=0
    for i in temporal:
        if cont==fila:
            try:
                if matriz[cont-1][columna]==1:
                    temporal[fila][columna]=1
                    check2(fila,columna)
                    return True
                else:
                    cont+=1
            except:
                try:
                    if matriz[cont+1][columna]==1:
                        temporal[fila][columna]=1
                        check2(fila,columna)
                        return True
                    else:
                        cont+=1
                except:
                    cont+=1
                    
        else:
                cont+=1
                            
def transpuesta(matriz):
    temp=[]
    result=[]
    while matriz[0]!=[]:
        for i in matriz:
            temp=temp+[i[0]]
            i=i.remove(i[0])
        result=result+[temp]
        temp=[]
    return result


def check_linea():
    global matriz
    for i in range(0,4):
        for j in range(1,4):
            if matriz[i][j]==1 and matriz[i][j-1]==1:
                try:
                    if matriz[i+1][j]==1 and matriz[i+1][j-1]==1:
                        return "e"
                except:
                    continue
            else:
                continue
    return 6
                
           
        
        
        
            
                
app = tkinter.Tk()

def acerca():
    top = Toplevel()
    top.title("Sobre...")
    top.geometry("200x100")
    top.config(bg="black")
    mensaje1 = Label(top, text="Timbriche matemático",bg='black',fg='orange')
    mensaje1.place(x=1,y=1)
    mensaje2 = Label(top,text='Hecho por:')
    mensaje2.place(x=1,y=20)
    mensaje2.config(bg="black",fg='white')
    mensaje3= Label(top,text='Steven Ramos\n Estudiante del ITCR')
    mensaje3.place(x=10,y=40)
    mensaje3.config(bg="black",fg='white')

    
def reglas():
    top = Toplevel()
    top.title("Reglas")
    top.geometry("305x240")
    top.config(bg="black")
    titulo =Label(top,text='Reglas:',bg='black',fg='orange')
    titulo.place(x=1,y=1)
    mensaje = Label(top, text="1. Este juego está diseñado para dos jugadores.\n2. Solo pueden conectarse dos puntos adyacentes.\n3. Gana el jugador que haya completado más cuadrados")
    mensaje.place(x=1,y=20)
    mensaje.config(bg="black",fg='white')

    
def trigger(e1,e2):
    global largo
    global ancho
    global X
    global Y
    print(X)
    if X==0:
        return 3
    elif Y==0:
        return 4
    elif largo==0 and ancho==0:
        return 2
    else:
        X=e1
        Y=e2
        return crear_label()

    
def crear_label():
    global largo
    global ancho
    global X
    global Y
    label=Label(app)
    label.config(width=ancho, height=largo, bg='white')
    label.place(x=X,y=Y)
    largo=0
    ancho=0
    X=0
    Y=0

def cambiarvalores(l1,a1,x1,y1):
    global largo
    global ancho
    global X
    global Y
    largo=l1
    ancho=a1
    X=x1
    Y=y1
    crear_label()
    
def reset():
    global largo
    global ancho
    global X
    global Y
    global matriz
    global temporal
    largo=0
    ancho=0
    X=0
    Y=0
    matriz=[[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]

    temporal=[[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]

    
app.title("Timbiriche matemático")
barra_menu=Menu(app)
archivo=Menu(barra_menu)
archivo.add_command(label='Reglas',command=reglas)
archivo.add_separator()
archivo.add_command(label='Sobre el programador',command=acerca)
app.config(menu=barra_menu)
barra_menu.add_cascade(label="Nuevo Juego",command=reset)
barra_menu.add_cascade(label="Ayuda", menu=archivo)
app.geometry("450x380")
app.resizable(False, False)
app.config(bg='black')
marcador1= Label(app, text="Jugador 1:", bg="black", fg="white" )
marcador1.place(x=343, y=100)
numero1 = Label(app, text="0", bg="black", fg="white")
numero1.place(x=415,y=100)
marcador2= Label (app, text="Jugador 2:", bg="black", fg="orange")
marcador2.place(x=343, y=150)
numero2=Label(app, text="0",bg="black",fg="orange")
numero2.place(x=415,y=150)
punto01 = Button(app, text="°", bg="black", fg="white", bd="0", height="1", width="2", cursor='X_cursor')
punto01.place(x=50,y=50)
punto02 = Button(app, text="°", bg="black", fg="white", bd="0", height="1", width="2", cursor='X_cursor')
punto02.place(x=130,y=50)
punto03 = Button(app, text="°", bg="black", fg="white", bd="0", height="1", width="2", cursor='X_cursor')
punto03.place(x=210,y=50)
punto04 = Button(app, text="°", bg="black", fg="white", bd="0", height="1", width="2", cursor='X_cursor')
punto04.place(x=290,y=50)
punto11 = Button(app, text="°", bg="black", fg="white", bd="0", height="1", width="2", cursor='X_cursor')
punto11.place(x=50,y=130)
punto12 = Button(app, text="°", bg="black", fg="white", bd="0", height="1", width="2", cursor='X_cursor')
punto12.place(x=130,y=130)
punto13 = Button(app, text="°", bg="black", fg="white", bd="0", height="1", width="2", cursor='X_cursor')
punto13.place(x=210,y=130)
punto14 = Button(app, text="°", bg="black", fg="white", bd="0", height="1", width="2", cursor='X_cursor')
punto14.place(x=290,y=130)
punto21 = Button(app, text="°", bg="black", fg="white", bd="0", height="1", width="2", cursor='X_cursor')
punto21.place(x=50,y=210)
punto22 = Button(app, text="°", bg="black", fg="white", bd="0", height="1", width="2", cursor='X_cursor')
punto22.place(x=130,y=210)
punto23 = Button(app, text="°", bg="black", fg="white", bd="0", height="1", width="2", cursor='X_cursor')
punto23.place(x=210,y=210)
punto24 = Button(app, text="°", bg="black", fg="white", bd="0", height="1", width="2", cursor='X_cursor')
punto24.place(x=290,y=210)
punto31 = Button(app, text="°", bg="black", fg="white", bd="0", height="1", width="2", cursor='X_cursor')
punto31.place(x=50,y=290)
punto32 = Button(app, text="°", bg="black", fg="white", bd="0", height="1", width="2", cursor='X_cursor')
punto32.place(x=130,y=290)
punto33 = Button(app, text="°", bg="black", fg="white", bd="0", height="1", width="2", cursor='X_cursor')
punto33.place(x=210,y=290)
punto34 = Button(app, text="°", bg="black", fg="white", bd="0", height="1", width="2", cursor='X_cursor')
punto34.place(x=290,y=290)


app.mainloop()
