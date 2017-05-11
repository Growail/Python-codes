fechas=[]
juegos=[]
teams=[]
ganado=3
empatado=1
numerodefecha=1
goles=0
goleadores=[]
grupotabla=[]
import itertools
import tkinter
from tkinter import *

def a():
    l=[0,1,2,3,4,5,6,7,8,9]
    for i in range(0,5):
        print(l[i])
def calendario(entrada):
    global teams
    n=0
    for i in entrada:
        teams+=[[i,0,0,0,0,0,0,0,0,n]]
        n+=1
    entrada=list(itertools.permutations(entrada,2))
    global final
    global total
    global numerodefecha
    total=[]
    final=[]
    return fecha(entrada)

def fecha(entrada):
    global fechas
    global juegos
    global teams
    global numerodefecha
    cont=[]
    fecha1=[]
    fecha2=[]
    if entrada==[]:
        return
    for i in entrada:
        if i[0] not in cont:
            if i[1] not in cont:
##                teams+=[]
                cont+=[i[0]]+[i[1]]
                fecha1+=[[i[0],i[1],"0","0"]]
                fecha2+=[[i[0],"VS",i[1]]]
                entrada.remove(i)
            else:
                pass
        else:
            pass
    fechas+=[fecha2]
    juegos+=fecha1
    print("Fecha",numerodefecha,"  ",fecha2)
    numerodefecha+=1
    return fecha(entrada)
def registrarresultados(local,gl,visita,gv):
        global juegos
        global teams
        for i in juegos:
            if i[0]==local and i[1]==visita:
                i[2]=gl
                i[3]=gv
                return 
            else:
                pass
        print("Ese partido no existe")
 


def sumar_ya():
    global juegos
    global teams
    for i in juegos:
##        print(i)
##        print(i[0])
##        print(i[2])
##        print(i[1])
##        print(i[3])
        sumar_a_la_tabla(i[0],i[2],i[1],i[3])
        
def sumar_a_la_tabla(local,gl, visita,gv):
    global juegos
    global teams
    global ganado
    global empatado
    gl=int(gl)
    gv=int(gv)
    for i in juegos:
        if i[0]==local and i[1]==visita:
            i[2]=gl
            i[3]=gv
            for i in teams:
                if gl>gv:
                    for i in teams:
                        if i[0]==local:
                            i[1]+=1
                            i[2]+=1
                            i[5]+=gl
                            i[6]+=gv
                            i[7]+=(gl-gv)
                            i[8]+=ganado
                        elif i[0]==visita:
                            i[1]+=1
                            i[3]+=1
                            i[5]+=gv
                            i[6]+=gl
                            i[7]+=(gv-gl)
                    return teams
                elif gl<gv:
                    for i in teams:
                        if i[0]==local:
                                i[1]+=1
                                i[3]+=1
                                i[5]+=gl
                                i[6]+=gv
                                i[7]+=(gl-gv)
                        elif i[0]==visita:
                                i[1]+=1
                                i[2]+=1
                                i[5]+=gv
                                i[6]+=gl
                                i[7]+=(gv-gl)
                                i[8]+=ganado
                    return teams
                elif gl==gv:
                        for i in teams:
                            if i[0]==local:
                                i[1]+=1
                                i[4]+=1
                                i[5]+=gl
                                i[6]+=gv
                                i[7]+=(gl-gv)
                                i[8]+=empatado
                            elif i[0]==visita:
                                i[1]+=1
                                i[4]+=1
                                i[5]+=gv
                                i[6]+=gl
                                i[7]+=(gv-gl)
                                i[8]+=empatado
                        return teams          
        else:
            pass
    print("Ese partido no existe")

def consultarresultado(local,visita):
    global juegos
    for i in juegos:
        if i[0]==local and i[1]==visita:
            print(local,i[2])
            print(visita,i[3])
            return juegos
        else:
            pass
    print("Ese partido no existe")

def eliminarresultado(local,visita):
    global juegos
    for i in juegos:
        if i[0]==local and i[1]==visita:
            if input("Seguro?")=="1":
                i[2]="-"
                i[3]="-"
                return juegos
        else:
            pass
    print("Ese partido no existe")

def goles1(cantidad):
    global goles
    global goleadores
    goles=cantidad
    if goles==0:
        goleadores.sort(reverse=True)
        return goleadores
    else:
        mae=input("Quién lo metió? ")
        if goleadores==[]:
            goleadores+=[[1,mae]]
            return goles1(cantidad-1)
        for i in goleadores:
            if i[1]==mae:
                i[0]+=1
                return goles1(cantidad-1)
        goleadores+=[[1,mae]]
        return goles1(cantidad-1)

def tablafinal():
    global teams
    temp=[]
    for i in teams:
        temp+=[[[i[8]]+[i[7]]+i]]
    teams=temp
    teams.sort(reverse=True)
    return tablaaux()
def tablaaux():
    global teams
    temp2=[]
    for i in teams:
        temp2+=[i[0][2:]]
    teams=temp2
    return teams
##def tablafinal():
##    global teams
##    global grupotabla
##    grupotabla=[]
##    for i in teams:
##        grupotabla+=[[i[8],i[7],i[9]]]
##    grupotabla.sort(reverse=True)
##    return tablaaux()
##def tablaaux():
##    temp=[]
##    global grupotabla
##    global teams
##    if grupotabla==[]:
##        teams=temp
##        print(teams)
##        return teams
##    for i in teams:
##        if grupotabla[0][2]==i[9]:
##            temp+=[i]
##            grupotabla[1:]
##            return tablaaux()
        
        
## registrarresultados("CRC",2,"URU",0)
##>>> registrarresultados("CRC",2,"USA",0)
##>>> registrarresultados("URU",2,"USA",0)
##>>> registrarresultados("URU",2,"CRC",0)
##>>> registrarresultados("USA",2,"CRC",2)
##>>> registrarresultados("USA",2,"URU",4)   
##    
    
def pestañagoles():
        def goles1():
            global goles
            global goleadores
            if goles==0:
                anotadores.destroy()
##                resultados.deiconify()
                goleadores.sort(reverse=True)
                return goleadores
            else:
                mae=maesillo.get()
                if goleadores==[]:
                    goleadores+=[[1,mae]]
                    goles-=1
                    anotadores.destroy()
                    return pestañagoles()
                for i in goleadores:
                    if i[1]==mae:
                        i[0]+=1
                        goles-=1
                        anotadores.destroy()
                        if goles==0:
            ##                resultados.deiconify()
                            goleadores.sort(reverse=True)
                            return goleadores
                        return pestañagoles()
                goleadores+=[[1,mae]]
                goles-=1
                anotadores.destroy()
                return pestañagoles()
        anotadores=Tk()
        anotadores.title("Anotadores")
        anotadores.geometry("400x200")
        anotadores.resizable(False,False)
        anotadores.config(bg="green")
        l=Label(anotadores,text="Ingrese el nombre del anotador y el minuto",bg="green",font="Times 14 underline").place(x=10,y=10)
        maesillo=Entry(anotadores,font="Arial 14 italic",width=30)
        maesillo.place(x=10,y=40)
        otro=Entry(anotadores,font="Arial 14 italic",width=10).place(x=10,y=80)
        bt=Button(anotadores,text="Añadir",command=goles1).place(x=100,y=120)
