def listaEntera(lista):
    if lista==[]:
        return []
    contador=0
    listaImpar=[]
    while contador<len(lista):
        if lista[contador]%2==1:
            listaImpar+=[lista[contador]]
            contador+=1
        else:
            contador+=1
    return listaImpar
        
