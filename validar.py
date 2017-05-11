actual={1: ('1-', (0, 0), (0, 1)), 2: ('3÷', (1, 0), (2, 0)), 3: ('1', (0, 2)), 4: ('6x', (1, 1), (1, 2)), 5: ('1-', (2, 1), (2, 2))}
matriz=[[2,3,1],[1,2,3],[3,1,2]]
boton=[[0,0,0],[0,0,0],[0,0,0]]
def inicio_de_validacion():
    global actual
    a=actual
    for i in a.values():
        print(i)
        validar_de_verdad(i)
    return
        
def validar_de_verdad(i):
        opera=""
        numero=""
        resul=[]
        lugar=[]
        for j in i:
            if type(j)==str:
                if operador(j)!="":
                    opera=operador(j)
                    numero=obtener_numero(j)
                else:
                    opera="#"
                    numero=obtener_numero(j)
            elif type(j)==tuple:
                lugar+=[j]
                resul+=[matriz[j[0]][j[1]]]
            
        resul.sort(reverse=True)
        return comprobar(resul,lugar,numero,opera)


def obtener_numero(string):
    resul=""
    for j in string:
        if j=="0" or j=="1" or j=="2" or j=="3" or j=="4" or j=="5" or j=="6" or j=="7" or j=="8" or j=="9":
            resul+=j
    return resul
    
                
            
            
    
def operador(string):
    resul=""
    for i in string:
        if i=="+":
            resul="+"
        elif i=="÷":
            resul="÷"
        elif i=="x":
            resul="x"
        elif i=="-":
            resul="-"
    return resul

def comprobar(resultados,lugar,numero,oper):
    global boton
    print("entre")
    print(oper)
    print(resultados)
    print(lugar)
    if oper=="-":
        final=0
        for i in resultados:
            if final==0:
                final+=i
            else:
                final-=i
        if int(final)==int(numero):
            None
        else:
            for i in lugar:

                boton[i[0]][i[1]].config(bg="red")
    elif oper=="+":
        final=0
        for i in resultados:
            if final==0:
                final+=i
            else:
                final+=i
        if int(final)==int(numero):
            None
        else:
            for i in lugar:

                boton[i[0]][i[1]].config(bg="red")
    elif oper=="x":
        final=1
        for i in resultados:
            if final==1:
                final*=i
            else:
                final*=i
        if int(final)==int(numero):
            None
        else:
            for i in lugar:
                boton[i[0]][i[1]].config(bg="red")
    elif oper=="÷":
        final=0
        for i in resultados:
            if final==0:
                final+=i
            else:
                final//=i
        if int(final)==int(numero):
            None
        else:
            for i in lugar:

                boton[i[0]][i[1]].config(bg="red")
    elif oper=="#":
        final=0
        for i in resultados:
                final+=i
        if int(final)==int(numero):
            None
        else:
            for i in lugar:
                boton[i[0]][i[1]].config(bg="red")

