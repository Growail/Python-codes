clientes=[]
lugar=[]
aerolineas=[]

#####################################################################################################################################################
##zona de funciones generales
##funcion que inicia el programa
def start():
    print("Tarea programada")
    print("Sistema de reservaciones aerolínea")
    adquirir()
    evaluarlug()
    evaluarclientes()
    menu()
##menu del programa
def menu():
    print("Elija una opción")
    print("1.Opciones de usuario")
    print("2.Opciones de gerente")
    print("3.Salir")
    opcion=input(">> ")
    if opcion=="1":
        menuusuario()
    elif opcion=="2":
        menugerente()
    elif opcion=="3":
        print("Cerrando...")
        print("")
        print("")
        print("")
        print("Gracias por usar")
        return
    else:
        print("Error: La opción digitada no es válida")
        menu()
def menugerente():
    print("")
    print("1.Ver todas las aerolíneas")
    print("2.Ver estadísticas de lugares")
    print("3.Ver estadísticas de clientes")
    print("4.Ver estadísticas de aerolíneas")
    print("5.Volver al menu principal")
    opcion2=input(">> ")
    if opcion2=="1":
        global aerolineas
        print("")
        print(aerolineas)
        print("")
        menugerente()
    elif opcion2=="2":
        print("")
        estadisticas_lugares()
        print("")
        menugerente()
    elif opcion2=="3":
        print("")
        estadisticas_clientes()
        print("")
        menugerente()
    elif opcion2=="4":
        print("")
        print("")
        menugerente()
    elif opcion2=="5":
        print("")
        menu()
        print("")
    else:
        print("Error: La opción digitada no es válida")
        menugerente()
def menuusuario():
    print("")
    print("1.Ver la lista de clientes")
    print("2.Ver los destinos")
    print("3.Hacer una reservación")
    print("4.Volver al menu principal")
    opcion1=input(">> ")
    if opcion1=="1":
        global clientes
        print("")
        print(clientes)
        print("")
        menuusuario()
    elif opcion1=="2":
        global lugar
        print("")
        print(lugar)
        print("")
        menuusuario()
    elif opcion1=="3":
        print("")
        print("")
        menuusuario()
    elif opcion1=="4":
        print("")
        menu()
        print("")
    else:
        print("Error: La opción digitada no es válida")
        menuusuario()
            
         
## funcion para asignar valor a la variable global
def adquirir():
    global clientes
    global lugar
    global aerolineas
    clientes=obtener_clientes()
    lugar=obtener_lugares()
    aerolineas=obtener_aerolineas()
    elimcelcli()
    elimcellug()
## acomodar los archivos del .txt en la lista creada   
def acomodar(lista):
    listanueva = lista[:4]
    lista = lista[4:]
    lista1 = []
    
    for i in range(len(lista)):
        if i == 0:
            for j in range(len(lista[i])):
                if lista[i][j] == '$':
                    lista1 += [lista[i][:j], lista[i][j], lista[i][j+1:]]
        elif len(lista[i]) > 3:
            for j in range(len(lista[i])):
                if lista[i][j] == '$':
                    lista1 += [lista[i][:j], lista[i][j], lista[i][j+1:]]
                    lista1 += lista[i+1:]
                    break
            break
        else:
            lista1 += lista[i]
            
    listanueva += lista1
    return listanueva   

##Función para eliminar los saltos de linea
def eliminar(lista):
    novalista = []
    for i in range(len(lista)):
        prev = ''
        for j in range(len(lista[i])):
            if lista[i][j] != '\n':
                prev += lista[i][j]
        novalista += [prev]
    return novalista
######################################################################################################################################################
##zona de funciones de reservación y estadísticas
##revisa las listas y dice si el destino y el cliente existen
def existe(cliente, destino):
    global clientes
    global lugar
    global aerolineas
    lugarcop=lugar
    clientescop=clientes
    while lugarcop!=[]:
        if destino==lugarcop[0][0]:
            break
        else:
            lugarcop=lugarcop[1:]
    while clientescop!=[]:
        if cliente==clientescop[0][1]:
            break
        else:
            clientescop=clientescop[1:]
    if lugarcop==[]:
        print("Este destino no existe")
    if clientescop==[]:
        print("Este cliente no existe")
    if clientescop!=[] and lugarcop!=[]:
        if directo(cliente,destino):
            print("Existe una ruta directa, ¿Desea usarla?")
            print("1.Sí")
            print("2.No")
            opcion=input(">>")
            if opcion=="1":
                return directoaux(cliente, destino)
            else:
                print("2")

    
##dice si es posible hacer un vuelo directo
def directo(cliente,destino):
    global clientes
    global lugar
    global aerolineas
    localizacion=0
    for i in clientes:
        if i[1]==cliente:
            localizacion=i[2]
            break
        else:
            pass
    for i in aerolineas:
        if i[2]==localizacion:
            for j in i[3]:
                if j[0]==destino:
                    return True
                else:
                    pass
        else:
            pass
    return False
##detalles del vuelo directo
def directoaux(cliente, destino):
    global clientes
    global lugar
    global aerolineas
    localizacion=0
    for i in clientes:
        if i[1]==cliente:
            localizacion=i[2]
            break
        else:
            pass
    for i in aerolineas:
        if i[2]==localizacion:
            for j in i[3]:
                if j[0]==destino:
                    return guardar(cliente,destino,i[1],j)
                else:
                    pass
        else:
            pass
    return False
def reservador(cliente,destino):
    global clientes
    global lugar
    global aerolineas
    localizacion=0
    ruta=[]
    for i in clientes:
        if i[1]==cliente:
            localizacion=i[2]
            break
        else:
            pass
    for i in aerolineas:
        if i[2]==localizacion:
            temp=i[3]
            while temp!=[]:
                if temp[0]==destino:
                    for i in clientes:
                        if i[1]==cliente:
                            i=[i[0],i[1],temp[0],i[3],((i[4])+1)]
                    print( ruta+[i[0],[temp]])
                    return
                else:
                    temp=temp[1:]
        else:
            pass
                
##escribir en el .txt de la factura (vuelo directo)              
def guardar(cliente,destino,aerolinea,j):
    global clientes
    global lugar
    clientevar=""
    estavar=""
    lugarvar=""
    for k in clientes:
        if k[1]==cliente:
            clientevar=k[2]
        else:
            pass
    for l in lugar:
        if l[0]==clientevar:
            estavar=l[1]
        else:
            pass
    for m in lugar:
        if m[0]==destino:
            lugarvar=m[1]
        else:
             pass
    factura0=aerolinea
    factura1= "Usuario",cliente
    factura2="Viaje de",estavar,"a",lugarvar
    factura3="Distancia",j[2]
    factura4="Costo",j[1]
    lista0= str(factura0)
    lista1= str(factura1)
    lista2= str(factura2)
    lista3= str(factura3)
    lista4= str(factura4)
    archivo= open(str("Factura")+".txt", "a")
    archivo.write(lista0)
    archivo.write("\n")
    archivo.write(lista1)
    archivo.write("\n")
    archivo.write(lista2)
    archivo.write("\n")
    archivo.write(lista3)
    archivo.write("\n")
    archivo.write(lista4)
    archivo.write("\n")
    archivo.write("-------------------------------------------")
    archivo.write("\n")
    archivo.close()
    print("Su reservación se completó con éxito")
        
    
  
##calcula los destinos más, menos y nunca visitados
def estadisticas_lugares():
    global lugar
    lista=[]
    masvisitados=0
    masvisitadostr=""
    menosvisitados=0
    menosvisitadosstr=""
    nuncavisitadosstr=""
    for i in lugar:
        lista=lista+[i[2]]
    masvisitados=max(lista)
    menosvisitados=min(lista)
    for i in lugar:
        if i[2]==masvisitados:
            masvisitadostr=masvisitadostr+"  "+i[1]
        elif i[2]==0:
            nuncavisitadosstr=nuncavisitadosstr+"  "+i[1]
        elif i[2]==menosvisitados:
            menosvisitadosstr=menosvisitadosstr+"  "+i[1]
    print("Destino(s) más visitado(s)")
    print(masvisitadostr)
    print("Destino(s) menos visitado(s)")
    print(menosvisitadosstr)
    print("Destino(s) nunca visitado(s)")
    print(nuncavisitadosstr)

## calcula el usuario que más viajó y el que nunca lo hizo
def estadisticas_clientes():
    global cliente
    lista=[]
    masvisitados=0
    masvisitadostr=""
    nuncavisitadosstr=""
    for i in clientes:
        lista=lista+[i[4]]
    masvisitados=max(lista)   
    for i in clientes:
        if i[4]==masvisitados:
            masvisitadostr=masvisitadostr+"  "+i[1]

        elif i[4]==0:
            nuncavisitadosstr=nuncavisitadosstr+"  "+i[1]
    print("Cliente(s) que más viajó")
    print(masvisitadostr)
    print("Cientes(s) que nunca viajó")
    print(nuncavisitadosstr)


#####################################################################################################################################################
##zona de funciones de manejo del .txt de lugares
## funcion para obtener lugares
def obtener_lugares():
    lugar = open("Lugares.txt")
    lugares = []
    n = 1
    fin=[]
    
    while n:
        linea = lugar.readline()
        if linea == '':
            n = 0
        else:
            linea = linea.split(';')
            linea = eliminar(linea)
            linea = [acomodar(linea)]
            lugares += linea
    return lugares
##eliminar repeticiones, separa los elementos del .txt en sublistas más manejables y agrega un cero para contar la cantidad de viajes al destino
def elimcellug():
    global lugar
    listanueva=[]
    temp=[]
    for i in lugar:
        temp=temp+[i[0][0:10]]
    temp=eliminador(temp)
    for j in lugar:
        if j[0][0:10] in temp:
            listanueva=listanueva+j
            temp=temp[1:]
        else:
            pass
    lugar=listanueva
    listanueva=[]
    t=[]
    while lugar!=[]:
        if len(t)!=2:
            t=t+[lugar[0]]
            lugar=lugar[1:]
        elif len(t)==2:
            listanueva=listanueva+[t]
            t=[]
    listanueva=listanueva+[t]
    lugar=listanueva
    listanueva=[]
    for i in lugar:
        i=i+[0]
        listanueva=listanueva+[i]
    lugar=listanueva

def evaluarlug():
    global lugar
    fin=[]
    for i in lugar:
        fin=fin+[[eval(i[0]),i[1],0]]
    lugar=fin
    return fin
        
################################################################################################################################################################
##zona de funciones de manejo del .txt de clientes
##Abrir el archivo de clientes
def obtener_clientes():
    cliente = open("Clientes.txt")
    clientes = []
    n = 1
    
    while n:
        linea = cliente.readline()
        if linea == '':
            n = 0
        else:
            linea = linea.split(';')
            linea = eliminar(linea)
            linea = [acomodar(linea)]
            clientes += linea
    return clientes

##eliminar repeticiones, separa los elementos del .txt en sublistas más manejables y agrega un cero para contar la cantidad de viajes del usuario
def elimcelcli():
    global clientes
    listanueva=[]
    temp=[]
    for i in clientes:
        temp=temp+[i[0][0:10]]
    temp=eliminador(temp)
    for j in clientes:
        if j[0][0:10] in temp:
            listanueva=listanueva+j
            temp=temp[1:]
        else:
            pass
    clientes=listanueva
    listanueva=[]
    t=[]
    while clientes!=[]:
        if len(t)!=4:
            t=t+[clientes[0]]
            clientes=clientes[1:]
        elif len(t)==4:
            listanueva=listanueva+[t]
            t=[]
    listanueva=listanueva+[t]
    clientes=listanueva
    listanueva=[]
    for i in clientes:
        i=i+[0]
        listanueva=listanueva+[i]
    clientes=listanueva
            
##crea un temporal para ser usado en la función de eliminar repetidos
def eliminador(temp):
    fin=[]
    fin=fin+[temp[0]]
    for i in range(len(temp)):
        if temp[i] in fin:
            pass
        else:
            fin=fin+[temp[i]]
    return fin
def evaluarclientes():
    global clientes
    fin=[]
    for i in clientes:
        fin=fin+[[i[0],i[1],eval(i[2]),i[3],0]]
    clientes=fin
    return fin
####################################################################################################################################################################
##zona de funciones de mannejo del .txt de aerolineas
##abrir el archivo de aerolineas    
def obtener_aerolineas():
    aerolinea = open("Aerolineas.txt")
    aerolineas = []
    fin=[]
    n = 1
    
    while n:
        linea = aerolinea.readline()
        if linea == '':
            n = 0
        else:
            linea = linea.split(';')
            linea = eliminar(linea)
            linea = [acomodar(linea)]
            aerolineas += linea
    aerolineas=aerolineas[:-1]
    for i in aerolineas:
        fin=fin+[evaluaraero(i)]
    return fin

##evalúa los elementos de aerolineas y los transforma en int y list
def evaluaraero(i):
    temp=[]
    temp2=[]
    i=[eval(i[0]),i[1],eval(i[2]),eval(i[3]),0]
    while i[3]!=[]:
        if len(temp)<3:
            temp=temp+[i[3][0]]
            i[3]=i[3][1:]
        else:
            temp2=temp2+[temp]
            temp=[]
    temp2=temp2+[temp]
    
    i=[i[0],i[1],i[2],temp2,0]
    return i

start()   
