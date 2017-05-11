import math
from math import *
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return(n*fact(n-2))

def conv(num):
    listanormal=[]
    while num!=0:
        listanormal=[num%10]+listanormal
        num=num//10
    return listanormal

        
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
