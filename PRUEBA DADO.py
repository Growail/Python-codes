from tkinter import *
import time
import random
X=300
Y=100




def dale():
    i=random.randrange(1,6)
    linea= canvas.create_rectangle(3,260,1,400, outline="red", fill='red')
    number=Label(root)
    number.config(bg='black', height='10', width='0')
    number.place(x=280,y=200)

    

root=Tk()
root.geometry('500x500')
canvas=Canvas(root, width=1, height=1)
global X
global Y
canvas.config(bg="black")
canvas.place(x=X,y=Y)



