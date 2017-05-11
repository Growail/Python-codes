#definicion de las clases
class Persona:
    nombre = ""
    direccion = ""
    telefono = ""
    cedula=""
    def Imprima(self):
        print("Nombre: ",self.nombre)
        print("dir.: ",self.direccion)
        print("tel.: ",self.telefono)
        print("cédula: ", self.cedula)
    

#programa
clientes = []   #lista de clientes
opcion = " "
while opcion.upper() != "S" :   #se sale hasta que "S"
    print("   1.  Ingresar clientes")
    print("   2.  Imprimir clientes")
    print("   S.  Salir")
    print("")
    opcion = input("   Digite la opcion y presione ENTER -->")
    if opcion == "1" :
        p = Persona()
        p.nombre = input("Digite el nombre :")
        p.direccion = input("Digite el direccion :")
        p.telefono = input("Digite el telefono :")
        p.cedula = input("Digite la cédula :")
        clientes.append(p)
    elif opcion == "2" :
        print("Lista de clientes :")
        print("-------------------")
        for i in range(len(clientes)):
            clientes[i].Imprima()
    elif opcion=="3":
        cont=0
        for i in clientes:
            cont+=1
        print(cont)
    elif opcion=="4":
        clienteBuscado = input("Ingrese la cédula del cliente a buscar :")
        encontro = -1       # no existe
        for i in range(len(clientes)):
            if clientes[i] == clienteBuscado :
                encontro = i
        if encontro != -1 :
            monto = int(input("Digite el monto del deposito :"))
            p[encontro].Depositar(monto)
        
    else :
        print("Gracias por usar el programa !!!")
        print("Fin")
