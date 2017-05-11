#definicion de las clases
class Cuenta:
    numeroCuenta= 0
    nombreCliente=""
    ID=0
    saldo= 0
    totalDepositos=0
    cantidadDepositos=0
    totalRetiros=0
    cantidadRetiros=0
    estado= "Activa"
    
    def Depositar(self,p):
        self.saldo = self.saldo + p
        self.totalDepositos+=p
        self.cantidadDepositos+=1
    def Retirar(self,p):
        self.saldo = self.saldo - p
        self.totalRetiros+=p
        self.cantidadRetiros+=1
    def ImprimirSaldo(self):
        print("El saldo de la cuenta es ",self.saldo)
    def Imprima(self):
        print("Número de cuenta: ",self.numeroCuenta)
        print("Nombre del cliente: ",self.nombreCliente)
        print("Identificación del cliente: " ,self.ID)
        print("Saldo actual: ",self.saldo) 
        print("Monto total depositado: ",self.totalDepositos)
        print("Cantidad de depósitos: ",self.cantidadDepositos)
        print("Monto total retirado: ",self.totalRetiros)
        print("Cantidad de retiros: ",self.cantidadRetiros)
        print("Estado de la cuenta: ",self.estado)
        print("                ")
        print("                ")
    def Activar(self):
        self.estado="Activa"
        print("Se ha activado con éxito")
    def Cerrar(self):
        self.estado="Inactiva"
        print("Se ha cerrado con éxito")
        
    
    

#programa
cuentas = []    #lista de cuentas


opcion = " "
while opcion.upper() != "S" :   #se sale hasta que "S"
    print("                ")
    print("                ")
    print("   1.  Crear cuenta")
    print("   2.  Imprimir saldo")
    print("   3.  Hacer deposito")
    print("   4.  Hacer retiro")
    print("   5.  Ver estado de cuenta")
    print("   6.  Activar una cuenta")
    print("   7.  Cerrar una cuenta")
    print("   8.  Imprimir cuentas")
    print("   S.  Salir")
    print("")
    opcion = input("   Digite la opcion y presione ENTER -->")
    if opcion == "8" :
        print("Cuentas registradas :")
        print("-------------------")
        for i in range(len(cuentas)):
            cuentas[i].Imprima()
        print("-------------------")
    elif opcion == "1" :
        c = Cuenta()
        c.numeroCuenta = int(input("Digite el numero de cuenta : "))
        c.nombreCliente=input("Digite su nombre : ")
        c.ID=int(input("Digite su cédula : "))
        cuentas.append(c)
    elif opcion == "3" :
        #buscar la cuenta y despues si existe, depositar
        cuentaBuscada = int(input("Ingrese la cuenta para deposito : "))
        encontro = -1       # no existe
        for i in range(len(cuentas)):
            if cuentas[i].numeroCuenta == cuentaBuscada :
                encontro = i
        if encontro != -1 :
            if cuentas[encontro].estado!="Inactiva":
                monto = int(input("Digite el monto del deposito :"))
                cuentas[encontro].Depositar(monto)
                print("Se ha depositado con éxito")
            else:
                print("Cuenta inactiva")
        else :
            print("La cuenta digitada no existe")
    elif opcion == "2" :
        #buscar la cuenta y despues si existe, consultar
        cuentaBuscada = int(input("Ingrese el número de cuenta a consultar :"))
        encontro = -1       # no existe
        for i in range(len(cuentas)):
            if cuentas[i].numeroCuenta == cuentaBuscada :
                encontro = i
        if encontro != -1 :
            cuentas[encontro].ImprimirSaldo()
        else :
            print("La cuenta digitada no existe")
    elif opcion == "4" :
        #buscar la cuenta y despues si existe, retirar
        cuentaBuscada = int(input("Ingrese la cuenta para retiro : "))
        encontro = -1       # no existe
        for i in range(len(cuentas)):
            if cuentas[i].numeroCuenta == cuentaBuscada :
                encontro = i
        if encontro != -1 :
            if cuentas[encontro].estado!="Inactiva":
                monto = int(input("Digite el monto del retiro :"))
                if (cuentas[encontro].saldo)<(monto):
                    print("Fondos insuficientes")
                else:
                    cuentas[encontro].Retirar(monto)
                    print("Se ha retirado con éxito")
            else:
                print("Cuenta inactiva")
        else :
            print("La cuenta digitada no existe")
    elif opcion=="5":
        #buscar la cuenta y despues si existe, imprimir
        cuentaBuscada = int(input("Ingrese el número de cuenta a consultar :"))
        encontro = -1       # no existe
        for i in range(len(cuentas)):
            if cuentas[i].numeroCuenta == cuentaBuscada :
                encontro = i
        if encontro != -1 :
            cuentas[encontro].Imprima()
        else :
            print("La cuenta digitada no existe")
    elif opcion=="6":
        #buscar la cuenta y despues si existe, activar
        cuentaBuscada = int(input("Ingrese el número de cuenta a activar :"))
        encontro = -1       # no existe
        for i in range(len(cuentas)):
            if cuentas[i].numeroCuenta == cuentaBuscada :
                encontro = i
        if encontro != -1 :
            cuentas[encontro].Activar()
        else :
            print("La cuenta digitada no existe")
    elif opcion=="7":
        #buscar la cuenta y despues si existe, cerrar
        cuentaBuscada = int(input("Ingrese el número de cuenta a cerrar :"))
        encontro = -1       # no existe
        for i in range(len(cuentas)):
            if cuentas[i].numeroCuenta == cuentaBuscada :
                encontro = i
        if encontro != -1 :
            cuentas[encontro].Cerrar()
        else :
            print("La cuenta digitada no existe")
        
        
 
        
    else :
        print("Gracias por usar el programa !!!")
        print("Fin")
