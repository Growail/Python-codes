def distancia(épsilon,cantidad):
    if épsilon<=0 or cantidad<1:
        print("Error: Parámetros incorrectos")
    else:
        d1(épsilon,cantidad)
def d1(e,n):
    numeros=[]
    marca=3
    while n!=0:
        if (marca**2-2)<(7+e) and (marca**2-2)>7:
            numeros+=[marca]
            marca+=0.000000001
            n-=1
        else:
            marca+=0.000000001
    print(numeros)
        
        

        
        
