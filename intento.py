#file = open("output.txt","w")
actual={1: ('1-', (0, 0), (0, 1)), 2: ('3/', (1, 0), (2, 0)), 3: ('1', (0, 2)), 4: ('6x', (1, 1), (1, 2)), 5: ('1-', (2, 1), (2, 2))}
matriz=[[0,0,1],[0,0,0],[0,0,0]]
error=0
import time

# function to check if the board is full or not
# returns true if it is full and false if it isn't
# it works on the fact that if it finds at least one 
# zero in the board it returns false
def isFull():
    global matriz
    for x in range(0, 3):
        for y in range (0, 3):
            if matriz[x][y] == 0:
                return False
    return True
def es_correcto():
    global error,matriz
    print(matriz)
    
    inicio_de_validacion()
    print("soyerrorarriba",error)
    
    if error ==1:
        error==0
        return False
    elif error==0:
        return True
    
# function to find all of the possible numbers
# which can be put at the specifies location by
# checking the horizontal and vertical and the 
# three by three square in which the numbers are
# housed
def possibleEntries( i, j):
    global matriz
    
    possibilityArray = {}
    
    for x in range (1, 4):
        possibilityArray[x] = 0
    
    #For horizontal entries
    for y in range (0, 3):
        if not matriz[i][y] == 0: 
            possibilityArray[matriz[i][y]] = 1
     
    #For vertical entries
    for x in range (0, 3):
        if not matriz[x][j] == 0: 
            possibilityArray[matriz[x][j]] = 1
            

    for x in range (1, 4):
        if possibilityArray[x] == 0:
            possibilityArray[x] = x
        else:
            possibilityArray[x] = 0
    
    return possibilityArray

# recursive function which solved the board and 
# prints it. 
def sudokuSolver():
    global matriz
    
    
    i = 0
    j = 0
    
    possiblities = {}
    
    # if board is full, there is no need to solve it any further
    if isFull() and es_correcto():
        print("Board Solved Successfully!")
        print(matriz)
        print("##########################")
        time.sleep(1)
        
        return  matriz

                
       
    else:
        # find the first vacant spot
        for x in range (0, 3):
            for y in range (0, 3):
                if matriz[x][y] == 0:
                    i = x
                    j = y
                    break
            else:
                continue
            break
        
        # get all the possibilities for i,j
        possiblities = possibleEntries(i, j)
        
        # go through all the possibilities and call the the function
        # again and again
        for x in range (1, 4):
            if not possiblities[x] == 0:
                matriz[i][j] = possiblities[x]
                #file.write(printFileBoard(board))
                sudokuSolver()
        # backtrack
        matriz[i][j] = 0

#agarra un diccionario y lo pasa a validar#
def inicio_de_validacion():
    global actual
    a=actual
    for i in a.values():
        validar_de_verdad(i)
    return
#agrara un elemento del diccionario y separa el operador del numero, tambien agarra los valores de la matriz en la tuple de la llave#
def validar_de_verdad(i):
        opera=""
        numero=""
        resul=[]
        lugar=[]
        for j in i:
            if type(j)==str:
                if operador(j)!="":
                    opera=operador(j)
                    numero=obtener_numero(j)
                else:
                    opera="#"
                    numero=obtener_numero(j)
            elif type(j)==tuple:
                lugar+=[j]
                resul+=[matriz[j[0]][j[1]]]
            
        resul.sort(reverse=True)
        return comprobar(resul,lugar,numero,opera)

#obtiene el numero de in string#
def obtener_numero(string):
    resul=""
    for j in string:
        if j=="0" or j=="1" or j=="2" or j=="3" or j=="4" or j=="5" or j=="6" or j=="7" or j=="8" or j=="9":
            resul+=j
    return resul
    
                
            

#saca el operador de un string#    
def operador(string):
    resul=""
    for i in string:
        if i=="+":
            resul="+"
        elif i=="/":
            resul="/"
        elif i=="x":
            resul="x"
        elif i=="-":
            resul="-"
    return resul
#esta funcion agarra los valoresde la matriz y ve que si operados dan el numero#
def comprobar(resultados,lugar,numero,oper):
    global error,error2
    if oper=="-":
        final=0
        for i in resultados:
            final-=int(i)
            final=abs(final)
        if int(final)==int(numero):
            None
        else:
            error=1
    
    elif oper=="+":
        final=0
        for i in resultados:
            final+=i
        if int(final)==int(numero):
            None
        else:
            error=1
        
    elif oper=="x":
        final=1
        print("R",resultados)
        print("num",numero)
        for i in resultados:
            final*=i
        print("final",final)
        print("evaluando",int(final)==int(numero))
        if int(final)==int(numero):
            None
        else:
            print("aqyui")
            error=1
            print(error)
        
    elif oper=="/":
        final=0
    
        for i in resultados:
            if final==0:
                final+=int(i)
            else:
                final/=int(i)
        
        if final==int(numero):
            None
        else:
            error=1
            
           
                
def main():
    global matriz
    sudokuSolver()
   
    

