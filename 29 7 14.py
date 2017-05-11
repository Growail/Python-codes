#29/7/14
def mcm(num1, num2, num3):
    cont=1
    i=1
    while i>num1 and i>num2 and i>num3 :
        if num1%i==0 and num2%i==0 and num3%i==0:
            num1=num1/i
            num2=num2/i
            num3=num3/i
            cont=cont*i
            i=i+1
        else:
            i=i+1
    return i

def suma (num):
    i=0
    total=0
    while i>=num:
        total=total+(((i**3)*(i**2)*num)/n)
        i+=1
    return total
