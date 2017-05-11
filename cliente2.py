from socket import socket
nombre=""
def main1():
    global nombre
    nombre=input("Nombre de usuario? ")
    print("Nombre aceptado")
    main()
def main():
    s = socket()
    s.connect(("localhost", 6030))
    print("Conexión establecida")
    while True:
        mensaje = input("Yo >> ")
        if mensaje=="close":
            mensaje="close"
        else:
            global nombre
            mensaje=nombre+" >>"+mensaje
##        print("Yo:",mensaje)
        #Con la instancia del objeto servidor (s) y el metodo send, enviamos el mensaje introducido
        s.send(mensaje.encode("utf-8"))
        if mensaje=="close":
            return
        mensaje=s.recv(1024).decode("utf-8")
        print(mensaje)
if __name__ == "__main__":
    main1()
