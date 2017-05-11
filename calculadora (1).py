import tkinter
from tkinter import *
import tkinter as tk


def conv_dec_bin(num):
    if type(num)==int:
        if num>=0:
            b=0
            p=0
            while num>0:
                b+=num%2*(10**p)
                p+=1
                num=num//2
            return b
        else:
            return 'Syntax error'
    else:
        return 'Syntax error'
    
def conv_dec_oct(num):
    if type(num)==int:
        if num>=0:
            o=0
            p=0
            while num>0:
                o+=num%8*(10**p)
                p+=1
                num=num//8
            return o
        else:
            return 'Syntax error'
    else:
        return 'Syntax error'


def conv_bin_dec(b):
    if type(b)==int:
        if comprobar_binario(b)==True:
            d=0
            p=0
            while b>0:
                d+=(b%10)*(2**p)
                p+=1
                b=b//10
            return d
        else:
            return 'Syntax error'
    else:
        return 'Syntax errorr'


def comprobar_binario(b):
    while b!=0:
        if b%10 ==0 or b%10 ==1:
            b=b//10
        else:
            return False
    return True


def conv_oct_dec(o):
    if type(o)==int:
        if comprobar_octal(o)==True:
            d=0
            p=0
            while o>0:
                d+=(o%10)*(8**p)
                p+=1
                o=o//10
            return d
        else:
            return 'Syntax errorl'
    else:
        return 'Syntax error'


def comprobar_octal(o):
    while o!=0:
        if o%10==0 or o%10==1 or o%10==2 or o%10==3 or o%10==4 or o%10==5 or o%10==6 or o%10==7:
            o=o//10
        else:
            return False
    return True


def conv_dec_hex(n):
    if type(n)==int:
        h=''
        if n>=0:
            while n>0:
                if n%16==0:
                    h+='0'
                    n=n//16
                elif n%16==1:
                    h+='1'
                    n=n//16
                elif n%16==2:
                    h+='2'
                    n=n//16
                elif n%16==3:
                    h+='3'
                    n=n//16
                elif n%16==4:
                    h+='4'
                    n=n//16
                elif n%16==5:
                    h+='5'
                    n=n//16
                elif n%16==6:
                    h+='6'
                    n=n//16
                elif n%16==7:
                    h+='7'
                    n=n//16
                elif n%16==8:
                    h+='8'
                    n=n//16
                elif n%16==9:
                    h+='9'
                    n=n//16
                elif n%16==10:
                    h+='A'
                    n=n//16
                elif n%16==11:
                    h+='B'
                    n=n//16
                elif n%16==12:
                    h+='C'
                    n=n//16
                elif n%16==13:
                    h+='D'
                    n=n//16
                elif n%16==14:
                    h+='E'
                    n=n//16
                elif n%16==15:
                    h+='F'
                    n=n//16
            return invertirstr(h)
        return 'Syntax error'


def invertirstr(string):
    if len(string)==1:
        return string
    else:
        return string[-1]+invertirstr(string[:-1])


def conv_hex_dec(string):
    if type(string)==str:
        string=string.lower()
        if comprobar_hex(string)==True:
            b=''
            while string !='':
                if string[0]=='0':
                    b+='0000'
                    string=string[1:]
                elif string[0]=='1':
                    b+='0001'
                    string=string[1:]
                elif string[0]=='2':
                    b+='0010'
                    string=string[1:]
                elif string[0]=='3':
                    b+='0011'
                    string=string[1:]
                elif string[0]=='4':
                    b+='00100'
                    string=string[1:]
                elif string[0]=='5':
                    b+='0101'
                    string=string[1:]
                elif string[0]=='6':
                    b+='0110'
                    string=string[1:]
                elif string[0]=='7':
                    b+='0111'
                    string=string[1:]
                elif string[0]=='8':
                    b+='1000'
                    string=string[1:]
                elif string[0]=='9':
                    b+='1001'
                    string=string[1:]
                elif string[0]=='a':
                    b+='1010'
                    string=string[1:]
                elif string[0]=='b':
                    b+='1011'
                    string=string[1:]
                elif string[0]=='c':
                    b+='1100'
                    string=string[1:]
                elif string[0]=='d':
                    b+='1101'
                    string=string[1:]
                elif string[0]=='e':
                    b+='1110'
                    string=string[1:]
                elif string[0]=='f':
                    b+='1111'
                    string=string[1:]
            return conv_bin_dec(int(b))
        return 'Syntax error'
    return 'Syntax error'


def comprobar_hex(s):
    s=s.lower()
    while s!='':
        if s[0]=='0' or s[0]=='1' or s[0]=='2' or s[0]=='3' or s[0]=='4' or s[0]=='5' or s[0]=='6' or s[0]=='7' or s[0]=='8' or s[0]=='9' or s[0]=='a' or s[0]=='b' or s[0]=='c' or s[0]=='d' or s[0]=='e' or s[0]=='f':
            s=s[1:]
        else:
            return False
    return True

def conv_bin_oct(b):
    if type(b)==int:
        if comprobar_binario(b)==True:
            return conv_dec_oct(conv_bin_dec(b))
        else:
            return 'Syntax error'
    else:
        return 'Syntax error'

def conv_bin_hex(b):
    if type(b)==int:
        if comprobar_binario(b)==True:
            return conv_dec_hex(conv_bin_dec(b))
        else:
            return 'Syntax error'
    else:
        return 'Syntax error'


def conv_oct_bin(b):
    if type(b)==int:
        if comprobar_octal(b)==True:
            return conv_dec_bin(conv_oct_dec(b))
        else:
            return 'Syntax error'
    else:
        return 'Syntax error'



def conv_oct_hex(b):
    if type(b)==int:
        if comprobar_octal(b)==True:
            return conv_dec_hex(conv_oct_dec(b))
        else:
            return 'Syntax error'
    else:
        return 'Syntax error'


def conv_hex_bin(s):
    if type(s)==str:
        s=s.lower()
        if comprobar_hex(s)==True:
            return conv_dec_bin(conv_hex_dec(s))
        else:
            return 'Syntax error'
    else:
        return 'Syntax error'


def conv_hex_oct(s):
    if type(s)==str:
        if comprobar_hex(s)==True:
            return conv_dec_oct(conv_hex_dec(s))
        else:
            return 'Syntax error'
    else:
        return 'Syntax error'



def suma_bin(num1,num2):
        if comprobar_binario(num1) == True and comprobar_binario(num2)==True:
            num1=str(num1)
            num2=str(num2)
            if len(num1)==len(num2):
                return suma_bin_aux(num1,num2)
            elif len(num1)<len(num2):
                return suma_bin_aux(completar_ceros(num1,num2),num2)
            else:
                return suma_bin_aux(num1,completar_ceros(num2,num1))
        else:
            return 'Syntax error'


def completar_ceros(n1,n2):
    while len(n1) != len(n2):
        n1='0'+n1
    return n1
                
           
    

def suma_bin_aux(num1,num2):
    acarreo=0
    result=''
    while num1 != '':
        if num1[-1]=='0' and num2[-1]=='0':
            if acarreo== 0:
                result +='0'
                num1= num1[:-1]
                num2= num2[:-1]
            else:
                result +='1'
                num1= num1[:-1]
                num2= num2[:-1]
                acarreo=0

        if num1[-1]=='0' and num2[-1]=='1':
            if acarreo== 0:
                result +='1'
                num1= num1[:-1]
                num2= num2[:-1]

            else:
                result +='0'
                num1= num1[:-1]
                num2= num2[:-1]
                acarreo= 1

        elif num1[-1]=='1' and num2[-1]=='0':
            if acarreo== 0:
                result +='1'
                num1= num1[:-1]
                num2= num2[:-1]

            else:
                result +='0'
                num1= num1[:-1]
                num2= num2[:-1]
                acarreo= 1

        elif num1[-1]=='1' and num2[-1]=='1':
            if acarreo== 0:
                result +='0'
                num1= num1[:-1]
                num2= num2[:-1]
                acarreo= 1

            else:
                result +='1'
                num1= num1[:-1]
                num2= num2[:-1]
                acarreo= 1
    if acarreo==0:
        return invertir(result)
    return str(acarreo)+invertir(result)


def invertir(num):
    result=''
    while num != '':
        result += num[-1]
        num = num[:-1]
    return result


def suma_oct(o1,o2):
    if type(o1)==int and type(o2)==int:
        if comprobar_octal(o1)==True and comprobar_octal(o2)==True:
            o1=str(o1)
            o2=str(o2)
            if len(o1)==len(o2):
                return suma_oct_aux(o1,o2)
            elif len(o1)<len(o2):
                return suma_oct_aux(completar_ceros(o1,o2),o2)
            else:
                return suma_oct_aux(o1,completar_ceros(o2,o1))
        else:
            return 'Syntax error'
    else:
        return 'Syntax error'


def suma_oct_aux(o1,o2):
    acarreo=0
    r=''
    while o1!='':
        re= str((conv_dec_oct(int(o1[-1])+int(o2[-1])+acarreo))%10)
        r+=re
        acarreo=(conv_dec_oct(int(o1[-1])+int(o2[-1])+acarreo))//10
        o1=o1[:-1]
        o2=o2[:-1]
    if acarreo==0:
        return invertir(r)
    return str(acarreo)+invertir(r)


def suma_hex(h1,h2):
    if type(h1)==str and type(h2)==str:
  
        if comprobar_hex(h1)==True and comprobar_hex(h2)==True:
            return conv_bin_hex(int(suma_bin(conv_hex_bin(h1),conv_hex_bin(h2))))
        else:
            return 'Syntax error'
    else:
        return 'Syntax error'


def resta_bin(num1,num2):
    if type(num1)==int and type(num2)==int:
        if comprobar_binario(num1)==True and comprobar_binario(num2)==True:
            num1=str(num1)
            num2=str(num2)
            if len(num1)==len(num2):
                return resta_bin_aux(num1,num2)
            elif len(num1)<len(num2):
                return resta_bin_aux(completar_ceros(num1,num2),num2)
            else:
                return resta_bin_aux(num1,completar_ceros(num2,num1))
        else:
            return 'Syntax error'
    else:
        return 'Syntax error'
            


def resta_bin_aux(num1,num2):
    result=''
    
    while num1 != '':
        if conv_bin_dec(num1) < conv_bin_dec(num2):
            result = invertir(suma_bin_aux(num1, complemento(num2)))
            return '-' + complemento(result)
        else:
            if num1[-1] == num2[-1]:
                result += '0'
                num1= num1[:-1]
                num2= num2[:-1]

            elif num1[-1] == '1' and num2[-1]=='0':
                result += '1'
                num1= num1[:-1]
                num2= num2[:-1]

            elif num1[-1] =='0' and num2[-1]== '1':
                result += '1'
                num1= prestamo(num1)[:-1]
                num2= num2[:-1]

    return invertir(result)

    
            
                        
def Not(num):
    result = ''
    while num != '':
        if num[0] == '0':
            result += '1'
            num = num[1:]
        else:
            result += '0'
            num = num[1:]
    return result

def complemento(num):
    return suma_bin_aux(Not(num),completar_ceros('1',Not(num)))



def prestamo(numero):
    result = ''
    while numero != '':
        if numero[-1] == '0':
            result += '1'
            numero = numero[:-1]
        elif numero[-1] == '1':
            result += '0'
            numero = numero[:-1]
            break
    return numero + invertir(result)
def resta_oct(o1,o2):
    if type(o1)==int and type(o2)==int:
        if comprobar_octal(o1)==True and comprobar_octal(o2):
            o1=str(o1)
            o2=str(o2)
            if len(o1)==len(o2):
                return resta_oct_aux(o1,o2)
            elif len(o1)<len(o2):
                return resta_oct_aux(completar_ceros(o1,o2),o2)
            else:
                return resta_oct_aux(o1,completar_ceros(o2,o1))
        else:
            return 'Syntax error'
    else:
        return 'Syntax error'


def resta_oct_aux(o1,o2):
    r=''
    while o1 !='':
        if conv_oct_dec(int(o1))>=conv_oct_dec(int(o2)):
            if int(o1[-1])>=int(o2[-1]):
                r+=str(int(o1[-1])-int(o2[-1]))
                o1=o1[:-1]
                o2=o2[:-1]
            else:
                r+=str(int(o1[-1])+8-int(o2[-1]))
                p=o1[:-1]
                t=str(int(p[-1])-1)
                x=o1[:-2]+t
                o1=x
                o2=o2[:-1]
    return invertir(r)

def resta_hex(h1,h2):
    if type(h1)==str and type(h2)==str:
        if comprobar_hex(h1)==True and comprobar_hex(h2)==True:
            h1=conv_hex_bin(h1)
            h2=conv_hex_bin(h2)
            return conv_bin_hex(int(resta_bin(h1,h2)))
        else:
            return 'Syntax error'
    else:
        return 'Syntax error'

def mult_bin(b1,b2):
    if type(b1)==int and type(b2)==int:
        if comprobar_binario(b1)==True and comprobar_binario(b2)==True:
            b1=str(b1)
            b2=str(b2)
            return str(conv_dec_bin(conv_bin_dec(int(b1))*conv_bin_dec(int(b2))))
        else:
            return 'Syntax error'
    else:
        return 'Syntax error'
    
def mult_oct(o1,o2):
    if type(o1)==int and type(o2)==int:
        if comprobar_octal(o1)==True and comprobar_octal(o2)==True:
            
            return str(conv_dec_oct(conv_oct_dec(o1)*conv_oct_dec(o2)))
        else:
            return 'Syntax error'
    else:
        return 'Syntax error'

def mult_hex(h1,h2):
    if type(h1)==str and type(h2):
        if comprobar_hex(h1)==True and comprobar_hex(h2):
            return conv_dec_hex(conv_hex_dec(h1)*conv_hex_dec(h2))
        else:
            return 'Syntax error'
    else:
        return 'Syntax error'

def click(key):
    global memory
    if key=="dec-bin":
        result = int(entry.get())
        result=conv_dec_bin(result)
        entry.delete(0, tk.END)
        entry.insert(tk.END,str(result)+"                                                                                                                                                                                              ")
    if key=="dec-oct":
        result = int(entry.get())
        result=conv_dec_oct(result)
        entry.delete(0, tk.END)
        entry.insert(tk.END,str(result)+"                                                                                                                                                                                              ")
    if key=="bin-dec":
        result = int(entry.get())
        result=conv_bin_dec(result)
        entry.delete(0, tk.END)
        entry.insert(tk.END,str(result)+"                                                                                                                                                                                            ")
    if key=="oct-dec":
        result = int(entry.get())
        result=conv_oct_dec(result)
        entry.delete(0, tk.END)
        entry.insert(tk.END,str(result)+"                                                                                                                                                                                              ")
    if key=="dec-hex":
        result = int(entry.get())
        result=conv_dec_hex(result)
        entry.delete(0, tk.END)
        entry.insert(tk.END,str(result)+"                                                                                                                                                                                              ")
    if key=="hex-dec":
        result = str(entry.get())
        result=conv_hex_dec(result)
        entry.delete(0, tk.END)
        entry.insert(tk.END,str(result)+"                                                                                                                                                                                              ")
    if key=="bin-oct":
        result = int(entry.get())
        result=conv_bin_oct(result)
        entry.delete(0, tk.END)
        entry.insert(tk.END,str(result)+"                                                                                                                                                                                              ")
    if key=="bin-hex":
        result = int(entry.get())
        result=conv_bin_hex(result)
        entry.delete(0, tk.END)
        entry.insert(tk.END,str(result)+"                                                                                                                                                                                              ")
    if key=="oct-bin":
        result = int(entry.get())
        result=conv_oct_bin(result)
        entry.delete(0, tk.END)
        entry.insert(tk.END,str(result)+"                                                                                                                                                                                              ")
    if key=="oct-hex":
        result = int(entry.get())
        result=conv_oct_hex(result)
        entry.delete(0, tk.END)
        entry.insert(tk.END,str(result)+"                                                                                                                                                                                              ")
    if key=="oct-dec":
        result = int(entry.get())
        result=conv_oct_dec(result)
        entry.delete(0, tk.END)
        entry.insert(tk.END,str(result)+"                                                                                                                                                                                              ")
    if key=="hex-bin":
        result = str(entry.get())
        result=conv_hex_bin(result)
        entry.delete(0, tk.END)
        entry.insert(tk.END,str(result)+"                                                                                                                                                                                              ")
    if key=="hex-oct":
        result = str(entry.get())
        result=conv_hex_oct(result)
        entry.delete(0, tk.END)
        entry.insert(tk.END,str(result)+"                                                                                                                                                                                              ")
    if key=="+b":
        result = str(entry.get())
        result=result.split("+")
        res1=int(result[0])
        res2=int(result[1])
        result=suma_bin(res1,res2)
        entry.delete(0, tk.END)
        entry.insert(tk.END,str(result)+"                                                                                                                                                                                              ")
    if key=="+o":
        result = str(entry.get())
        result=result.split("+")
        res1=int(result[0])
        res2=int(result[1])
        result=suma_oct(res1,res2)
        entry.delete(0, tk.END)
        entry.insert(tk.END,str(result)+"                                                                                                                                                                                              ")
    if key=="+h":
        result = str(entry.get())
        result=result.split("+")
        res1=str(result[0])
        res2=str(result[1])
        result=suma_hex(res1,res2)
        entry.delete(0, tk.END)
        entry.insert(tk.END,str(result)+"                                                                                                                                                                                             ")
    if key=="-b":
        result = str(entry.get())
        result=result.split("-")
        res1=int(result[0])
        res2=int(result[1])
        result=resta_bin(res1,res2)
        entry.delete(0, tk.END)
        entry.insert(tk.END,str(result)+"                                                                                                                                                                                              ")
    if key=="-o":
        result = str(entry.get())
        result=result.split("-")
        res1=int(result[0])
        res2=int(result[1])
        result=resta_oct(res1,res2)
        entry.delete(0, tk.END)
        entry.insert(tk.END,str(result)+"                                                                                                                                                                                              ")
    if key=="-h":
        result = str(entry.get())
        result=result.split("-")
        res1=str(result[0])
        res2=str(result[1])
        if res1==res2:
            result="0"
        else:
            result=resta_hex(res1,res2)
        entry.delete(0, tk.END)
        entry.insert(tk.END,str(result)+"                                                                                                                                                                                              ")

    if key=="xb":
        result = str(entry.get())
        result=result.split("*")
        res1=int(result[0])
        res2=int(result[1])
        result=mult_bin(res1,res2)
        entry.delete(0, tk.END)
        entry.insert(tk.END,str(result)+"                                                                                                                                                                                              ")

    if key=="xo":
        result = str(entry.get())
        result=result.split("*")
        res1=int(result[0])
        res2=int(result[1])
        result=mult_oct(res1,res2)
        entry.delete(0, tk.END)
        entry.insert(tk.END,str(result)+"                                                                                                                                                                                              ")
    if key=="xh":
        result = str(entry.get())
        result=result.split("*")
        res1=str(result[0])
        res2=str(result[1])
        result=mult_hex(res1,res2)
        entry.delete(0, tk.END)
        entry.insert(tk.END,str(result)+"                                                                                                                                                                                              ")
    if key == '=':
        # division entre 0
        if '/' in entry.get() and '.' not in entry.get():
            entry.insert(tk.END, ".0")
        str1 = "Error"
        if entry.get()[0] not in str1:
            entry.insert(tk.END, "Sintax " + str1)
        # Calculos
        try:
            result = eval(entry.get())
            entry.insert(tk.END, " = " + str(result))
        except:
            entry.insert(tk.END, "Sorry")
    elif key == 'Cl':
        entry.delete(0, tk.END)  # Borra
    elif key == '->M':
        memory = entry.get()
        if '=' in memory:
            ix = memory.find('=')
            memory = memory[ix+2:]
        root.title('M=' + memory)
    else:
        if '=' in entry.get():
            entry.delete(0, tk.END)
        entry.insert(tk.END, key)
root = tk.Tk()
root.title("The marvelous calculator")
root.geometry("590x440")
root.config(bg="light blue")


cmd9 = lambda x='9': click(x)
but9= Button(text='9',command=cmd9,width=5,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
but9.place(x=200,y=30)
cmd8 = lambda x='8': click(x)
but8= Button(text='8',command=cmd8,width=5,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
but8.place(x=250,y=30)
cmd7 = lambda x='7': click(x)
but7= Button(text='7',command=cmd7,width=5,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
but7.place(x=300,y=30)
cmd6 = lambda x='6': click(x)
but6= Button(text='6',command=cmd6,width=5,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
but6.place(x=200,y=80)
cmd5 = lambda x='5': click(x)
but5= Button(text='5',command=cmd5,width=5,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
but5.place(x=250,y=80)
cmd4 = lambda x='4': click(x)
but4= Button(text='4',command=cmd4,width=5,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
but4.place(x=300,y=80)
cmd3 = lambda x='3': click(x)
but3= Button(text='3',command=cmd3,width=5,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
but3.place(x=200,y=130)
cmd2 = lambda x='2': click(x)
but2= Button(text='2',command=cmd2,width=5,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
but2.place(x=250,y=130)
cmd1 = lambda x='1': click(x)
but1= Button(text='1',command=cmd1,width=5,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
but1.place(x=300,y=130)
cmd0 = lambda x='0': click(x)
but0= Button(text='0',command=cmd0,width=5,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
but0.place(x=200,y=180)
cmdpoint = lambda x='.': click(x)
butpoint= Button(text='.',command=cmdpoint,width=5,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
butpoint.place(x=300,y=180)
cmdmas = lambda x='+': click(x)
butmas= Button(text='+',command=cmdmas,width=6,height=5, bg='yellow', activebackground='red', cursor='X_cursor')
butmas.place(x=100,y=35)
cmdmenos = lambda x='-': click(x)
butmenos= Button(text='-',command=cmdmenos,width=6,height=5, bg='yellow', activebackground='red', cursor='X_cursor')
butmenos.place(x=100,y=135)
cmdpor = lambda x='*': click(x)
butpor= Button(text='*',command=cmdpor,width=6,height=5, bg='yellow', activebackground='red', cursor='X_cursor')
butpor.place(x=40,y=35)
cmdentre = lambda x='/': click(x)
butentre= Button(text='/',command=cmdentre,width=6,height=5, bg='yellow', activebackground='red', cursor='X_cursor')
butentre.place(x=40,y=135)
cmdigual = lambda x='=': click(x)
butigual= Button(text='=',command=cmdigual,width=15,height=3, bg='yellow', activebackground='red', cursor='X_cursor')
butigual.place(x=40,y=230)
cmdclear = lambda x='Cl': click(x)
butclear= Button(text='C',command=cmdclear,width=5,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
butclear.place(x=250,y=180)
cmddtb = lambda x='dec-bin': click(x)
butdtb= Button(text='Dec->Bin',command=cmddtb,width=7,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
butdtb.place(x=40,y=300)
cmddto = lambda x='dec-oct': click(x)
butdto= Button(text='Dec->Oct',command=cmddto,width=7,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
butdto.place(x=40,y=340)
cmddth = lambda x='dec-hex': click(x)
butdth= Button(text='Dec->Hex',command=cmddth,width=7,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
butdth.place(x=40,y=380)
cmdbtd = lambda x='bin-dec': click(x)
butbtd= Button(text='Bin->Dec',command=cmdbtd,width=7,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
butbtd.place(x=100,y=300)
cmdbto = lambda x='bin-oct': click(x)
butbto= Button(text='Bin->Oct',command=cmdbto,width=7,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
butbto.place(x=100,y=340)
cmdbth = lambda x='bin-hex': click(x)
butbth= Button(text='Bin->Hex',command=cmdbth,width=7,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
butbth.place(x=100,y=380)
cmdotb = lambda x='oct-bin': click(x)
butotb= Button(text='Oct->Bin',command=cmdotb,width=7,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
butotb.place(x=160,y=300)
cmdotd = lambda x='oct-dec': click(x)
butotd= Button(text='Oct->Dec',command=cmdotd,width=7,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
butotd.place(x=160,y=340)
cmdoth = lambda x='oct-hex': click(x)
butoth= Button(text='Oct->Hex',command=cmdoth,width=7,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
butoth.place(x=160,y=380)
cmdhtb = lambda x='hex-bin': click(x)
buthtb= Button(text='Hex->Bin',command=cmdhtb,width=7,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
buthtb.place(x=220,y=300)
cmdhto = lambda x='hex-oct': click(x)
buthto= Button(text='Hex->Oct',command=cmdhto,width=7,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
buthto.place(x=220,y=340)
cmdhtd = lambda x='hex-dec': click(x)
buthtd= Button(text='Hex->Dec',command=cmdhtd,width=7,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
buthtd.place(x=220,y=380)
cmdmasb = lambda x='+b': click(x)
butmasb= Button(text='Bin+',command=cmdmasb,width=6,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
butmasb.place(x=360,y=30)
cmdmenosb = lambda x='-b': click(x)
butmenosb= Button(text='Bin-',command=cmdmenosb,width=6,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
butmenosb.place(x=360,y=80)
cmdporb = lambda x='xb': click(x)
butporb= Button(text='Bin*',command=cmdporb,width=6,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
butporb.place(x=360,y=130)
cmdmaso = lambda x='+o': click(x)
butmaso= Button(text='Oct+',command=cmdmaso,width=6,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
butmaso.place(x=420,y=30)
cmdmenoso = lambda x='-o': click(x)
butmenoso= Button(text='Oct-',command=cmdmenoso,width=6,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
butmenoso.place(x=420,y=80)
cmdporo = lambda x='xo': click(x)
butporo= Button(text='Oct*',command=cmdporo,width=6,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
butporo.place(x=420,y=130)
cmdmash = lambda x='+h': click(x)
butmash= Button(text='Hex+',command=cmdmash,width=6,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
butmash.place(x=480,y=30)
cmdmenosh= lambda x='-h': click(x)
butmenosh= Button(text='Hex-',command=cmdmenosh,width=6,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
butmenosh.place(x=480,y=80)
cmdporh = lambda x='xh': click(x)
butporh= Button(text='Hex*',command=cmdporh,width=6,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
butporh.place(x=480,y=130)
cmda = lambda x='A': click(x)
buta= Button(text='A',command=cmda,width=6,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
buta.place(x=350,y=250)
cmdb = lambda x='B': click(x)
butb= Button(text='B',command=cmdb,width=6,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
butb.place(x=410,y=250)
cmdc = lambda x='C': click(x)
butc= Button(text='C',command=cmdc,width=6,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
butc.place(x=470,y=250)
cmdd = lambda x='D': click(x)
butd= Button(text='D',command=cmdd,width=6,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
butd.place(x=350,y=310)
cmde = lambda x='E': click(x)
bute= Button(text='E',command=cmde,width=6,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
bute.place(x=410,y=310)
cmdf = lambda x='F': click(x)
butf= Button(text='F',command=cmdf,width=6,height=2, bg='yellow', activebackground='red', cursor='X_cursor')
butf.place(x=470,y=310)

# use Entry widget for an editable display
entry = tk.Entry(root, width=330, fg='blue',bg="white")
entry.grid(row=0, column=9, columnspan=5)
root.mainloop()
