segundos=0
minutos=0

import threading
import time
from tkinter import *
from tkinter import messagebox
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
                    #retroceso.set("Valor:"+str(cont)) Blue Tron #18CAE6
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
    lt=Label(ventana,font ="Consolas 20",bg="black",fg="#DF740C")
    lt.place(x=40,y=25)
    ly=Label(ventana,font="Consolas 20",bg="black",fg="#6FC3DF")
    ly.place(x=20,y=25)
    t=Button(ventana,text="Inicio",command=llamar_temp2)
    t.place(x=20,y=50)
    ventana.config(bg="black")
    ventana.deiconify()
    ventana.mainloop()
