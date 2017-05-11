##variable para almacenar todos los clientes despues de cargarlos
Todos_clientes=[]
##variable para almacenar los lugares
Todos_lugares=[]
##variable para almacenar aerolineas
Todos_aerolineas=[]
##variable para almacener el clientes en transaccion
cliente_actual=[]
## variable ára almacenar el lugar al cual el cliente desea viajar
lugar_viaje= []


def acomodar(lista):
    novalista = lista[:4]
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
            
    novalista += lista1
    return novalista   

##Función para eliminar '\n' o mejor conocidos como los saltos de linea
def eliminar(lista):
    novalista = []
    for i in range(len(lista)):
        prev = ''
        for j in range(len(lista[i])):
            if lista[i][j] != '\n':
                prev += lista[i][j]
        novalista += [prev]
    return novalista
    
##Abrir el archivo de clientes
def obtener_txt_clientes():
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
    return validar_cedulas(clientes)

## funcion para validar que las cedulas de los clientes no se repitan
def validar_cedulas(lista):
    resultado=[]
    for i in lista:
        if i[0] not in resultado:
            resultado+=[i[0]]+[i]
    return acomodo_clientes(resultado)
## funcion para acomodar la lista de clientes. esta funcion puede ser la que le de valor a global clientes
def acomodo_clientes(lista):
    global Todos_clientes
    resultado=[]
    for i in range(1,len(lista),2):
        resultado+=[lista[i]]
    Todos_clientes=resultado
    return resultado

## funcion para obtener los llugares  como una lista
def obtener_txt_lugares():
    lugar = open("Lugares.txt")
    lugares = []
    n = 1
    
    while n:
        linea = lugar.readline()
        if linea == '':
            n = 0
        else:
            linea = linea.split(';')
            linea = eliminar(linea)
            linea = [acomodar(linea)]
            lugares += linea
    return validar_lugares(lugares)
## funcion para validar que los codigos de las aerolineas no se repite 
def validar_lugares(lista):
    resultado=[]
    for i in lista:
        if i[0] not in resultado:
            resultado+=[i[0]]+[i]
    return acomodo_lugares(resultado)
##funcion que acomoda la lista de lugares tal vez usada para asignar la global llamada Lugares
def acomodo_lugares(lista):
    global Todos_lugares
    resultado=[]
    for i in range(1,len(lista),2):
        resultado+=[lista[i]]
    Todos_lugares=resultado
    return resultado
## funcion para obtener las aerolineas
def obtener_txt_aerolineas():
    global Todos_aerolineas
    aerolinea = open("Aerolineas.txt")
    aerolineas = []
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
    Todos_aerolineas = aerolineas
    return aerolineas
## funcion usada para asignar valor a la variable global llamada cliente_actual.
def seleccionar_clientes():
    global Todos_clientes,cliente_actual
    for i in range(len(Todos_clientes)):
        print(i,Todos_clientes[i])
    opcion=(eval(input("Seleccione un Cliente :")))
    print("el cliente seleccionado es:",Todos_clientes[opcion])
    cliente_actual=Todos_clientes[opcion]
    return
        

def seleccionar_lugares():
    global Todos_lugares,lugar_viaje
    for i in range(len(Todos_lugares)):
        print(i,Todos_lugares[i])
    opcion=(eval(input("Seleccione el Lugar al cual desea viajar :")))
    print("el lugar seleccionado es:",Todos_lugares[opcion])
    lugar_viaje= Todos_lugares[opcion]
    return

## funcion para hacer la factura del cliente
def guardar():
    global cliente_actual,lugar_viaje
    factura= cliente_actual+[lugar_viaje]
    lista= str(factura)
    archivo= open(str("Factura")+".txt", "a")
    archivo.write(lista)
    archivo.write("\n")
    cliente_actual=[]
    lugar_viaje=[]
    archivo.close()
