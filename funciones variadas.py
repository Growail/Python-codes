lista1=[]
lista0=[]
lista2=[]
def funcodigo(s):
    if len(s)!=3:
        return "Error"
    else:
        global lista1
        for i in lista1:
            if i==s:
                return "Ya está incluido"
            else:
                pass
        lista1+=[s]
        return True
def funnombre(n,s):
    if type(n)!=type(s)!=str:
        return "Error en las entradas"
    else:
        global lista0
        if funcodigo(s):
            lista0+=[n]
        
        
def fusion_ha():
    global lista0
    global lista1
    global lista2
    p=0
    lista2=[]
    for i in lista1:
        lista2+=[[lista0[p],i]]
        p+=1
    return lista2
