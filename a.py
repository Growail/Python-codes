def f1(num):
    if num not in range(-101,101):
        return "ERROR!!"
    elif num==0:
        return [0,0]
    else:
        return f2(num,0)
def f2(num,var):
    if num==1 or num==-1:
##        lista+=[[num,var]]
        return [[num,var]]
    elif num<0:
##        lista+=[[num,var]]
##        var=var-1
##        num=num+1
        return [[num,var]]+f2(num+1,var-1)
    else:
##        lista+=[[num,var]]
##        var=var+1
##        num=num-1
        return [[num,var]]+f2(num-1,var+1)
