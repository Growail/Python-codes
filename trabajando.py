from tkinter import *
from tkinter import messagebox
import threading
import time
boton=[]
matriz=[]
filas=0
reloj=0
posicion=0
sonido=0
ancho=0
largo=0
fil=""
col=""
segundos=0
minutos=0
inicio=False
pausa=True
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
        elif reloj==1:
            algo2()
#funcion para seleccionar un nivel#
def nivel_seleccionado():
    global filas
    nivel=Tk()
    nivel.geometry("400x400")
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
    
    def valor():
        global filas,ancho,largo
        numero=num.get()
        if numero==3:
            filas=3
            ancho=10
            largo=5
        elif numero==4:
            filas=4
            ancho=8
            largo=5
        elif numero==5:
            filas=5
            ancho=7
            largo=4
        elif numero==6:
            filas=6
            ancho=5
            largo=3
        elif numero==7:
            filas=7
            ancho=4
            largo=2
        elif numero==8:
            filas=8
            ancho=3
            largo=2
        elif numero==9:
            filas=9
            ancho=3
            largo=2
    def continuar():
        numero=num.get()
        a=messagebox.askquestion("Cancelar","Desea continuar")
        if a== "yes" and numero !=0:
            valor()
            nivel.destroy()
            activar_reloj()
        elif a=="no":
            nivel.destroy()
            main()
            
        elif numero ==0:
            messagebox.showerror("Verifique los datos","Debe seleccionar una opcion.")
        
    buton=Button(nivel,text="Continuar",font="Arial 16",bg="green",command=continuar).place(x=150,y=310)
    nivel.mainloop()
def nuevo_tiempo():
    nuevo=Tk()
    nuevo.geometry("400x250")
    nuevo.config(bg="white")
    X3=Entry(nuevo,bg="black",fg="white")
    X3.place(x=140,y=40)
    def continuar():
        global segundos
        num=X3.get()
        if type(eval(num))!=int:
            messagebox.showerror("Error","Debe Ser un entero")
        elif eval(num)<=0:
            messagebox.showerror("Error","Debe Ser mayor que 0")
        else:
            segundos=int(num)
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
        numero=ele.get()
        a=messagebox.askquestion("Cancelar","Desea continuar")
        if numero==0:
            messagebox.showerror("Error","Debe seleccionar una opcion")
        elif a== "yes" and numero ==1:
            crear_tiempo()
            deci.destroy()
            posicion_botones()
        elif a== "yes" and numero ==2:
            deci.destroy()
            nuevo_tiempo()
        elif a=="no":
            deci.destroy()
            main()
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
    def algo2():
        global segundos
    ##    segundos=seg
        ventana=Tk()
        ventana.geometry("300x250")
        ventana.title("Hilos")
        def tempor2():
            global segundos
            global minutos
            while minutos>=0:
                while segundos>=0:
                    lt.config(text=segundos)
                    ly.config(text=minutos)
                        #retroceso.set("Valor:"+str(cont))
                    segundos+=1
                    time.sleep(1)
                    if segundos==60:
                        minutos+=1
                        segundos=0
                messagebox.showerror("Error","su tiempo se acabo")
                
        def llamar_temp2():
            t.destroy()
            b=threading.Thread(target=tempor2,name="Temporizador",args=())
            b.start()
        lt= Label(ventana)
        lt.place(x=40,y=25)
        ly=Label(ventana)
        ly.place(x=20,y=25)
        t=Button(ventana,text="Inicio",command=llamar_temp2)
        t.place(x=20,y=50)
        ventana.deiconify()
        ventana.mainloop()
    def valor():
        global filas,segundos,reloj
        numero=var.get()
        if numero==1:
            reloj=1
            algo2()
        elif numero==2:
            reloj=2
        elif numero==3:
            reloj=3
            
    def continuar():
        numero=var.get()
        a=messagebox.askquestion("Cancelar","Desea continuar")
        if a== "yes" and (numero ==1 or numero==2):
            valor()
            activado.destroy()
            posicion_botones()
        elif a== "yes" and numero ==3:
            valor()
            activado.destroy()
            decidir_tiempo()
        elif a=="no":
            activado.destroy()
            main()
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
        a=messagebox.askquestion("Cancelar","Desea continuar")
        if a== "yes" and numero !=0:
            valor()
            pos.destroy()
            activar_volumen()
        elif a=="no":
            pos.destroy()
            main()
            
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
        a=messagebox.askquestion("Cancelar","Desea continuar")
        if a== "yes" and numero !=0:
            valor()
            song.destroy()
        elif a=="no":
            main()
            song.destroy()
        elif numero ==0:
            messagebox.showerror("Verifique los datos","Debe seleccionar una opcion.")
    buton=Button(song,text="Continuar",font="Arial 16",bg="green",command=continuar).place(x=150,y=170)
    song.mainloop()


def crear_matriz_logica():
    global matriz
    for i in range(filas):
        matriz.append([0]*filas)
    return
def crear_matriz_botones():
    global boton
    for i in range(filas):
        boton.append([0]*filas)
    return
def pantalla():
    juego=Tk()
    juego.geometry("570x570")
    
    def botones():
        global matriz,ancho,largo
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                btn = Button(juego,bg="white",width=ancho,height =largo,command=lambda a=i,b=j :[seleccionado(a,b)])
                # se coloca el boton en la matriz, en la posicion i,j
                btn.grid(row=i+1, column=j+1)
                boton[i][j] = btn
    def seleccionado(i,j):
        global boton,fil,col,inicio
        if inicio==False:
            messagebox.showerror("Error","Debe iniciar el juego.")
        elif inicio=="":
            messagebox.showerror("Error","El juego esta pausado.")
        else:
            fil=i
            col=j
            (boton[i][j]).config(bg="sky blue")
        
    def numeros():
        def numero1():
            global fil,col
            if col!="" and fil!="":
                matriz[fil][col]=1
                boton[fil][col].config(bg="white",text="1")
                fil=""
                col=""
            else:
                messagebox.showerror("Verifique los datos","Debe seleccionar una celda.")
        def numero2():
            global fil,col
            if col!="" and fil!="":
                matriz[fil][col]=2
                boton[fil][col].config(bg="white",text="2")
                fil=""
                col=""
            else:
                messagebox.showerror("Verifique los datos","Debe seleccionar una celda.")
        def numero3():
            global fil,col
            if col!="" and fil!="":
                matriz[fil][col]=3
                boton[fil][col].config(bg="white",text="3")
                fil=""
                col=""
            else:
                messagebox.showerror("Verifique los datos","Debe seleccionar una celda.")
        def numero4():
            global fil,col
            if col!="" and fil!="":
                matriz[fil][col]=4
                boton[fil][col].config(bg="white",text="4")
                fil=""
                col=""
            else:
                messagebox.showerror("Verifique los datos","Debe seleccionar una celda.")
        def numero5():
            global fil,col
            if col!="" and fil!="":
                matriz[fil][col]=5
                boton[fil][col].config(bg="white",text="5")
                fil=""
                col=""
            else:
                messagebox.showerror("Verifique los datos","Debe seleccionar una celda.")
        def numero6():
            global fil,col
            if col!="" and fil!="":
                matriz[fil][col]=6
                boton[fil][col].config(bg="white",text="6")
                fil=""
                col=""
            else:
                messagebox.showerror("Verifique los datos","Debe seleccionar una celda.")
        def numero7():
            global fil,col
            if col!="" and fil!="":
                matriz[fil][col]=7
                boton[fil][col].config(bg="white",text="7")
                fil=""
                col=""
            else:
                messagebox.showerror("Verifique los datos","Debe seleccionar una celda.")
        def numero8():
            global fil,col
            if col!="" and fil!="":
                matriz[fil][col]=8
                boton[fil][col].config(bg="white",text="8")
                fil=""
                col=""
            else:
                messagebox.showerror("Verifique los datos","Debe seleccionar una celda.")
        def numero9():
            global fil,col
            if col!="" and fil!="":
                matriz[fil][col]=9
                boton[fil][col].config(bg="white",text="9")
                fil=""
                col=""
            else:
                messagebox.showerror("Verifique los datos","Debe seleccionar una celda.")
        if filas==3 and posicion==2:
            boton1=Button(juego,text="1",width=5,height =3,command=numero1).place(x=10,y=10)
            boton2=Button(juego,text="2",width=5,height =3,command=numero2).place(x=10,y=70)
            boton3=Button(juego,text="3",width=5,height =3,command=numero3).place(x=10,y=130)
        elif filas==3 and posicion==1:
            boton1=Button(juego,text="1",width=5,height =3,command=numero1).place(x=500,y=10)
            boton2=Button(juego,text="2",width=5,height =3,command=numero2).place(x=500,y=70)
            boton3=Button(juego,text="3",width=5,height =3,command=numero3).place(x=500,y=130)
        elif filas==4 and posicion==2:
            boton1=Button(juego,text="1",width=5,height =3,command=numero1).place(x=10,y=10)
            boton2=Button(juego,text="2",width=5,height =3,command=numero2).place(x=10,y=70)
            boton3=Button(juego,text="3",width=5,height =3,command=numero3).place(x=10,y=130)
            boton4=Button(juego,text="4",width=5,height =3,command=numero4).place(x=10,y=190)
        elif filas==4 and posicion==1:
            boton1=Button(juego,text="1",width=5,height =3,command=numero1).place(x=500,y=10)
            boton2=Button(juego,text="2",width=5,height =3,command=numero2).place(x=500,y=70)
            boton3=Button(juego,text="3",width=5,height =3,command=numero3).place(x=500,y=130)
            boton4=Button(juego,text="4",width=5,height =3,command=numero4).place(x=500,y=190)
        elif filas==5 and posicion==2:
            boton1=Button(juego,text="1",width=5,height =3,command=numero1).place(x=10,y=10)
            boton2=Button(juego,text="2",width=5,height =3,command=numero2).place(x=10,y=70)
            boton3=Button(juego,text="3",width=5,height =3,command=numero3).place(x=10,y=130)
            boton4=Button(juego,text="4",width=5,height =3,command=numero4).place(x=10,y=190)
            boton5=Button(juego,text="5",width=5,height =3,command=numero5).place(x=10,y=250)
        elif filas==5 and posicion==1:
            boton1=Button(juego,text="1",width=5,height =3,command=numero1).place(x=500,y=10)
            boton2=Button(juego,text="2",width=5,height =3,command=numero2).place(x=500,y=70)
            boton3=Button(juego,text="3",width=5,height =3,command=numero3).place(x=500,y=130)
            boton4=Button(juego,text="4",width=5,height =3,command=numero4).place(x=500,y=190)
            boton5=Button(juego,text="5",width=5,height =3,command=numero5).place(x=500,y=250)
        elif filas==6 and posicion==2:
            boton1=Button(juego,text="1",width=5,height =3,command=numero1).place(x=10,y=10)
            boton2=Button(juego,text="2",width=5,height =3,command=numero2).place(x=10,y=70)
            boton3=Button(juego,text="3",width=5,height =3,command=numero3).place(x=10,y=130)
            boton4=Button(juego,text="4",width=5,height =3,command=numero4).place(x=10,y=190)
            boton5=Button(juego,text="5",width=5,height =3,command=numero5).place(x=10,y=250)
            boton6=Button(juego,text="6",width=5,height =3,command=numero6).place(x=10,y=310)
        elif filas==6 and posicion==1:
            boton1=Button(juego,text="1",width=5,height =3,command=numero1).place(x=500,y=10)
            boton2=Button(juego,text="2",width=5,height =3,command=numero2).place(x=500,y=70)
            boton3=Button(juego,text="3",width=5,height =3,command=numero3).place(x=500,y=130)
            boton4=Button(juego,text="4",width=5,height =3,command=numero4).place(x=500,y=190)
            boton5=Button(juego,text="5",width=5,height =3,command=numero5).place(x=500,y=250)
            boton6=Button(juego,text="6",width=5,height =3,command=numero6).place(x=500,y=310)
        elif filas==7 and posicion==2:
            boton1=Button(juego,text="1",width=4,height =2,command=numero1).place(x=10,y=10)
            boton2=Button(juego,text="2",width=4,height =2,command=numero2).place(x=10,y=55)
            boton3=Button(juego,text="3",width=4,height =2,command=numero3).place(x=10,y=100)
            boton4=Button(juego,text="4",width=4,height =2,command=numero4).place(x=10,y=145)
            boton5=Button(juego,text="5",width=4,height =2,command=numero5).place(x=10,y=190)
            boton6=Button(juego,text="6",width=4,height =2,command=numero6).place(x=10,y=235)
            boton7=Button(juego,text="7",width=4,height =2,command=numero7).place(x=10,y=280)
        elif filas==7 and posicion==1:
            boton1=Button(juego,text="1",width=4,height =2,command=numero1).place(x=500,y=10)
            boton2=Button(juego,text="2",width=4,height =2,command=numero2).place(x=500,y=55)
            boton3=Button(juego,text="3",width=4,height =2,command=numero3).place(x=500,y=100)
            boton4=Button(juego,text="4",width=4,height =2,command=numero4).place(x=500,y=145)
            boton5=Button(juego,text="5",width=4,height =2,command=numero5).place(x=500,y=190)
            boton6=Button(juego,text="6",width=4,height =2,command=numero6).place(x=500,y=235)
            boton7=Button(juego,text="7",width=4,height =2,command=numero7).place(x=500,y=280)
        elif filas==8 and posicion==2:
            boton1=Button(juego,text="1",width=4,height =2,command=numero1).place(x=10,y=10)
            boton2=Button(juego,text="2",width=4,height =2,command=numero2).place(x=10,y=55)
            boton3=Button(juego,text="3",width=4,height =2,command=numero3).place(x=10,y=100)
            boton4=Button(juego,text="4",width=4,height =2,command=numero4).place(x=10,y=145)
            boton5=Button(juego,text="5",width=4,height =2,command=numero5).place(x=10,y=190)
            boton6=Button(juego,text="6",width=4,height =2,command=numero6).place(x=10,y=235)
            boton7=Button(juego,text="7",width=4,height =2,command=numero7).place(x=10,y=280)
            boton8=Button(juego,text="8",width=4,height =2,command=numero8).place(x=10,y=325)
        elif filas==8 and posicion==1:
            boton1=Button(juego,text="1",width=4,height =2,command=numero1).place(x=500,y=10)
            boton2=Button(juego,text="2",width=4,height =2,command=numero2).place(x=500,y=55)
            boton3=Button(juego,text="3",width=4,height =2,command=numero3).place(x=500,y=100)
            boton4=Button(juego,text="4",width=4,height =2,command=numero4).place(x=500,y=145)
            boton5=Button(juego,text="5",width=4,height =2,command=numero5).place(x=500,y=190)
            boton6=Button(juego,text="6",width=4,height =2,command=numero6).place(x=500,y=235)
            boton7=Button(juego,text="7",width=4,height =2,command=numero7).place(x=500,y=280)
            boton8=Button(juego,text="8",width=4,height =2,command=numero8).place(x=500,y=325)
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
        

        
    label=Label(juego,text="                                     ")
    label.grid(row=0, column=0)

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
    def validar_columna():
        global matriz,boton,filas,pausa
        cont2=0
        cont=0
        resultado=0
        while cont2<len(matriz[cont]):
            lista=[]
            
            while cont<len(matriz):
                if matriz[cont][cont2] not in lista:
                    lista+=[matriz[cont][cont2]]
                    cont+=1
                    resultado+=1
                else:
                    boton[cont][cont2].config(bg="red")
                    cont+=1
            cont=0
            cont2+=1
        if resultado==(filas*filas):
            pausa=False
            messagebox.showinfo("Felicidades","Haz Ganado")
        else:
            messagebox.showerror("Error","Hay errores por corregir")
            
        return
    def tempor():
        global segundos,pausa
        cont=segundos
        print(pausa)
        while cont>=0:
            if pausa==True:
                lt.config(text=cont)
                    #retroceso.set("Valor:"+str(cont))
                cont-=1
                time.sleep(1)
            else:
                lt.config(text=cont)
        messagebox.showerror("Error","su tiempo se acabo")
    def llamar_temp():
        b=threading.Thread(target=tempor,name="Temporizador",args=())
        b.start()
    def inicio_juego():
        global inicio
        if inicio==True:
            messagebox.showerror("Error","El juego ya fue iniciado")
        else:
            inicio=True
    def star():
        inicio_juego()
        llamar_temp()
        
       
    lt= Label(juego)
    lt.place(x=20,y=510)
    t=Button(juego,text="Iniciar",command=star).place(x=40,y=530)
    boton_val=Button(juego,text="Validar",command=validar_fila).place(x=100,y=530)
    def reiniciar():
        global matriz,botones,segundos,inicio
        inicio=False
        matriz=[]
        boton=[]
        segundos=segundos
        crear_matriz_logica()
        crear_matriz_botones()
        juego.destroy()
        pantalla()

    reini=Button(juego,text="Reiniciar",command=reiniciar).place(x=160,y=530)
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
            
                    
    def boton_pausa():
        global reloj ,pausa,inicio
        if reloj==3 and pausa==True:
            pause=Button(juego,text="Pausar",command=pausar).place(x=80,y=490)
        
    numeros()
    botones()
    boton_pausa()
    juego.mainloop()


#pantalla principal#
def main():
    principal=Tk()
    principal.geometry("490x310")
    principal.title("Torneo de bola")
    principal. config(bg="yellow")
    principal.resizable(False,False)

    def validar1():
        principal.destroy()
        nivel_seleccionado()
    boton1= Button(principal,text="Configuración Del Juego",fg="red",font="Cosmic 14",bg="black",command=validar1).place(x=10,y=5)
    principal.mainloop()
