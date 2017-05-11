def arbol(raiz,hijoizq=[], hijoder=[]):
    if hijoizq==[] and hijoder==[]:
        return raiz
    else:
        return [raiz]+[hijoizq]+[hijoder]

def irordenando(lista):
    if len(lista)<=3:
        return arboldelista(lista)
    else:
        lista1=lista[0:3]
        print(lista1)
        return arboldelista(lista1)
def arboldelista(raiz):
    if len(raiz)==1:
        return raiz
    elif len(raiz)==2:
        if raiz[1]<raiz[0]:
            return [raiz[0],raiz[1],[]]
        else:
            return [raiz[0],[],raiz[1]]
    else:
        return raiz
            
def atomo(x):
    if type(x)!=list:
        return True
    else:
        return False

def raiz(arbol):
    if atomo(arbol):
        return arbol
    else:
        return arbol[0]

def hijoizq(arbol):
    if atomo(arbol):
        return []
    else:
        return arbol[1]

def hijoder(arbol):
    if atomo(arbol):
        return []
    else:
        return arbol[2]
def inOrden(arbol):
    if arbol==[]:
        return []
    elif atomo(arbol):
        return [arbol]
    else:
        return inOrden(hijoizq(arbol))+[raiz(arbol)]+inOrden(hijoder(arbol))

def preOrden(arbol):
    if arbol==[]:
        return []
    elif atomo(arbol):
        return [raiz(arbol)]
    else:
        return [raiz(arbol)]+preOrden(hijoizq(arbol))+preOrden(hijoder(arbol))

def insertList(arbol,ele):
    l1=(inOrden(arbol))
    print(l1)
    l1.sort()
    l2=preOrden(arbol)
    l3=[]
    l4=[]
    raiz=[]
    while l1!=[]:
        if l1[0]==l2[0]:
            l4=l1[1:]
            raiz=l1[0]
            return arbolizar([raiz]+[l3]+[l4])
        else:
            l3+=[l1[0]]
            l1=l1[1:]

            
def arbolizar(lista):
    print(irordenando(lista[1]))
    return [lista[0],irordenando(lista[1]),irordenando(lista[2])]
            
    
