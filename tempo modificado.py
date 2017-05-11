segundos=60
minutos=1

import threading
import time
from tkinter import *
from tkinter import messagebox
def algo(minu,seg):
    global segundos
    global minutos
    minutos=minu
    segundos=seg
    ventana=Tk()
    ventana.geometry("300x250")
    ventana.title("Hilos")
    def tempor():
        global segundos
        global minutos
        while minutos>=0:
            if minutos==0 and segundos==0:
                segundos=0
                lt.config(text=segundos)
                break
            while segundos>=0:
                lt.config(text=segundos)
                ly.config(text=minutos)
                    #retroceso.set("Valor:"+str(cont))
                if segundos==0:
                    minutos-=1
                    segundos=60
                segundos-=1
                time.sleep(1)
                if minutos==0 and segundos==0:
                    break
        messagebox.showerror("Error","su tiempo se acabo")
##        while segundos>=0:
##            lt.config(text=segundos)
##            #retroceso.set("Valor:"+str(cont))
##            segundos-=1
##            time.sleep(1)
##        messagebox.showerror("Error","su tiempo se acabo")
    def llamar_temp():
        b=threading.Thread(target=tempor,name="Temporizador",args=())
        b.start()
    lt= Label(ventana)
    lt.place(x=40,y=25)
    ly=Label(ventana)
    ly.place(x=20,y=25)
    t=Button(ventana,text="Temporizador",command=llamar_temp)
    t.place(x=20,y=50)
    ventana.mainloop()
