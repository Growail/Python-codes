import tkinter
from tkinter import *
actual={1: ('1-', (0, 0), (0, 1)), 2: ('3÷', (1, 0), (2, 0)), 3: ('1', (0, 2)), 4: ('6x', (1, 1), (1, 2)), 5: ('1-', (2, 1), (2, 2))}
def a():
    global actual
    stractual=str(actual)
    stractual=stractual[3:]
    temp=""
    actualprintable=[]
    for i in stractual:
        if i=="}":
            temp=temp[0:len(temp)]
            actualprintable+=[temp]
            temp=""
        elif i==":":
            temp=temp[0:len(temp)-2]
            actualprintable+=[temp]
            temp=""
        else:
            temp+=i
    master=Tk()
    master.resizable(False,False)
    master.title("Coordenadas")
    listbox=Listbox(master)
    listbox.pack()
    listbox.config(font="Consolas 16", width=30,bg="#121212",fg="white")
    listbox.insert(END, "Lista de jaulas y coordenadas")
    for i in actualprintable:
        listbox.insert(END, i)

