GAM=[]
atlantica=[]
pacifica=[]
norte=[]
suma=[]


def bisiesto(año):
##     """Entradas:un  numero
##     Salidas: un booleano o un string de error
##     Restricciones: la entrada debe ser un número entero mayor a 2000
##     Qué hace?: divide el año entre 4 para saber si es bisiseto o no"""
    if año<2000:
        return "Error: Año inválido"
    elif año%4==0:
        return True
    else:
        return False
 

def valida_fecha(num):
    """Entradas: un número
         Salidas: un booleano
         Restricciones: la entrada debe ser un número entero de 8 digitos
         Qué hace?: parte la entrada en tres segmentos: dia , mes y año y compara con un calendario para ver si tal fecha puede existir"""
    año=num%10000
    num=num//10000
    mes=num%100
    num=num//100
    dia=num
    if bisiesto(año)==True:
        if mes==2 and dia<=29:
            return True
        elif mes in (1,3,5,7,8,10,12) and dia<=31:
            return True
        elif mes in (4,6,9,11) and dia<=30:
            return True
        else:
            return False
    else:
        if mes==2 and dia<=28:
            return True
        elif mes in (1,3,5,7,8,10,12) and dia<=31:
            return True
        elif mes in (4,6,9,11) and dia<=30:
            return True
        else:
            return False


def fecha1(num):
    """Entradas: un numero 
         Salidas: un string o un booleano
         Restricciones: la entrada debe ser un numero entero de 8 digitos
         Qué hace?: primero valida si la fecha puede existir y luego la transcribe de forma legible"""
    if valida_fecha(num):
        meses=["nada","enero","febrero","marzo","abril","mayo","junio","julio","agosto","setiembre","octubre","noviembre","diciembre"]
        año=num%10000
        num=num//10000
        mes=num%100
        num=num//100
        dia=num
        return str(dia)+" "+"de"+" "+meses[mes]+" "+str(año)
    else:
        return False

def promedio(zona):
##    calcula el promedio de un grupo de datos
    global GAM
    global atlantica
    global pacifica
    global norte
    global suma
    if zona==1:
        if len(GAM)==0:
            return "No hay lecturas disponibles para esa zona"
        else:
            total=0
            for i in GAM:
                total+=i[0]
            return total/len(GAM)
    elif zona==2:
        if len(atlantica)==0:
                return "No hay lecturas disponibles para esa zona"
        else:
                total=0
                for i in atlantica:
                    total+=i[0]
                return total/len(atlantica)
    elif zona==3:
        if len(pacifica)==0:
                return "No hay lecturas disponibles para esa zona"
        else:
                total=0
                for i in pacifica:
                    total+=i[0]
                return total/len(pacifica)
    elif zona==4:
        if len(norte)==0:
            return "No hay lecturas disponibles para esa zona"
        else:
            total=0
            for i in norte:
                total+=i[0]
            return total/len(norte)
    elif zona==5:
        if len(suma)==0:
            return "No hay lecturas disponibles"
        else:
            total=0
            for i in suma:
                total+=i[0]
            return total/len(suma)
        

def estadisticasesp():
##    calcula la cantidad de entradas, promedio, máximo y minimo de una zona determinada
    global GAM
    global atlantica
    global pacifica
    global norte
    zona=input("Introduzca el código de zona: ")
    if zona=="1":
        print("Cantidad de lecturas: ",len(GAM))
        if len(GAM)==0:
            print("Temperatura promedio: ",0)
            print("Temperatura mayor: ",0)
            print("Temperatura menor: ",0)
            tontera=input()
            menu()
        else:
            print("Temperatura promedio: ",promedio(1))
            print("Temperatura mayor: ",max(GAM))
            print("Temperatura menor: ",min(GAM))
            tontera=input()
            menu()
    elif zona=="2":
        print("Cantidad de lecturas: ",len(atlantica))
        if len(atlantica)==0:
            print("Temperatura promedio: ",0)
            print("Temperatura mayor: ",0)
            print("Temperatura menor: ",0)
            tontera=input()
            menu()
        else:
            print("Temperatura promedio: ",promedio(2))
            print("Temperatura mayor: ",max(atlantica))
            print("Temperatura menor: ",min(atlantica))
            tontera=input()
            menu()
    elif zona=="3":
        print("Cantidad de lecturas: ",len(pacifica))
        if len(pacifica)==0:
            print("Temperatura promedio: ",0)
            print("Temperatura mayor: ",0)
            print("Temperatura menor: ",0)
            tontera=input()
            menu()
        else:
            print("Temperatura promedio: ",promedio(3))
            print("Temperatura mayor: ",max(pacifica))
            print("Temperatura menor: ",min(pacífica))
            tontera=input()
            menu()
    elif zona=="4":
        print("Cantidad de lecturas: ",len(norte))
        if len(norte)==0:
            print("Temperatura promedio: ",0)
            print("Temperatura mayor: ",0)
            print("Temperatura menor: ",0)
            tontera=input()
            menu()
        else:
            print("Temperatura promedio: ",promedio(4))
            print("Temperatura mayor: ",max(norte))
            print("Temperatura menor: ",min(norte))
            tontera=input()
            menu()
    elif zona=="*":
        print("Error 404: Función no encontrada")
        menu()
        
        
def estadisticagen():
##    calcula las estadísticas de todas las zona fundiéndolas en una y luego repitiendo el proceso de estadisticas específicas
    global GAM
    global atlantica
    global pacifica
    global norte
    global suma
    suma=GAM+atlantica+pacifica+norte
    print("Cantidad total de lecturas: ",len(suma))
    if len(suma)==0:
        print("Temperatura promedio: ",0)
        print("Temperatura mayor: ",0)
        print("Temperatura menor: ",0)
        tontera=input()
        menu()
    else:
        print("Temperatura promedio: ",promedio(5))
        print("Temperatura mayor: ",max(suma))
        print("Temperatura menor: ",min(suma))
        tontera=input()
        menu()
        




    
def recibidor():
##esta función recibe la zona, fecha y temperatura y las envía a el escribidor que las escribe en la variable
    zona=input("Introduzca el código de la zona: ")
    fecha=input("Introduzca la fecha con el formato establecido: ")
    temperatura=input("Introduzca la temperatura en Celsius: ")
    fecha=int(fecha)
    zona=int(zona)
    temperatura=int(temperatura)
    if valida_fecha(fecha):
        if temperatura<41 and temperatura>4:
            if zona==1 or zona==2 or zona==3 or zona==4:
                escribidor(zona,fecha,temperatura)
            else:
                print("Error: Zona inválida")
                recibidor()
        else:
            print("Error: Temperatura Inválida")
            recibidor()
    else:
        print("Error: Fecha inválida")
        recibidor()

def escribidor(zona,fecha,temperatura):
##  escribe los nuevos valores en la variable
    global GAM
    global atlantica
    global pacifica
    global norte
    fecha=fecha1(fecha)
    if zona==1:
        GAM=GAM+[[temperatura,fecha]]
        menu()
    elif zona==2:
        atlantica+=[[temperatura,fecha]]
        menu()
    elif zona==3:
        pacifica+=[[temperatura,fecha]]
        menu()
    elif zona==4:
        norte+=[[temperatura,fecha]]
        menu()



def menu():
    """Menú de interfaz"""
    print("")
    print("Bienvenido al sistema de registro de temperaturas")
    print("Elija una opción")
    print("")
    print("1. Introducir temperaturas")
    print("2. Ver estadísticas de una zona específica")
    print("3. Ver estadísticas generales")
    print("X. Salir")
    entrada=input(">>>")
    print("")
    if entrada =="1":
        recibidor()
        print("")
    elif entrada=="3":
        estadisticagen()
        print("")
    elif entrada=="2":
        estadisticasesp()
        print("")
    elif entrada=="x" or entrada=="X":
        print("Gracias por usar")
        return
    else:
        menu()

menu()
