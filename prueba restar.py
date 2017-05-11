def restar(dicci):
    d=dicci
    for i in d.keys():
        resultado=[]
        for j in d[i]:
            if type(j)==str:
                resultado+=[j]
            elif type(j)==tuple:
                a=list(j)
                a[0]-=1
                a[1]-=1
                j=tuple(a)
                resultado+=[j]
        d[i]= tuple(resultado)
    return d
