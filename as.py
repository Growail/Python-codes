def divisores(num,divisor):
    if divisor==num:
        return num
    elif num%divisor==0:
        return divisor
    else:
        return divisores(num,divisor+1)

def mcm(num1,num2,num3):
    if num1==num2==num3==0:
        return 0
    else:
        l=[num1,num2,num3]
        n3=max(l)
        n1=min(l)
        l.remove(n1)
        l.remove(n3)
        n2=l[0]
        return mcm1(n1,n2,n3)

def mcm1(num1,num2,num3,result=1,div=2):
    if num1==1:
        return mcm2(num2,num3,result,2)
    elif num1%div==0 and num2%div==0 and num3%div==0:
        return mcm1(num1//div,num2//div,num3//div,result*div,div)
    elif num1%div==0 and num2%div==0:
        return mcm1(num1//div,num2//div,num3,result*div,div)
    elif num1%div==0 and num3%div==0:
        return mcm1(num1//div,num2,num3//div,result*div,div)
    elif divisores(num1,2)<num1:
        return mcm1(num1//div,num2,num3,result*div,div)
    else:
        return mcm1(num1,num2,num3,result,div+1)

def mcm2(num2,num3,result,div):
    if num2==1:
        return mcm3(num3,result,2)
    elif num2%div==0 and num3%div==0:
        return mcm2(num2//div,num3//div,result*div,div)
    elif divisores(num2,2)<num2:
        return mcm2(num2//div,num3,result*div,div)
    else:
        return mcm2(num2,num3,result,div+1)
    
def mcm3(num3,result,div):
    if num3==1:
        return result
    elif divisores(num3,2)<num3:
        return mcm3(num3//div,result*div,div)
    else:
        return mcm3(num3,result,div+1)





def f3(num1,num2,num3,i=0,mayor=0):
    if i ==0: 
        if num1>num2 and num1>num3:
            f3(num1,num2,num3,1,num1)
        elif num2>num1 and num2>num3:
            f3(num1,num2,num3,1,num2)
        else:
            f3(num1,num2,num3,1,num3)
    else:
        while True:
            if (mayor%num1==0) and (mayor%num2==0) and (mayor%num3==0):
                resul=mayor
                break
            mayor+=1
        return resul














    
        
    
