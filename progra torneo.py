from tkinter import *
from tkinter import messagebox
import itertools
nombre=""
participantes=0
par=0
clasifican=0
ganado=0
empatado=0
conflag=0
teamflag=0
calenflag=0
equipos=[]
codigos=[]
fechas=[]
juegos=[]
numerodefecha=1
goles=0
goleadores=[]
teams=[]
def put():
    if messagebox.askokcancel( title="Salir",message="Seguro que desea salir?"):
        main.destroy()

def configura():
    global conflag
    global nombre
    global participantes
    global clasifican
    global ganado
    global empatado
    if conflag==0:
        conflag=1
        main.withdraw()
        configuracion=Tk()
        configuracion.title("Ingrese las especificaciones del torneo")
        configuracion.config(bg="green")
        configuracion.geometry("420x400")
        configuracion.resizable(True,False)
        nombre=Label(configuracion,text="Nombre del torneo",bg="green",font="Arial 12").place(x=1,y=15)
        nombreaa=Entry(configuracion,font="Times 14",width=45)
        nombreaa.place(x=1,y=40)
        partici=Label(configuracion,text="Cantidad de equipos participantes",bg="green",font="Arial 12").place(x=1,y=70)
        particiaa=Entry(configuracion,font="Times 14",width=45)
        particiaa.place(x=1,y=95)
        clasifi=Label(configuracion, font="Arial 12",bg="green", text="Cantidad de equipos clasificados").place(x=1,y=130)
        clasifiaa=Entry(configuracion,font="Times 14",width=45)
        clasifiaa.place(x=1,y=155)
        pun=Label(configuracion, font="Arial 12",bg="green", text="Puntos por partido ganado").place(x=1,y=190)
        punaa=Entry(configuracion,font="Times 14",width=45)
        punaa.place(x=1,y=215)
        pune=Label(configuracion, font="Arial 12",bg="green", text="Puntos por partido empatado").place(x=1,y=250)
        puneaa=Entry(configuracion,font="Times 14",width=45)
        puneaa.place(x=1,y=275)
        def asignar():
            global nombre
            global participantes
            global par
            global clasifican
            global ganado
            global empatado
            if len(nombreaa.get())>=2 and len(nombreaa.get())<=40:
                if int(particiaa.get())%2==0:
                    if int(clasifiaa.get())>=1 and int(clasifiaa.get())<int(particiaa.get()):
                        if int(punaa.get())>=1:
                            if int(puneaa.get())>=1 and int(puneaa.get())<int(punaa.get()):
                                nombre=nombreaa.get()
                                participantes=int(particiaa.get())
                                par=int(particiaa.get())
                                clasifican=int(clasifiaa.get())
                                ganado=int(punaa.get())
                                empatado=int(puneaa.get())
                                configuracion.destroy()
                                main.deiconify()
                            else:
                                messagebox.showerror(title="Error",message="Los puntos asignados por empate no son válidos")
                        else:
                            messagebox.showerror(title="Error",message="Los puntos asignados por gane no son válidos")
                    else:
                        messagebox.showerror(title="Error",message="La cantidad de equipos clasificados no es válida")
                else:
                    messagebox.showerror(title="Error",message="La cantidad de equipos no es válida")
            else:
                messagebox.showerror(title="Error",message="El nombre del torneo no es válido")
                            
                                
        def aas():
            if messagebox.askokcancel( title="Cancelar",message="Seguro que desea cancelar?"):
                configuracion.destroy()
                main.wm_deiconify()
        aceptar=Button(configuracion,text="Aceptar",command=asignar,state="normal").place(x=60,y=335)
        cancelar=Button(configuracion,text="Cancelar",command=aas).place(x=310,y=335)
    else:
        configuracion=Tk()
        configuracion.title("Especificaciones del torneo")
        configuracion.config(bg="green")
        configuracion.geometry("400x200")
        configuracion.resizable(True,False)
        n=Label(configuracion,text="Nombre del torneo:",bg="green", font="Times 14 bold").place(x=1,y=10)
        p=Label(configuracion,text="Número de participantes:",bg="green", font="Times 14 bold").place(x=1,y=40)
        c=Label(configuracion,text="Número de clasificados:",bg="green", font="Times 14 bold").place(x=1,y=70)
        g=Label(configuracion,text="Puntos por partido ganado:",bg="green", font="Times 14 bold").place(x=1,y=100)
        e=Label(configuracion,text="Puntos por partido empatado:",bg="green", font="Times 14 bold").place(x=1,y=130)
        nombre=Label(configuracion,text=nombre,bg="green",font="Arial 12 italic").place(x=165,y=10)
        partici=Label(configuracion,text=participantes,bg="green",font="Arial 12 italic").place(x=213,y=40)
        clasifi=Label(configuracion, font="Arial 12 italic",bg="green", text=clasifican).place(x=205,y=70)
        pun=Label(configuracion, font="Arial 12 italic",bg="green", text=ganado).place(x=230,y=100)
        pune=Label(configuracion, font="Arial 12 italic",bg="green", text=empatado).place(x=250,y=130)
        cerrar=Button(configuracion,text="Cerrar",command=configuracion.destroy).place(x=190,y=170)

def adminequipos():
    if teamflag==0:
        def pestañaeliminar():
            def eliminar():
                if messagebox.askokcancel( title="Eliminar",message="Seguro que desea eliminar?"):
                    global equipos
                    global par
                    global codigos
                    flag=False
                    pos=0
                    for i in equipos:
                        if i[1]==codigoe.get():
                            equipos.remove(i)
                            codigos.remove(i[1])
                            par+=1
                            flag=True
                            eequipos.destroy()
                    if flag==False:
                        messagebox.showerror(title="Error",message="Este equipo no existe. No se puede eliminar")
                        eequipos.deiconify()
                else:
                    eequipos.destroy()
                    aequipos.deiconify()
            global codigos
            if len(codigos)==0:
                messagebox.showerror(title="Error",message="No puede escoger esta opción a menos que haya ingresado equipos antes")
                aequipos.deiconify()
            else:
    ##            aequipos.destroy()
                eequipos=Tk()
                eequipos.title("Modificación de equipos")
                eequipos.config(bg="green")
                eequipos.resizable(False,False)
                eequipos.geometry("300x300")
                codigo=Label(eequipos,text="Código del equipo a eliminar", bg="green",font="Verdana 12 bold underline ").place(x=20,y=20)
                codigoe=Entry(eequipos,font="Times 14 italic", width=20)
                codigoe.place(x=40,y=55)
                consulta=Button(eequipos,text="Eliminar",command=eliminar).place(x=60,y=180)
                salida=Button(eequipos,text="Cancelar",command=eequipos.destroy).place(x=190,y=180)
                
        def pestañamodificar():
            def modificar():
                    global equipos
                    flag=False
                    for i in equipos:
                        if i[1]==codigoe.get():
                            i[0]=nombren.get()
                            flag=True
                            mequipos.destroy()
                    if flag==False:
                        messagebox.showerror(title="Error",message="Este equipo no existe. No se puede modificar")
                        mequipos.deiconify()
            global codigos
            if len(codigos)==0:
                messagebox.showerror(title="Error",message="No puede escoger esta opción a menos que haya ingresado equipos antes")
                aequipos.deiconify()
            else:
    ##            aequipos.destroy()
                mequipos=Tk()
                mequipos.title("Modificación de equipos")
                mequipos.config(bg="green")
                mequipos.resizable(False,False)
                mequipos.geometry("300x300")
                titulo=Label(mequipos,text="Nombre nuevo?",bg="green",font="Times 20 italic").place(x=20,y=100)
                codigo=Label(mequipos,text="Código del equipo a modificar", bg="green",font="Verdana 12 bold underline ").place(x=20,y=20)
                codigoe=Entry(mequipos,font="Times 14 italic", width=20)
                codigoe.place(x=40,y=55)
                nombren=Entry(mequipos,font="Times 14 bold",width=25)
                nombren.place(x=20,y=130)
                consulta=Button(mequipos,text="Modificar",command=modificar).place(x=60,y=180)
                salida=Button(mequipos,text="Cancelar",command=mequipos.destroy).place(x=190,y=180)
                
        def pestañaconsulta():
            def consultar():
                    global equipos
                    flag=False
                    for i in equipos:
                        if i[1]==codigoe.get():
                            titulo=Label(cequipos,text="El nombre asignado",bg="green",font="Times 20 italic").place(x=20,y=130)
                            titulo2=Label(cequipos,text="a este código es:",bg="green",font="Times 20 italic").place(x=20,y=160)
                            nombre1=Label(cequipos,text="                                              ",bg="green",font="Times 20 italic").place(x=20,y=200)
                            nombre=Label(cequipos,text=i[0],bg="green",font="Times 20 italic").place(x=20,y=200)
                            flag=True
                    if flag==False:
                        messagebox.showerror(title="Error",message="Este equipo no existe. No se puede consultar")
                        cequipos.deiconify()
            global codigos
            if len(codigos)==0:
                messagebox.showerror(title="Error",message="No puede escoger esta opción a menos que haya ingresado equipos antes")
                aequipos.deiconify()
            else:
    ##            aequipos.destroy()
                cequipos=Tk()
                cequipos.title("Consulta de equipos")
                cequipos.config(bg="green")
                cequipos.resizable(False,False)
                cequipos.geometry("300x300")
                codigo=Label(cequipos,text="Código del equipo a consultar", bg="green",font="Verdana 12 bold underline ").place(x=20,y=20)
                codigoe=Entry(cequipos,font="Times 14 italic", width=20)
                codigoe.place(x=40,y=55)
                consulta=Button(cequipos,text="Consulta",command=consultar).place(x=80,y=90)
                salida=Button(cequipos,text="Cancelar",command=cequipos.destroy).place(x=150,y=90)
                                     
        def primersiguiente():
    ##        aequipos.destroy()
            global par
            global participantes
            global teamflag
            if par!=0:
                pestañaequipos()
            elif participantes==0:
                messagebox.showerror(title="Error",message="No puede escoger esta opción a menos que haya configurado el torneo antes")
                return
            if par==0:
                messagebox.showerror(title="Listo",message="Las plazas para equipos nuevos ya están llenas")
                teamflag=1
                aequipos.deiconify()
                
    ##            adminequipos()
                
            
        def pestañaequipos():
            def siguiente():
                global par
                global equipos
                global codigos
                if par==1:
                    for i in codigos:
                        if i==codogoe.get():
                            messagebox.showerror(title="Error",message="Este equipo ya está registrado. No se puede agregar")
                            pequipos.deiconify()
                            return
                    if len(codogoe.get())==3:
                        if len(nombree.get())>=5 and len(nombree.get())<=40:
                            codigos+=[codogoe.get()]
                            equipos+=[[nombree.get(),codogoe.get()]]    
                            pequipos.destroy()
                            par-=1
    ##                        adminequipos()
                        else:
                            messagebox.showerror(title="Error", message="El nombre del equipo debe ser de cinco a cuarenta caracteres")
                            pequipos.deiconify()
                            return
                    else:
                        messagebox.showerror(title="Error", message="El código de equipo debe ser de tres caracteres")
                        pequipos.deiconify()
                        return
                elif par>0:
                    for i in codigos:
                        if i==codogoe.get():
                            messagebox.showerror(title="Error",message="Este equipo ya está registrado. No se puede agregar")
                            pequipos.deiconify()
                            return
                    if len(codogoe.get())==3:
                        if len(nombree.get())>=5 and len(nombree.get())<=40:
                            codigos+=[codogoe.get()]
                            equipos+=[[nombree.get(),codogoe.get()]]    
                            pequipos.destroy()
                            par-=1
    ##                        adminequipos()
                        else:
                            messagebox.showerror(title="Error", message="El nombre del equipo debe ser de cinco a cuarenta caracteres")
                            pequipos.deiconify()
                            return
                    else:
                        messagebox.showerror(title="Error", message="El código de equipo debe ser de tres caracteres")
                        pequipos.deiconify()
                        return
            global participantes
            global par
            pequipos=Tk()
            pequipos.title("Registro de equipos")
            pequipos.config(bg="green")
            pequipos.resizable(False,False)
            pequipos.geometry("400x300")
            nombre=Label(pequipos,text="Nombre del equipo que participará", bg="green",font="Verdana 12 bold underline ").place(x=20,y=20)
            nombree=Entry(pequipos,font="Times 14 italic", width=30)
            nombree.place(x=1,y=55)
            codogo=Label(pequipos,text="Código del equipo que participará", bg="green",font="Verdana 12 bold underline ").place(x=20,y=80)
            codogoe=Entry(pequipos,font="Times 14 italic", width=30)
            codogoe.place(x=1,y=115)
            listo=Button(pequipos,text="Agregar",command=siguiente).place(x=100,y=160)
            salida=Button(pequipos,text="Cancelar",command=pequipos.destroy).place(x=190,y=160)
        aequipos=Tk()
        aequipos.title("Administrar información de equipos")
        aequipos.config(bg="green")
        aequipos.resizable(False,False)
        aequipos.geometry("410x200")
        abcdf=Label(aequipos,text="Seleccione una opción",bg="green",font="Times 24 italic bold").place(x=50,y=10)
        a=Button(aequipos,text="Añadir",command=primersiguiente).place(x=30,y=100)
        b=Button(aequipos,text="Consultar",command=pestañaconsulta).place(x=120,y=100)
        c=Button(aequipos,text="Modificar",command=pestañamodificar).place(x=230,y=100)
        d=Button(aequipos,text="Eliminar",command=pestañaeliminar).place(x=330,y=100)
    else:
        equ=Tk()
        equ.title("Equipos registrados")
        equ.config(bg="green")
        equ.resizable(False,True)
        equ.geometry("250x400")
        lab=Label(equ,font="Arial 14 underline",bg="green",text="Nombre").place(x=1,y=10)
        lab2=Label(equ,font="Arial 14 underline",bg="green",text="Código").place(x=150,y=10)
        Y=50
        for i in equipos:
            nombreprint=Label(equ,font="Arial 14 italic",bg="green",text=str(i[0]))
            nombreprint.place(x=1,y=Y)
            codigoprint=Label(equ,font="Arial 14 italic",bg="green",text=str(i[1]))
            codigoprint.place(x=150,y=Y)
            Y+=30

        
        
def crearcalendario():
    if teamflag==1:
        global calenflag
        if calenflag==0:
            calenflag=1
            def calendario1(entrada):
                global teams
                for i in entrada:
                    teams+=[[i,0,0,0,0,0,0,0,0]]
                entrada=list(itertools.permutations(entrada,2))
                global final
                global total
                global numerodefecha
                total=[]
                final=[]
                fecha(entrada,10)
            def fecha(entrada,Y):
                    global fechas
                    global juegos
                    global numerodefecha
                    cont=[]
                    fecha1=[]
                    fecha2=[]
                    if entrada==[]:
                        return 
                    for i in entrada:
                        if i[0] not in cont:
                            if i[1] not in cont:
                                cont+=[i[0]]+[i[1]]
                                fecha1+=[[i[0],i[1],"0","0"]]
                                fecha2+=[([i[0],"VS",i[1]])]
                                entrada.remove(i)
                            else:
                                pass
                        else:
                            pass
                    fechas+=[fecha2]
                    juegos+=fecha1
                    fechaprint=Label(calendario,font="Arial 14 italic",bg="green",text="Fecha"+str(numerodefecha)+"  "+str(fecha2))
                    fechaprint.place(x=1,y=Y)
                    numerodefecha+=1
                    return fecha(entrada,Y+30)
            calendario=Tk()
            calendario.title("Calendario de juegos")
            calendario.config(bg="green")
            calendario.resizable(True,True)
            calendario.geometry("800x700")
            global codigos
            dale=Button(calendario,text="Crear calendario",command=calendario1(codigos))
        else:
            calendario=Tk()
            calendario.title("Calendario de juegos")
            calendario.config(bg="green")
            calendario.resizable(True,True)
            calendario.geometry("800x700")
            global numerodefecha
            numerodefecha=1
            Y=10
            for i in fechas:
                fechaprint=Label(calendario,font="Arial 14 italic",bg="green",text="Fecha"+str(numerodefecha)+"  "+str(i))
                fechaprint.place(x=1,y=Y)
                numerodefecha+=1
                Y+=30
            numerodefecha=1
    else:
        messagebox.showerror(title="Error",message="No puede escoger esta opción hasta que haya ingresado todos los equipos")
            
        

def registrarresultados():
    if calenflag==1:
        def pestañaregistro():
            def registrarresultados1(local,gl, visita,gv):
                global juegos
                for i in juegos:
                    if i[0]==local and i[1]==visita:
                        i[2]=gl
                        i[3]=gv
                        pregistro.destroy()
                        if int(gl)+int(gv)>0:
                            global goles
                            goles=int(gl)+int(gv)
                            pestañagoles()
                            return
                        else:
                            return
                messagebox.showerror(title="Error",message="Ese partido no existe")
                pregistro.deiconify()
            def pestañagoles():
                if goles==0:
                    pass
                else:
                    def goles1():
                        global goles
                        global goleadores
                        if goles==0:
                            anotadores.destroy()
                            resultados.deiconify()
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
                                        resultados.deiconify()
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
                
            def darle():
                registrarresultados1(equipo1.get(),equipo1goles.get(),equipo2.get(),equipo2goles.get())
                
            pregistro=Tk()
            pregistro.geometry("400x300")
            pregistro.title("Añadir resultado")
            pregistro.resizable(False,False)
            pregistro.config(bg="green")
            titulo=Label(pregistro,text="Ingrese el resultado del juego", bg="green",font="Verdana 12 bold underline ").place(x=60,y=10)
            versus=Label(pregistro,text="VS",bg="green",font="Times 35 italic bold").place(x=165,y=50)
            equipo1=Entry(pregistro,font="Times 14 italic",width=10)
            equipo1.place(x=20,y=60)
            equipo2=Entry(pregistro,font="Times 14 italic",width=10)
            equipo2.place(x=270,y=60)
            equipo1goles=Entry(pregistro,font="Times 14 italic",width=5)
            equipo1goles.place(x=20,y=100)
            equipo2goles=Entry(pregistro,font="Times 14 italic",width=5)
            equipo2goles.place(x=320,y=100)
            reg=Button(pregistro,text="Registrar",command=darle).place(x=165,y=140)
        def pestañamodificar():
            def registrarresultados2(local,gl, visita,gv):
                global juegos
                for i in juegos:
                    if i[0]==local and i[1]==visita:
                        i[2]=gl
                        i[3]=gv
                        pmod.destroy()
                        if int(gl)+int(gv)>0:
                            global goles
                            goles=int(gl)+int(gv)
                            pestañagoles1()
                            return
                        else:
                            return
                messagebox.showerror(title="Error",message="Ese partido no existe")
                pmod.deiconify()
            def pestañagoles1():
                if goles==0:
                    pass
                else:
                    def goles11():
                        global goles
                        global goleadores
                        if goles==0:
                            anotadores.destroy()
                            resultados.deiconify()
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
                                        resultados.deiconify()
                                        goleadores.sort(reverse=True)
                                        return goleadores
                                    return pestañagoles()
                            goleadores+=[[1,mae]]
                            goles-=1
                            anotadores.destroy()
                            return pestañagoles1()
                    anotadores=Tk()
                    anotadores.title("Anotadores")
                    anotadores.geometry("400x200")
                    anotadores.resizable(False,False)
                    anotadores.config(bg="green")
                    l=Label(anotadores,text="Ingrese el nombre del anotador y el minuto",bg="green",font="Times 14 underline").place(x=10,y=10)
                    maesillo=Entry(anotadores,font="Arial 14 italic",width=30)
                    maesillo.place(x=10,y=40)
                    otro=Entry(anotadores,font="Arial 14 italic",width=10).place(x=10,y=80)
                    bt=Button(anotadores,text="Añadir",command=goles11).place(x=100,y=120)
                
            def darle():
                registrarresultados2(equipo1.get(),equipo1goles.get(),equipo2.get(),equipo2goles.get())
            pmod=Tk()
            pmod.geometry("400x300")
            pmod.title("Añadir resultado")
            pmod.resizable(False,False)
            pmod.config(bg="green")
            titulo=Label(pmod,text="Ingrese el resultado del juego", bg="green",font="Verdana 12 bold underline ").place(x=60,y=10)
            subtitulo=Label(pmod,text="Asegúrese de que ya haya sido registrado",bg="green",font="Verdana 10 italic").place(x=50,y=35)
            versus=Label(pmod,text="VS",bg="green",font="Times 35 italic bold").place(x=165,y=70)
            equipo1=Entry(pmod,font="Times 14 italic",width=10)
            equipo1.place(x=20,y=80)
            equipo2=Entry(pmod,font="Times 14 italic",width=10)
            equipo2.place(x=270,y=80)
            equipo1goles=Entry(pmod,font="Times 14 italic",width=5)
            equipo1goles.place(x=20,y=120)
            equipo2goles=Entry(pmod,font="Times 14 italic",width=5)
            equipo2goles.place(x=320,y=120)
            reg=Button(pmod,text="Modificar",command=darle).place(x=165,y=160)
        def pestañaconsultar():    
            def consultarresultado(local,visita):
                global juegos
                for i in juegos:
                    if i[0]==local and i[1]==visita:
                        l1=Label(pconsulta,bg="green",font="Verdana 34 italic",text=str(i[2])+"    ").place(x=40,y=110)
                        l2=Label(pconsulta,bg="green",font="Verdana 34 italic",text=str(i[3])+"    ").place(x=290,y=110)
                        return
                    else:
                        pass
                messagebox.showerror(title="Error",message="Ese partido no existe")
            def dadale():
                consultarresultado(equipo1.get(),equipo2.get())
            pconsulta=Tk()
            pconsulta.title("Consulta de resultados")
            pconsulta.resizable(False,False)
            pconsulta.config(bg="green")
            pconsulta.geometry("400x300")
            titulo=Label(pconsulta,text="Ingrese el juego a consultar", bg="green",font="Verdana 12 bold underline ").place(x=60,y=10)
            versus=Label(pconsulta,text="VS",bg="green",font="Times 35 italic bold").place(x=165,y=50)
            equipo1=Entry(pconsulta,font="Times 14 italic",width=10)
            equipo1.place(x=20,y=60)
            equipo2=Entry(pconsulta,font="Times 14 italic",width=10)
            equipo2.place(x=270,y=60)
            cons=Button(pconsulta,text="Consultar",command=dadale).place(x=165,y=160)
            
        def pestaña_que_elimina():
            def eliminarresultado1(local,visita):
                global juegos
                for i in juegos:
                    if i[0]==local and i[1]==visita:
                        i[2]=0
                        i[3]=0
                        return 
                    else:
                        pass
                messagebox.showerror(title="Error",message="Ese partido no existe")
            def dadadale():
                if messagebox.askokcancel( title="Eliminar",message="Seguro que desea eliminar?"):
                    pelim.destroy()
                    eliminarresultado1(equipo1.get(),equipo2.get())
            pelim=Tk()
            pelim.title("Consulta de resultados")
            pelim.resizable(False,False)
            pelim.config(bg="green")
            pelim.geometry("400x300")
            titulo=Label(pelim,text="Ingrese el juego a eliminar", bg="green",font="Verdana 12 bold underline ").place(x=60,y=10)
            versus=Label(pelim,text="VS",bg="green",font="Times 35 italic bold").place(x=165,y=50)
            equipo1=Entry(pelim,font="Times 14 italic",width=10)
            equipo1.place(x=20,y=60)
            equipo2=Entry(pelim,font="Times 14 italic",width=10)
            equipo2.place(x=270,y=60)
            cons=Button(pelim,text="Eliminar",command=dadadale).place(x=165,y=160)
                
        resultados=Tk()
        resultados.title("Resultados de juegos")
        resultados.config(bg="green")
        resultados.resizable(False,False)
        resultados.geometry("410x200")
        abcdf=Label(resultados,text="Seleccione una opción",bg="green",font="Times 24 italic bold").place(x=50,y=10)
        a=Button(resultados,text="Añadir",command=pestañaregistro).place(x=30,y=100)
        b=Button(resultados,text="Consultar",command=pestañaconsultar).place(x=120,y=100)
        c=Button(resultados,text="Modificar",command=pestañamodificar).place(x=230,y=100)
        d=Button(resultados,text="Eliminar",command=pestaña_que_elimina).place(x=330,y=100)
    else:
        messagebox.showerror(title="Error", message="No puede escoger esta opción hasta que haya creado el calendario de juegos")

def pestañagoleadores():
    if messagebox.askokcancel(title="Seguro?",message="Se recomienda que escoja esta opción luego de registrar todos los resultados. Continuar?"):
        global goleadores
        goleo=Tk()
        goleo.title("Los más goleadores")
        goleo.config(bg="green")
        goleo.resizable(False,False)
        Y=40
        goleo.geometry("300x300")
        l3=Label(goleo,text="Nombre",bg="green",font="Times 14 bold").place(x=50,y=10)
        l4=Label(goleo,text="Goles",bg="green",font="Times 14 bold").place(x=180,y=10)
        for i in range(0,8):
            l1=Label(goleo,text=goleadores[i][1],bg="green",font="Times 14 bold").place(x=50,y=Y)
            l2=Label(goleo,text=goleadores[i][0],bg="green",font="Times 14 bold").place(x=180,y=Y)
            Y+=30

def pestañatabla():
     if messagebox.askokcancel(title="Seguro?",message="Para evitar errores en los cálculos no seleccione esta opción hasta haber ingresado todos los resultados. Continuar?"):
        global clasifican
        global teams
        def sumar_ya():
            global juegos
            global teams
            for i in juegos:
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
             messagebox.showerror(title="Error",message="Ese partido no existe")
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
        tabla=Tk()
        tabla.title("Tabla final")
        tabla.config(bg="green")
        tabla.resizable(False,False)
        tabla.geometry("640x500")
        equip=Label(tabla,text="Equipo",font="Times 14",bg="green").place(x=90,y=10)
        pj=Label(tabla,text="PJ",font="Times 14",bg="green").place(x=190,y=10)
        pg=Label(tabla,text="PG",font="Times 14",bg="green").place(x=240,y=10)
        pp=Label(tabla,text="PP",font="Times 14",bg="green").place(x=290,y=10)
        pe=Label(tabla,text="PE",font="Times 14",bg="green").place(x=340,y=10)
        gf=Label(tabla,text="GF",font="Times 14",bg="green").place(x=390,y=10)
        gc=Label(tabla,text="GC",font="Times 14",bg="green").place(x=440,y=10)
        gd=Label(tabla,text="GD",font="Times 14",bg="green").place(x=490,y=10)
        pts=Label(tabla,text="PTS",font="Times 14",bg="green").place(x=540,y=10)
        bt2=Button(tabla,command=sumar_ya())
        bt=Button(tabla,command=tablafinal())
        global clasifican
        Y1=30
        for i in range(0,clasifican):
            aprint=Label(tabla,text="Clasifica",bg="green",font="Arial 12 italic").place(x=1,y=Y1)
            Y1+=20
        Y2=30
        for i in teams:
            equipl=Label(tabla,text=i[0],font="Times 14",bg="green").place(x=90,y=Y2)
            pjl=Label(tabla,text=i[1],font="Times 14 ",bg="green").place(x=190,y=Y2)
            pgl=Label(tabla,text=i[2],font="Times 14 ",bg="green").place(x=240,y=Y2)
            ppl=Label(tabla,text=i[3],font="Times 14 ",bg="green").place(x=290,y=Y2)
            pel=Label(tabla,text=i[4],font="Times 14",bg="green").place(x=340,y=Y2)
            gfl=Label(tabla,text=i[5],font="Times 14 ",bg="green").place(x=390,y=Y2)
            gcl=Label(tabla,text=i[6],font="Times 14 ",bg="green").place(x=440,y=Y2)
            gdl=Label(tabla,text=i[7],font="Times 14",bg="green").place(x=490,y=Y2)
            ptsl=Label(tabla,text=i[8],font="Times 14",bg="green").place(x=540,y=Y2)
            Y2+=20
        
    
def pestañaayuda():
    ayuda=Tk()
    ayuda.title("Ayuda")
    ayuda.config(bg="green")
    ayuda.resizable(False,False)
    ayuda.geometry("500x500")
    l1=Label(ayuda,text="Este es el programa versión 1.3",bg="green",font="Arial 12 italic").pack()
    l2=Label(ayuda,text="Creado por Steven Ramos Salazar",bg="green",font="Arial 12 italic").pack()
    l3=Label(ayuda,text="Si tiene más dudas contácte al programador al 8944-1566",bg="green",font="Arial 12 italic").pack()
    l4=Label(ayuda,text="Para empezar correctamente el programa debe seleccionar la opción",bg="green",font="Arial 12").place(x=1,y=80)
    l5=Label(ayuda,text="configuración del torneo e ingresar los datos requeridos sobre el torneo",bg="green",font="Arial 12").place(x=1,y=100)
    l6=Label(ayuda,text="a realizarse. Una vez hecho esto dirijase a administrar información de",bg="green",font="Arial 12").place(x=1,y=120)
    l7=Label(ayuda,text="equipos. Ingrese el nombre y el código de los equipos que van a",bg="green",font="Arial 12").place(x=1,y=140)
    l8=Label(ayuda,text="participar. O seleccione las demás opciones para consultar, modificar",bg="green",font="Arial 12").place(x=1,y=160)
    l9=Label(ayuda,text="o eliminar equipos. Una vez que haya ingresado todos los equipos",bg="green",font="Arial 12").place(x=1,y=180)
    l10=Label(ayuda,text="diríjase a crear/consultar el calendario de juegos. Debe saber que los",bg="green",font="Arial 12").place(x=1,y=200)
    l11=Label(ayuda,text="juegos se mostrarán de la forma: código vs código. Y por lo tanto es de ",bg="green",font="Arial 12").place(x=1,y=220)
    l12=Label(ayuda,text="suma importancia que recuerde a qué equipo pertenece cada código. ",bg="green",font="Arial 12").place(x=1,y=240)
    l13=Label(ayuda,text="Una vez hecho esto podrá seleccionar registrar los resultados de cada",bg="green",font="Arial 12").place(x=1,y=260)
    l14=Label(ayuda,text="fecha, ingrese los resultados de todos los partidos. En cada partido se",bg="green",font="Arial 12").place(x=1,y=280)
    l15=Label(ayuda,text="le preguntará quienes fueron los anotadores del partido y en cual",bg="green",font="Arial 12").place(x=1,y=300)
    l16=Label(ayuda,text="minuto anotaron. IMPORTANTE: si es un autogol el minuto en que se",bg="green",font="Arial 12").place(x=1,y=320)
    l17=Label(ayuda,text="anotó se pone en negativo, por ejemplo: -15. Luego de hacer todo lo",bg="green",font="Arial 12").place(x=1,y=340)
    l18=Label(ayuda,text="anterior estará listo para ver el recuento del torneo con las opciones",bg="green",font="Arial 12").place(x=1,y=360)
    l19=Label(ayuda,text="tabla de posiciones y tabla de goleadores. En la primera podrá ver",bg="green",font="Arial 12").place(x=1,y=380)
    l20=Label(ayuda,text="los equipos de acuerdo a su puntaje y también los clasificados. En",bg="green",font="Arial 12").place(x=1,y=400)
    l21=Label(ayuda,text="la segunda podrá ver a los que más han perferado las redes ",bg="green",font="Arial 12").place(x=1,y=420)
    l22=Label(ayuda,text="enemigas. Muchas gracias por usar el sistema.",bg="green",font="Arial 12").place(x=1,y=440)
    l23=Label(ayuda,text="Que tenga un buen día :-)",bg="green",font="Arial 12").place(x=1,y=460)
    
            
main=Tk()
main.title("Torneo de fútbol")
main.config(bg="green")
main.resizable(False,False)
main.geometry("300x300")
a=Button(text="Configuración del torneo",command=configura).pack()
b=Button(text="Administrar información de equipos",command=adminequipos).pack()
bb=Button(text="Crear/consultar el calendario de juegos",command=crearcalendario).pack()
c=Button(text="Registrar los resultados de cada fecha",command=registrarresultados).pack()
d=Button(text="Tabla de posiciones",command=pestañatabla).pack()
e=Button(text="Tabla de goleadores",command=pestañagoleadores).pack()
f=Button(text="Ayuda",command=pestañaayuda).pack()
but=Button(text="Salir",command=put).pack()

def start():
    main=Tk()
    main.title("Torneo de fútbol")
    main.config(bg="green")
    main.resizable(False,False)
    main.geometry("516x414")
    a=Button(text="Configuración del torneo",command=configura).pack()
    b=Button(text="Administrar información de equipos",command=adminequipos).pack()
    bb=Button(text="Crear/consultar el calendario de juegos",command=crearcalendario).pack()
    c=Button(text="Registrar los resultados de cada fecha",command=registrarresultados).pack()
    d=Button(text="Tabla de posiciones").pack()
    e=Button(text="Tabla de goleadores").pack()
    f=Button(text="Ayuda").pack()
    but=Button(text="Salir",command=put).pack()
