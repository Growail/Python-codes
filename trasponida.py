def transpuesta(matriz):
    temp=[]
    result=[]
    while matriz[0]!=[]:
        for i in matriz:
            temp=temp+[i[0]]
            i=i.remove(i[0])
        result=result+[temp]
        temp=[]
    return result
            
##transpuesta([[1,2],[3,4],[5,6]])
