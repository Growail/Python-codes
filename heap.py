def heap(lista):
    for i in range(len(lista)):
        nuevallave=0
        padre=0
        siguiente=0
        auxiliar=0
        siguiente=i
        padre=siguiente//2
        lista[siguiente]=nuevallave
        while (siguiente != 0 and lista[padre]<=lista[siguiente]):
            auxiliar=lista[padre]
            lista[padre]=lista[siguiente]
            lista[siguiente]=auxiliar
            siguiente=padre
            padre=siguiente//2
    return lista
