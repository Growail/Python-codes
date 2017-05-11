def tarea1(lista):
    if type(lista)!=list:
        return "Error en la entrada"
    elif lista==[]:
        return "Lista Vacía"
    else:
        for i in lista:
            
                
            
        return True

def tarea3(lista1,lista2):
    if len(lista1)<6 or len(lista2)<6 or len(lista1)!=len(lista2):
        return "listas inválida"
    elif len(lista1)%6!=0:
        return "Error: La lista debe medir un múltiplo de 6"
    elif len(lista1)==6:
        listaresult=[lista1[0],lista2[2],lista2[3],lista1[3],lista1[4],lista2[0],lista2[1],lista1[1],lista1[2],lista2[4],lista2[5],lista2[0]]]
        return listaresult
    elif len(lista1)>6:
        while len(lista1)>=6:
            listaresult=[]
            listaresult=listaresult+[lista1[0],lista2[2],lista2[3],lista1[3],lista1[4],lista2[0],lista2[1],lista1[1],lista1[2],lista2[4],lista2[5],lista2[0]]]
            lista1=lista1[6:]
            lista2=lista2[6:]
        return listaresult
            
