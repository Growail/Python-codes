#importamos el modulo del socket#
#IP de mi celular: 10.133.172.95
from socket import socket, error
#importamos los hilos#
from threading import Thread
nombre=""
class Client(Thread):
    def __init__(self, conn, addr):
        # Inicializar clase padre.
        Thread.__init__(self)
        self.conn = conn 
        self.addr = addr
    def run(self):
        while True:
            try:
                # Recibir datos del cliente.
                recibido = self.conn.recv(1024)#conn nombre del cliente#
                if recibido.decode("utf-8")=="close":
                    print("Usuario desconectado.")
                else:
                    print (recibido.decode("utf-8"))
                mensaje = input("Yo >> ")
                global nombre
                mensaje=nombre+" >>"+mensaje
            except error:
                print("[%s] Error de lectura." % self.name)
                break
            else:
                # Reenviar la información recibida.
                if mensaje:
                    
                    self.conn.send(mensaje.encode("utf-8"))
def main1():
    global nombre
    nombre=input("Nombre de usuario? ")
    print("Nombre aceptado")
    main()
    
def main():
    s = socket()
    # Escuchar peticiones en el puerto 6030.
    s.bind(("localhost", 6030))
    print("Conexión abierta")
    s.listen(1)
    while True:
        conn, addr = s.accept()
        c = Client(conn, addr)
        c.start()
        print("%s:%d se ha conectado." % addr)
if __name__ == "__main__":
    main1()
