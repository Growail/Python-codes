def orden(lista):
    for i in range(len(lista)-1):
        if lista[i]<=lista[i+1]:
            pass
        else:
            return False
    return True
def radix(lista):
    work=lista
    potencia=0
    for i in lista:
        lista0=lista1=lista2=lista3=lista4=lista5=lista6=lista7=lista8=lista9=[]
        if orden(lista):
            pass
        else:
            potencia=potencia+1
            for j in lista:
                if ((j%10**potencia)//10**(potencia-1))==0:
                    lista0=lista0+[j]
                elif ((j%10**potencia)//10**(potencia-1))==1:
                    lista1=lista1+[j]
                elif ((j%10**potencia)//10**(potencia-1))==2:
                    lista2=lista2+[j]
                elif ((j%10**potencia)//10**(potencia-1))==3:
                    lista3=lista3+[j]
                elif ((j%10**potencia)//10**(potencia-1))==4:
                    lista4=lista4+[j]
                elif ((j%10**potencia)//10**(potencia-1))==5:
                    lista5=lista5+[j]
                elif ((j%10**potencia)//10**(potencia-1))==6:
                    lista6=lista6+[j]
                elif ((j%10**potencia)//10**(potencia-1))==7:
                    lista7=lista7+[j]
                elif ((j%10**potencia)//10**(potencia-1))==8:
                    lista8=lista8+[j]
                elif ((j%10**potencia)//10**(potencia-1))==9:
                    lista9=lista9+[j]
            lista=[]
            lista=lista0+lista1+lista2+lista3+lista4+lista5+lista6+lista7+lista8+lista9
    return lista
def seleccion (lista) : 
   for i in range(0, len(lista)-1) : 
    indiceMenor=i 
    for j in range(i+1, len(lista)) : 
      if lista[j]<lista[indiceMenor] : 
        indiceMenor=j 
      if i!=indiceMenor : 
          lista[i],lista[indiceMenor]=lista[indiceMenor],lista[i] 
   return lista 

def insercion (lista) : 
  for i in range(1,len(lista)) : 
    aux=lista[i] 
    j=i 
    while j>0 and aux<lista[j-1] : 
      lista[j]=lista[j-1] 
      j-=1 
    lista[j]=aux 
  return lista 
