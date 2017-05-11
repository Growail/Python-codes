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
    arbol=input_tk.get()
    print(arbol)
boton = Button(app,text="Estadísticas del árbol",bg="light blue",fg="magenta",command=estadísticas)
boton.place(x=170,y=200)
texto = Label(app,bg="#00FFFF",fg="black")
texto.config(font=("Arial 15 bold"))
texto.place(x=150,y=160)
