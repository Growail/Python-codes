import math
def candig(n):
    result=0
    if n==0:
        return 1
    else:
        while n!=0:
            n=n//10
            result=result+1
        return result

def tarea(n):
    if n>=0:
        result=0
        i=n
        while i>=0:
            result=result+(((i**3)+(i**4)+(i**5))**5)*(((n**4)+(i**3))**2)
            i=i-1
        return result
    else:
        return "Error"

def tarea2(n):
    if n>=0:
        result=0
        i=n
        while i>=0:
            result=result+((((math.factorial(n))**2)**2)+(i**n))
            i=i-1
        return result
    else:
        return "Error"

def tarea3(n):
    if n>=0:
        result=0
        i=n
        while i>=0:
            result=result+((((i**3)+(n**4)+(i**5))**5)*((n**(n-i))+(i**3)**2)**2)
            i=i-1
        return result
    else:
        return "Error"

def quiz(n):
    if n>=0:
        result=0
        resulti=0
        i=1
        while i<=n:
            result=result+((math.factorial(n)*((i+1)**n))**2)
            resulti=resulti+((math.factorial(n+i))/2)
            i=i-1
        return result/resulti
    else:
        return "Error"

def wtf(num1,num2,num3):
    result=0
    potencia=0
    n=num1
    while num2!=0:
        result=result+((((num1//(10**(candig(num1)-1)))*10**2)+((num2%10)*(10**1))+((num3//(10**(candig(num3)-1)))*10**0))*(10**potencia))
        potencia=potencia+3
        num1=num1%10**(candig(num1)-1)
        num2=num2//10
        num3=num3%10**(candig(num1)-1)
        
    return result
                       
def cambiaceros(num):
    if num<1:
        return "Número inválido"
    else:
        result=0
        potencia=0
        while num!=0:
            if num%10==0:
                result=result+(1*(10**potencia))
                potencia+=1
                num=num//10
            else:
                result=result+((num%10)*(10**potencia))
                potencia+=1
                num=num//10
        return result
                
def quiztaller(num):
    if num>0:
        if num==0:
            return 0
        else:
            pila=[]
            while num!=0:
                pila+=[(num%10)+(num//10**(candig(num)-1))]
                num=num//10
                num=num%10**(candig(num)-1)
                if candig(num)==1:
                    pila+=[num]
                    num=0
            potencia=len(pila)-1
            result=0
            while pila!=[]:
                if candig(pila[0])==2:
                    result=result+(pila[0]*10**potencia)
                    potencia=potencia-2
                    pila=pila[1:]
                else:
                    result=result+(pila[0]*10**potencia)
                    potencia=potencia-1
                    pila=pila[1:]
            return result
    else:
        return "Error"
def revuelta(num):
    result=0
    potencia=0
    while num!=0:
        if (num//10**(candig(num)-1))%2==0:
                result+=((num//10**(candig(num)-1))+3)*10**potencia
                potencia+2
                num=num%10**(candig(num)-1)
        else:
                result+=((num//10**(candig(num)-1))*2)*10**potencia
                potencia+1
                num=num%10**(candig(num)-1)
    return result
                
            
            
    

        
            
    
