class Calculadora():
    def _init_(self,operando1,operando2):
        self.op1=operando1
        self.op2=operando2
    def sumar (self):
        print(self.op1+self.op2)
    def restar (self):
        print(self.op1-self.op2)
    def multiplicar (self):
        print(self.op1*self.op2)
    def dividir (self):
        print(self.op1/self.op2)

ej=Calculadora()
ej._init_(10,2)
ej.sumar()
ej.restar()
ej.multiplicar()
ej.dividir()
