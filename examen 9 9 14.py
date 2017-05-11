import math
def candig(num):
    if num==0:
        return 1
    else:
        cont=0
        while num!=0:
            cont+=1
            num=num//10
        return cont


def conv(n):
    listanormal=[]
    while n!=0:
        listanormal=[n%10]+listanormal
        n=n//10
    return listanormal

def ordenar(num,lista):
    lista=lista+[num]
    return orden(lista)
    

def orden(lista):
    menor = []
    igual = []
    mayor = []

    if len(lista) > 1:
        flag = lista[0]
        for x in lista:
            if x < flag:
                menor.append(x)
            if x == flag:
                igual.append(x)
            if x > flag:
                mayor.append(x)
        return orden(menor)+igual+orden(mayor)
    else:
        return lista


            
               
def examen1(n1,n2):
    if type(n1)==type(n2)==int:
        ins=[]
        lista=[]
        if candig(n1)>=candig(n2):
            num1=n1
            num2=n2
        else:
            num1=n2
            num2=n1
        num1=conv(num1)
        num2=conv(num2)
        cont=0
        for i in num2:
            ins=ordenar(i,ins)
            ins=ordenar((num1[cont]),ins)
            cont+=1
            lista=lista+[ins]
        num1=num1[cont:]
        for i in num1:
            ins=ordenar[i,ins]
            lista=lista+ins
        return lista
            
    else:
        return "Error en las entradas"

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return(n*fact(n-2))



        
def f2(x):
    if type(x)!=int:
        return ('ERROR')
    else:
        x=conv(x)
        resul=[]
        lista=[]
        for n in x:
            lista=lista+[n,math.factorial(n),(fact(n))]
            resul+=[lista]
            lista=[]
        print(resul)
        numeros=0
        factoriales=0
        dfactoriales=0
        for elem in resul:
            numeros+=elem[0]
            factoriales+=elem[1]
            dfactoriales+=elem[2]
        return([numeros,factoriales,dfactoriales])
    
            
            
