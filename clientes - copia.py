#f2
#f3
#f4

class Cuenta:
    numeroCuenta = ""
    saldo = 0
    tipo = "No especificado"
    cedula = ""
    referenciaSucursal = ""
    def Depositar(self,p):
        self.saldo = self.saldo + p
    def Retirar(self,p):
        if self.saldo<p:
            print('Los fondos son insuficientes')
        else:
            self.saldo=self.saldo-p
    def ImprimirSaldo(self):
        print("El saldo de la cuenta es ",self.saldo)
    
class Persona:
    identificacion = ""
    nombre = ""
    apellido=''
    cumpleaños=''
    direccion = ""
    sucursal=''
    def Imprima(self):
        print("Identificacion: ",self.identificacion)
        print("Nombre: ",self.nombre)
        print('Apellido: ',self.apellido)
        print("")
        
class Sucursal:
    codigo=''
    nombre=''
    
#programa
clientes = []   #lista de clientes
cuentas = []    #lista de cuentas
sucursales=[]
# algunos datos iniciales
j = Persona()
j.nombre = "Juan"
j.apellido='Perez'
j.identificacion='123'
clientes.append(j)
k = Persona()
k.nombre = "Pedro"
k.apellido = 'Perez'
k.identificacion='456'
clientes.append(k)

opcion = " "
while opcion.upper() != "S" :   #se sale hasta que "S"
    print("   1.  Ingresar clientes")
    print("   2.  Imprimir clientes")
    print("   3.  Crear cuenta")
    print("   4.  Hacer deposito")
    print("   5.  Imprimir saldo")
    print("   6.  Imprimir lista de cuentas")
    print("   8.  Imprimir cantidad de cuentas del banco")
    print("   7.  Hacer retiro") 
    print("   9.  Imprimir cantidad de clientes")
    print("  10. Imprimir cantidad de cuentas de la sucursal")
    print("   S.  Salir")
    print("")
    opcion = input("   Digite la opcion y presione ENTER -->")
    if opcion == "1" :
        p = Persona()
        p.identificacion = input("Digite la identificacion :")
        p.nombre = input("Digite el nombre :")
        p.apellido = input("Digite el apellido :")
        clientes.append(p)
    elif opcion == "2" :
        print("Lista de clientes :")
        print("-------------------")
        for i in range(len(clientes)):
            clientes[i].Imprima()
    elif opcion == "3" :
        c = Cuenta()
        c.numeroCuenta = input("Digite el numero de cuenta :")
        print('Tipos de cuenta:')
        print('Ahorros 1: 1')
        print('Ahorro dólares: 2')
        print('Cuenta corriente: 3')
        c.tipo= input('Especifique el tipo de cuenta:')
        c.referenciaCliente = input("Digite la cédula del cliente dueño :")
        cuentas.append(c)
    elif opcion == "4" :
        clienteBuscado=input('Ingrese la cédula del cliente:')
        encontroc=-1
        for i in range(len(clientes)):
            if clientes[i].identificacion==clienteBuscado:
                encontroc=i
        if encontroc != -1:
            #buscar la cuenta y despues si existe, depositar
            cuentaBuscada = input("Ingrese la cuenta para deposito :")
            encontro = -1       # no existe
            for i in range(len(cuentas)):
                if cuentas[i].numeroCuenta == cuentaBuscada :
                    encontro = i
            if encontro != -1 :
                monto = int(input("Digite el monto del deposito :"))
                cuentas[encontro].Depositar(monto)
            else :
                print("La cuenta digitada no existe !!!")
        else:
            print('El cliente buscado no existe !!!')
        
    elif opcion == "5" :
        #buscar la cuenta y despues si existe, depositar
        cuentaBuscada = input("Ingrese el código de cuenta :")
        encontro = -1       # no existe
        for i in range(len(cuentas)):
            if cuentas[i].numeroCuenta == cuentaBuscada :
                encontro = i
        if encontro != -1 :
            cuentas[encontro].ImprimirSaldo()
        else :
            print("La cuenta digitada no existe !!!")
    elif opcion =="6" :
        clienteBuscado = input("Digite la identificacion del cliente :")
        encontro = -1       # no existe
        for i in range(len(cuentas)):
            if cuentas[i].referenciaCliente == clienteBuscado :
                encontro = i
                print('Cuenta encontrada:')
                print("              código :",cuentas[i].numeroCuenta)
                print('              saldo:',cuentas[i].saldo)
                print('              tipo:',cuentas[i].tipo)
        if encontro == -1 :
            print("El cliente no tiene cuentas !!!")
    elif opcion=='7':
        clienteBuscado=input('Ingrese la cédula del cliente:')
        encontroc=-1
        for i in range(len(clientes)):
            if clientes[i].identificacion==clienteBuscado:
                encontroc=i
        if encontroc != -1:
            #buscar la cuenta y despues si existe, depositar
            cuentaBuscada = input("Ingrese la cuenta para retiro :")
            encontro = -1       # no existe
            for i in range(len(cuentas)):
                if cuentas[i].numeroCuenta == cuentaBuscada :
                    encontro = i
            if encontro != -1 :
                monto = int(input("Digite el monto del retiro :"))
                cuentas[encontro].Retirar(monto)
            else :
                print("La cuenta digitada no existe !!!")
        else:
            print('El cliente buscado no existe !!!')
    elif opcion=='8':
        print('Cantidad total de cuentas en el banco:')
        print(len(cuentas))
    elif opcion=='9':
        print('Cantidad actual de usuarios del sistema')
        print(len(clientes))
    elif opcion=='10':
        print('Cantidad de cuentas registradas en la sucursal:')
        print(len(sucursales))
    else :
        print("Gracias por usar el programa !!!")
        print("Fin")



def f3(num1,num2,num3,i=0,mayor=0,resul=0):
    if i ==0: 
        if num1>num2 and num1>num3:
            f3(num1,num2,num3,1,num1)
        elif num2>num1 and num2>num3:
            f3(num1,num2,num3,1,num2)
        else:
            f3(num1,num2,num3,1,num3)
    else:
        while True:
            if (mayor%num1==0) and (mayor%num2==0) and (mayor%num3==0):
                resul=mayor
                print(resul)
                break
            mayor+=1


    
def f2(lista,i=0,resul=[[]]):
    if i==(len(lista)):
        return f2aux(resul,[])
    elif lista[i]>lista[i-1]:
               resul[0]+=[lista[i]]
               i+=1
               return f2(lista,i,resul)
    else:
        resul=[[lista[i]]]+resul
        i+=1
        return f2(lista,i,resul)        

def f2aux(lista,resul):
    if lista==[]:
        print (resul)
        res=f2aux2(resul,[])
        return Vuelve(res,[])
    else:
        return f2aux(lista[1:],[lista[0]]+resul)

#Manda a quitar las comas
def f2aux2(lista,resul):
    if lista==[]:
        return resul
    else:
        num=Conc(lista[0],0,[])
        return f2aux2(lista[1:],[num]+resul)
#Concatena
def Conc(lista,var,resul):
    if lista==[]:
        return resul+[var]
    else:
        var=var*(10**(len(str(lista[0]))))+(lista[0])
        return Conc(lista[1:],var,resul)
def Vuelve(lista,resul):
    if lista==[]:
        return (resul)
    else:
        return Vuelve(lista[1:],[lista[0]]+resul)
#Recibe numero
#
def f4(num,par=[],impar=[]):
    num=str(num)
    for elem in num:
        elem=int(elem)
        if elem%2==0:
            par+=[elem]
        else:
            impar+=[elem]
    par=(Conc(par,0,[]))[0]
    impar=(Conc(impar,0,[]))[0]
    print("Numero:",num)
    print("Pares:",par)
    print("Impares:",impar)
    print("Nuevo par:", f4auxpar(par))
    print("Nuevo Impar:", f4auximpar(impar))
    print("Suma:", (f4suma(num,par,impar)))
    print("Resta:",(f4resta(num,par,impar)))
    print("Multiplicación:", (f4mul(num,par,impar)))

def f4auxpar(num,i=0,resul=[]):
    num=str(num)
    for elem in num:
        elem=int(elem)
        if i%2==0:
            elem=elem+2
            resul+=[elem]
            i+=1
        else:
            elem=elem*3
            resul+=[elem]
            i+=1
    resul=Conc(resul,0,[])
    resul=resul[0]
    return resul

def f4auximpar(num,i=0,resul=[]):
    num=str(num)
    for elem in num:
        elem=int(elem)
        if i%2==0:
            elem=elem*3
            resul+=[elem]
            i+=1
        else:
            elem=elem+2
            resul+=[elem]
            i+=1
    resul=Conc(resul,0,[])
    resul=resul[0]
    return resul
    
def f4suma(num,num2,num3):
    return (eval("{}".format(num))+eval("{}".format(num2))+eval("{}".format(num3)))
def f4resta(num,num2,num3):
    return (eval("{}".format(num))-eval("{}".format(num2))-eval("{}".format(num3)))
def f4mul(num,num2,num3):
    return (eval("{}".format(num))*eval("{}".format(num2))*eval("{}".format(num3)))

