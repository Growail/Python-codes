#modulos
import ast
from ast import*
import tkinter
from tkinter import*
import threading
import time
import subprocess
import itertools
from itertools import*
import os
import platform

#globales
indice1 = 0
indice2 = 0
horas = 0
minutos = 0
segundos = 0
horas2 = 0
minutos2 = 0
segundos2 = 0
multiniv = 3
diccionario = {}
jugando = {}
inicio = False
reloj = False
tempo = False
elegido = False
especial = False
ya = False
mulniv = False
posicion = list()
juegos = list()
jugados = list()
maximos = list()
maximotempo = list()
matriz = [[[],[],[]],
          [[],[],[]],
          [[],[],[]]]
tablero = []
board = list()
hacer = list()
rehacer = list()
valores = []
alfabeto = [1,2,3,4,5,6,7,8,9]
operacion = ''

#funcion para salir de ventana de soluciones
def salirsolu():
    solulb.delete(0,END)
    solu.withdraw()
    

#funcion para agregar soluciones a tablero
def agregarsolucion():
    global posicion, jugando,board,tablero
    poner = eval(solulb.get(solulb.curselection()[0]))
    for i in list(jugando.keys()):
        if posicion in list(jugando[i]):
            posiciones = list(jugando[i])[1:]
            cont = 0
            for i in posiciones:
                board[i[0]][i[1]].invoke()
                colocar(poner[0][cont])
                cont +=1
            messagebox.showinfo(None,'La solucion ha sido implementada')
            return
        else:
            pass
            
    
#funcion que pone soluciones posibles en ventana de soluciones
def ponersoluciones(posibles):
    for i in posibles:
        solulb.insert(END,i)
    solu.deiconify()
    messagebox.showinfo(None,'Seleccione la solucion que desea ingresar')
    return

#funcion que genera soluciones posibles de juego       
def soluciones():
    global inicio,alfabeto,jugando,elegido,posicion,board,elegido
    if inicio == False:
        messagebox.showinfo(None,'El juego no ha empezado')
        return
    elif elegido == False:
        messagebox.showinfo(None,'Debe seleccionar una celda de una jaula')
        return
    else:
        board[posicion[0]][posicion[1]].config(image=jaula)
        elegido = False
        posicion = tuple(posicion)
        for i in list(jugando.keys()):
            if posicion in list(jugando[i]):
                if len(list(jugando[i])) == 2:
                    messagebox.showinfo(None,'No hay soluciones posibles para jaulas con numeros preestablecidos')
                    return
                else:
                    num = int(list(jugando[i])[0][0:-1])
                    operacion = (jugando[i][0][-1])
                    if operacion == 'x' or posicion == 'X':
                        operacion = '*'
                    cant = len(list(jugando[i]))-1
                    posibles = []
                    todos = list(itertools.product(alfabeto,repeat=cant))
                    for i in todos:
                        resuelva = ''
                        for j in i:
                            resuelva +=(str(j)+operacion)
                        resuelva = resuelva[0:-1]
                        if eval(resuelva) == num:
                            posibles.append([i])
                        else:
                            pass
                    return ponersoluciones(posibles)              
            else:
                pass

#ventana de soluciones posibles
solu = Toplevel()
solu.title('Soluciones posibles')
##solu.protocol('WM_DELETE_WINDOW',nosalir)
soluf = Frame(solu)
sols = Scrollbar(soluf)
sols.pack(side=RIGHT,fill=Y)
solulb = Listbox(soluf,selectmode=SINGLE)
sols['command'] = solulb.yview()
solulb['yscrollcommand'] = sols.set
sl = Label(solu,text='Estas son las soluciones posibles').pack()
soluf.pack()
solulb.pack()
solub = Button(solu,text='Poner solucion',command=agregarsolucion)
solub.pack()
solub2 = Button(solu,text='Listo',command=salirsolu)
solub2.pack()
solu.withdraw()
