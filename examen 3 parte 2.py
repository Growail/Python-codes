def ej3(lista,result=[]):
    if lista==[]:
        total=len(result)
        return total
    elif type(lista[0])==list:
        return ej3(lista[1:],result+ej31(lista[0],[]))
    elif type(lista[0]!=list):
        return ej3(lista[1:],result+[lista[0]],)
    
def ej31(lista,result=[]):
    if lista==[]:
        total=len(result)
        return result
    elif type(lista[0])==list:
        return ej31(lista[1:],result+ej31(lista[0],[]))
    elif type(lista[0]!=list):
        return ej31(lista[1:],result+[lista[0]])   

def ej4(num):
    if num not in range(-101,101):
        return "ERROR!!"
    elif num==0:
        return [0,0]
    else:
        return f21(num,0)
def f21(num,var):
    if num==1 or num==-1:
        return [[num,var]]
    elif num<0:
        return [[num,var]]+f21(num+1,var-1)
    else:
        return [[num,var]]+f21(num-1,var+1)



