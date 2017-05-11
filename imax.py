#Zona de variables globales
sala1=120
sala2=120
sala3=120
egeneral1=0
eniños1=0
eviejos1=0
egeneral2=0
eniños2=0
eviejos2=0
egeneral3=0
eniños3=0
eviejos3=0


def estadisticaegen():
    """Esta función usa las variables globales y las combina para dar las estadísticas de las 3 salas conjuntas"""
    global sala1
    global sala2
    global sala3
    global egeneral1
    global eniños1
    global eviejos1
    global egeneral2
    global eniños2
    global eviejos2
    global egeneral3
    global eniños3
    global eviejos3
    vendidas=(120-sala1)+(120-sala2)+(120-sala3)
    print("Cantidad disponible de asientos: ", sala1+sala2+sala3)
    print("Cantidad de entradas vendidas: ",vendidas)
    print("Capacidad máxima de todas las salas: 360")
    print("Ingreso por ventas de entradas de tipo general: ",egeneral1+egeneral2+egeneral3)
    print("Ingreso por ventas de entradas de tipo niños/estudiantes: ",eniños1+eniños2+eniños3)
    print("Ingreso por ventas de entradas de tipo personas de la tercera edad: ",eviejos1+eviejos2+eviejos3)
    print("Total de ingresos por ventas de todas las salas: ",egeneral1+egeneral2+egeneral3+eniños1+eniños2+eniños3+eviejos1+eviejos2+eviejos3)
    print("")
    tontera=input("")
    menu()
    
def estadísticadet(sala):
##"""Esta función usa su argumento para seleccionar entre las 3 salas y usa un procedimento idéntico al de la función anterior para imprimir los resultados"""
     global sala1
     global sala2
     global sala3
     global egeneral1
     global eniños1
     global eviejos1
     global egeneral2
     global eniños2
     global eviejos2
     global egeneral3
     global eniños3
     global eviejos3
     if sala=="1":
         vendidas=(120-sala1)
         print("Cantidad disponible de asientos: ", sala1)
         print("Cantidad de entradas vendidas: ",vendidas)
         print("Capacidad máxima de la sala  : 120")
         print("Ingreso por ventas de entradas de tipo general: ",egeneral1)
         print("Ingreso por ventas de entradas de tipo niños/estudiantes: ",eniños1)
         print("Ingreso por ventas de entradas de tipo personas de la tercera edad: ",eviejos1)
         print("Total de ingresos por ventas de la sala: ",egeneral1+eniños1+eviejos1)
         print("")
         tontera=input("")
         menu()
     elif sala=="2": 
        vendidas=(120-sala2)
        print("Cantidad disponible de asientos: ", sala2)
        print("Cantidad de entradas vendidas: ",vendidas)
        print("Capacidad máxima de la sala : 120")
        print("Ingreso por ventas de entradas de tipo general: ",egeneral2)
        print("Ingreso por ventas de entradas de tipo niños/estudiantes: ",eniños2)
        print("Ingreso por ventas de entradas de tipo personas de la tercera edad: ",eviejos2)
        print("Total de ingresos por ventas de la sala: ",egeneral2+eniños2+eviejos2)
        print("")
        tontera=input("")
        menu()
     elif sala=="3":
         vendidas=(120-sala3)
         print("Cantidad disponible de asientos: ", sala3)
         print("Cantidad de entradas vendidas: ",vendidas)
         print("Capacidad máxima de la sala : 120")
         print("Ingreso por ventas de entradas de tipo general: ",egeneral3)
         print("Ingreso por ventas de entradas de tipo niños/estudiantes: ",eniños3)
         print("Ingreso por ventas de entradas de tipo personas de la tercera edad: ",eviejos3)
         print("Total de ingresos por ventas de la sala: ",egeneral3+eniños3+eviejos3)
         print("")
         tontera=input("")
         menu()
     elif sala=="*":
        vendidas1=(120-sala1)
        vendidas2=(120-sala2)
        vendidas3=(120-sala3)
        print("Sala 1")
        print("Cantidad disponible de asientos: ", sala1)
        print("Cantidad de entradas vendidas: ",vendidas1)
        print("Capacidad máxima de la sala  : 120")
        print("Ingreso por ventas de entradas de tipo general: ",egeneral1)
        print("Ingreso por ventas de entradas de tipo niños/estudiantes: ",eniños1)
        print("Ingreso por ventas de entradas de tipo personas de la tercera edad: ",eviejos1)
        print("Total de ingresos por ventas de la sala: ",egeneral1+eniños1+eviejos1)
        print("")
        print("Sala 2")
        print("Cantidad disponible de asientos: ", sala2)
        print("Cantidad de entradas vendidas: ",vendidas2)
        print("Capacidad máxima de la sala : 120")
        print("Ingreso por ventas de entradas de tipo general: ",egeneral2)
        print("Ingreso por ventas de entradas de tipo niños/estudiantes: ",eniños2)
        print("Ingreso por ventas de entradas de tipo personas de la tercera edad: ",eviejos2)
        print("Total de ingresos por ventas de la sala: ",egeneral2+eniños2+eviejos2)
        print("")
        print("Sala 3")
        print("Cantidad disponible de asientos: ", sala1)
        print("Cantidad de entradas vendidas: ",vendidas3)
        print("Capacidad máxima de la sala  : 120")
        print("Ingreso por ventas de entradas de tipo general: ",egeneral1)
        print("Ingreso por ventas de entradas de tipo niños/estudiantes: ",eniños1)
        print("Ingreso por ventas de entradas de tipo personas de la tercera edad: ",eviejos1)
        print("Total de ingresos por ventas de la sala: ",egeneral1+eniños1+eviejos1)
        print("")
        tontera=input("")
        menu()
        
        
               
         
    
    
def venta(cantidad,costo,sala):
    """Esta función revisa si es posible comprar una determinada cantidad de entradas. Usa simples sumas y restas y una variable temporal llamada sa1, sa2 o sa3 para no modificar la variable global
    y así mantener los datos intactos"""
    global sala1
    global sala2
    global sala3
    sa1=sala1
    sa2=sala2
    sa3=sala3
    if sala=="1":
        if cantidad>sala1:
            sala1=sa1
            print("")
            print("No hay suficientes asientos disponibles")
            print("Cantidad disponible: ",sala1)
            print("")
            opcion1()
        else:
            stotal=cantidad*costo
            return stotal
    elif sala=="2":
        if cantidad>sala2:
            sala2=sa2
            print("")
            print("No hay suficientes asientos disponibles")
            print("Cantidad disponible: ",sala2)
            print("")
            opcion1()
        else:
            stotal=cantidad*costo
            return stotal
    elif sala=="3":
        if cantidad>sala3:
            sala3=sa3
            print("")
            print("No hay suficientes asientos disponibles")
            print("Cantidad disponible: ",sala3)
            print("")
            opcion1()
        else:
            stotal=cantidad*costo
            return stotal
    

def opcion1():
    """Esta función recoge los inputs e imprime. Es en realidad la función venta la que hace todo el trabajo"""
    salas=input("Número de sala: ")
    normal=input("Cantidad de entradas generales: ")
    niños=input("Cantidad de entradas para niños/estudiantes: ")
    viejos=input("Cantidad de entradas para adultos mayores: ")
    print("")
    print("Está seguro?")
    print("s para confirmar, c para cancelar y volver al menú principal")
    print("")
    confirm=input(">>>")
    if confirm=="s" or confirm=="S":
        normalp=venta(int(normal),2000,salas)
        niñosp=venta(int(niños),1500,salas)
        viejosp=venta(int(viejos),1000,salas)
        if type(normalp)==int and type(niñosp)==int and type(viejosp)==int:
            if salas=="1":
                global sala1
                if int(normal)+int(niños)+int(viejos)>sala1:
                    print("No hay suficientes asientos disponibles")
                    print("Cantidad disponible",sala1)
                    opcion1()
                else:
                    sala1=sala1-int(normal)-int(niños)-int(viejos)
                    suma=normalp+niñosp+viejosp
                    print("")
                    print("Factura")
                    print(normal," Entradas generales")
                    print(niños," Entradas para niños/estudiantes")
                    print(viejos, " Entradas para adultos mayores")
                    print(" Total",suma)
                    global egeneral1
                    global eniños1
                    global eviejos1
                    egeneral1+=normalp
                    eniños1+=niñosp
                    eviejos1+=viejosp
                    print("")
                    opcion1()
            elif salas=="2":
                global sala2
                if int(normal)+int(niños)+int(viejos)>sala2:
                    print("No hay suficientes asientos disponibles")
                    print("Cantidad disponible",sala2)
                    opcion1()
                else:
                    sala2=sala2-int(normal)-int(niños)-int(viejos)
                    suma=normalp+niñosp+viejosp
                    print("")
                    print("Factura")
                    print(normal," Entradas generales")
                    print(niños," Entradas para niños/estudiantes")
                    print(viejos, " Entradas para adultos mayores")
                    print(" Total",suma)
                    global egeneral2
                    global eniños2
                    global eviejos2
                    egeneral2+=normalp
                    eniños2+=niñosp
                    eviejos2+=viejosp
                    print("")
                    opcion1()
            elif salas=="3":
                global sala3
                if int(normal)+int(niños)+int(viejos)>sala3:
                    print("No hay suficientes asientos disponibles")
                    print("Cantidad disponible",sala3)
                    opcion1()
                else:
                    sala3=sala3-int(normal)-int(niños)-int(viejos)
                    suma=normalp+niñosp+viejosp
                    print("")
                    print("Factura")
                    print(normal," Entradas generales")
                    print(niños," Entradas para niños/estudiantes")
                    print(viejos, " Entradas para adultos mayores")
                    print(" Total",suma)
                    global egeneral3
                    global eniños3
                    global eviejos3
                    egeneral3+=normalp
                    eniños3+=niñosp
                    eviejos3+=viejosp
                    print("")
                    opcion1()
    elif confirm=="C" or confirm=="c":
        print("")
        menu()


def menu():
    """Menú de interfaz"""
    print("Bienvenido al sistema electrónico de salas Imax")
    print("Elija una opción")
    print("")
    print("1. Comprar entradas")
    print("2. Ver estadísticas de una sala específica")
    print("3. Ver estadísticas generales")
    print("X. Salir")
    entrada=input(">>>")
    print("")
    if entrada =="1":
        opcion1()
        print("")
    elif entrada=="3":
        estadisticaegen()
        print("")
    elif entrada=="2":
        argumento=input("Introduzca la sala a consultar: ")
        estadísticadet(argumento)
        print("")
    elif entrada=="x" or entrada=="X":
        print("Gracias por usar")
        return
    else:
        menu()

               
menu()


