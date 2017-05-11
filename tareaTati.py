ListaPlacas=[]
def agregarPlaca(placa):
    global ListaPlacas
    cont=0;
    while cont<len(ListaPlacas):
        if ListaPlacas[cont]==placa:
            return "Placa repetida"
        else:
            cont+=1
    ListaPlacas+=[placa]
    return "Placa "+placa+" agregada"
def eliminarPlaca(placa):
    global ListaPlacas
    listaTemp=[]
    cont=0;
    while cont<len(ListaPlacas):
        if ListaPlacas[cont]==placa:
            ListaPlacas=listaTemp+ListaPlacas[cont+1:]
            return "Placa "+placa+" eliminada"
        else:
            listaTemp+=ListaPlacas[cont]
            cont+=1
    return "Placa "+placa+" no encontrada"
def actualizarPlaca(placa, placaNueva):
    global ListaPlacas
    listaTemp=[]
    cont=0;
    while cont<len(ListaPlacas):
        if ListaPlacas[cont]==placa:
            ListaPlacas=listaTemp+[placaNueva]+ListaPlacas[cont+1:]
            return "Placa "+placa+" actualizada"
        else:
            listaTemp+=ListaPlacas[cont]
            cont+=1
    return "Placa "+placa+" no encontrada"
def listarPlacas():
    global ListaPlacas
    cont=0
    while cont<len(ListaPlacas):
        print(ListaPlacas[cont])
        cont+=1
def restriccionDia(dia):
    diadd=dia
    diad=""
    if (dia=="Lunes"):
        diad="1"
        dia="2"
    elif (dia=="Martes"):
        diad="3"
        dia="4"
    elif (dia=="Miercoles" or dia=="Miércoles"):
        diad="5"
        dia="6"
    elif ( dia=="Jueves"):
        diad="7"
        dia="8"
    elif (dia=="Viernes"):
        diad="9"
        dia="0"
    else:
        return "Día no válido"
    global ListaPlacas
    cont=0;
    print("Placas no permitidas el día "+diadd)
    while cont<len(ListaPlacas):
        longitud=len(ListaPlacas[cont])-1
        if ListaPlacas[cont][longitud]==dia:
            print(ListaPlacas[cont])
            cont+=1
        elif ListaPlacas[cont][longitud]==diad:
            print(ListaPlacas[cont])
            cont+=1
        else:
            cont+=1
            
