class Lista:
    valor=[]
    def insertarEnPosicion(self,elem,pos):
        temporal=[]
        flag=1
        for i in range(len(self.valor)):
            if i==pos:
                self.valor=temporal+[elem]+self.valor
                flag=0
                break
            else:
                temporal=temporal+[self.valor[0]]
                self.valor=self.valor[1:]
        if flag==1:
            self.valor=temporal+[elem]
    def insertarInicio(self,elem):
        self.valor=[elem]+self.valor
    def insertarFinal(self,elem):
        self.valor=self.valor+[elem]
    def imprimir(self):
        print(self.valor)
l=Lista()

opcion=""
while opcion!='0':
    print('1. Imprimir')
    print('2. Insertar al inicio')
    print('3. Insertar al final')
    print('4. Insertar en una posición específica')
    opcion = 
