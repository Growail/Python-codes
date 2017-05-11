import tkinter
from tkinter import *
stopflag=True

app=tkinter.Tk()
app.title("Inicio")
app.config(bg="green")
app.geometry("400x400")
app.resizable(False,False)
dadologo = PhotoImage(file="dado_5.png")
dado= Label(app, image=dadologo, width=120, height=120)
dado.place(x=150,y=50)

def dadomove():
    global stopflag
    cont=1
    while stopflag==True:
        if cont==1:
            cont=2
            dadologo = PhotoImage(file="dado_1.png")
            dado= Label(app, image=dadologo, width=120, height=120)
            dado.place(x=150,y=50)
        elif cont==2:
            cont=1
            dadologo = PhotoImage(file="dado_2.png")
            dado= Label(app, image=dadologo, width=120, height=120)
            dado.place(x=150,y=50)
            
darle = Button(app,text="Tirar!", cursor="X_cursor", command=dadomove)
darle.place(x=50,y=200)

