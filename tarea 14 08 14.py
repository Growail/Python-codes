def tarea1(num):
    if type(num)!=int:
        return "Error en la entrada"
    else:
        printable=str(num)
        lista1=[]
        for i in printable:
            lista1=lista1+[i]
        print ("Lista del número original:", lista1)
        impar=True
        lista2=[]
        posicion=0
        for i in lista1:
            if impar==True:
                lista2=lista2+[int(lista1[posicion])*3]
                impar=not impar
                posicion+=1
            else:
                lista2=lista2+[int(lista1[posicion])+2]
                impar=not impar
                posicion+=1
        print("Lista procesada:", lista2)

def elim(x,lista):
    if lista==[]:
        return "Error en lista"
    else:
        lista2=[]
        posicion=0
        for i in lista:
            if i==x:
                pass
            else:
                lista2=lista2+[i]
        return lista2

def mayor(lista):
    if lista==[]:
        return "Lista vacía"
    else:
        cont=0
        for i in lista:
            if i>cont:
                cont=i
            else:
                pass
        return cont
def ceros(lista):
    if lista==[]:
        return False
    else:
        for i in lista:
            if i==0:
                return True
            else:
                pass
        return False

##ordenamiento burbuja: es un algoritmo de ordenamiento, intercambia posiciones de los elementos en la lista para ver si están en el orden equivocado
##se detiene cuando no es necesario hacer más intercambios

##ordenamiento radix : es un algoritmo de ordenamiento, ordena números enteros revisando sus dígitos individuales

##ordenamiento shell: es una generalidad del algoritmo de ordenamiento por inserción que toma en cuenta dos aspectos
##-es eficiente si la entrada es casi ordenada    
##-es ineficiente en general porque mueve los valores de posición solo una vez

##ordenamiento merge: es un algoritmo de ordenamiento, se basa en dividir lo ordenable en pequeños segmentos más manejables

##ordenamiento heapsort: consiste en almacenar todos los elementos a ordenar en un "montículo" para extraer iteritivamente el nodo raíz hasta vaciar el montículo

