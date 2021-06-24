from tkinter import*
import numpy as np
import math
from sympy import *
from itertools import permutations,combinations
root=Tk()
root.title("Calculator")
root.minsize(660,542)
global d
d=""
e=Entry(root,fg="yellow",bg="black",width="100",borderwidth=6)
e.grid(row=0,column=0,columnspan=3,pady=10)
def perm():
    global first
    first=e.get()
    e.delete(0,END)
    global d
    d="perm"
def comb():
    global first
    first=e.get()
    e.delete(0,END)
    global d
    d="comb"
    
def click(number):
    s=e.get()
    e.delete(0,END)
    
    e.insert(0,str(s)+str(number))
def add():
    global first
    first=e.get()
    global d
    d="+"
    e.delete(0,END)
def minus():
    global first
    first=e.get()
    
        
    global d
    
    d="-"
    
    e.delete(0,END)
def multiply():
    global d
    global first
    first=e.get()
    d="*"
    e.delete(0,END)
def div():
    global d
    global first
    first=e.get()
    d="/"
    e.delete(0,END)
def intdiv():
    
    global d
    global first
    first=e.get()
    d="//"
    e.delete(0,END)
def mod():
    
    global d
    global first
    first=e.get()
    d="%"
    e.delete(0,END)
def sqrt():
    global first
    first=e.get()
    e.delete(0,END)
    e.insert(0,math.sqrt(int(first)))
def log2():
    global first
    first=e.get()
    e.delete(0,END)
    e.insert(0,math.log2(int(first)))
def log10():
    global first
    first=e.get()
    e.delete(0,END)
    e.insert(0,math.log10(int(first)))
def loge():
    global first
    first=e.get()
    e.delete(0,END)
    e.insert(0,math.log(int(first)))

        
    
        
def pow():
    
    global d
    global first
    first=e.get()
    d="^"
    e.delete(0,END)

def clear():
    e.delete(0,END)
def fact():
    global first
    global d
    d="!"
    first=e.get()
    e.delete(0,END)
def gcd():
    global first
    global d
    d="gcd"
    first=e.get()
    e.delete(0,END)
def gcd1(q,r):
    if(r==0):
        return q;
    else:
        return(gcd1(r,q%r))
def percent():
    global first
    global d
    first=e.get()
    d="per"
    e.delete(0,END)
def lcm():
    global first
    first=e.get()
    e.delete(0,END)
    global d
    d="lcm"
def divmod1():
    
    global first
    global d
    d="Divmod"
    first=e.get()
    e.delete(0,END)
def rev():
    
    global first
    global d
    d="rev"
    first=e.get()
    e.delete(0,END)
    r=int(first)
    p=0
    while(r>0):
        p=p*10+r%10
        r=r//10
    e.insert(0,str(p))

def degree():
    global first
 
    
    first=e.get()
    e.delete(0,END)
    l=[]
    l.clear()
    d1=int(first)
    while(d1>0):
        s=d1%10
        l.append(s)
        d1=d1//10
    p1=np.poly1d(l)
    
    e.insert(0,p1.order)
    

def  root1():
    global first
 
    
    first=e.get()
    e.delete(0,END)
    l=[]
    d1=int(first)
    while(d1>0):
        s=d1%10
        l.append(s)
        d1=d1//10
    l.reverse()
    p1=np.poly1d(l)
    
    e.insert(0,p1.r)

def sin():
    global first
    first=int(e.get())
    first=(math.pi/180)*first
    e.insert(0,math.sin(first))
def cos():
    global first
    first=int(e.get())
    first=(math.pi/180)*first
    e.insert(0,math.cos(first))
def tan():
    global first
    first=int(e.get())
    first=(math.pi/180)*first
    e.insert(0,math.tan(first))
 
def diff():
    global first
    first=e.get()
    e.delete(0,END)
    d=1
    g=0
    u=0
    while(d<=(int(first))):
          if (int(first)%d==0):
              g=1
              u=u+1
              
          d=d+1
            
    if(u==2):
        e.insert(0,"Prime")
    else:
        e.insert(0,"  Non prime ")
        e.insert(0,u)
    
          
    

def max1():
    global first
    first =e.get()
    e.delete(0,END)
    d1=int(first)
    l=list()
    while(d1>0):
        s=d1%10
        l.append(s)
        d1=d1//10
    e.insert(0,max(l))
def min1():
    
    global first
    first =e.get()
    e.delete(0,END)
    d1=int(first)
    l=list()
    while(d1>0):
        s=d1%10
        l.append(s)
        d1=d1//10
    e.insert(0,min(l))

def arm():
    g=int(e.get())
    e.delete(0,END)
    h=g
    l=0
    while(h>0):
        l=l+1
        h=h//10
    h=g
    p=0
    while(h>0):
        p=p+int(math.pow(h%10,l))
        h=h//10
    if(p==g):
        e.insert(0,str(p)+" is a Armstrong Number")
    else:
        e.insert(0,str(g)+" is Not Armstrong")
def equal():
    p=e.get()
    e.delete(0,END)
    if(d=="per"):
        e.insert(0,(int(first)/int(p))*100)
    if(d=="perm"):
        k=[l for l in range(int(first))]
        perm=permutations(k,int(p))
        f=0
        for a in perm:
            f=f+1
        e.insert(0,f)
    if(d=="comb"):
        k=[l for l in range(int(first))]
        perm=combinations(k,int(p))
        f=0
        for a in list(perm):
            f=f+1
        e.insert(0,f)
    
    if(d=="+"):
        e.insert(0,int(p)+int(first))
    if(d=="-"):
        e.insert(0,-int(p)+int(first))
    if(d=="*"):
        e.insert(0,int(p)*int(first))
    if(d=="/"):
        e.insert(0,int(first)/int(p))
    if(d=="//"):
        e.insert(0,int(first)//int(p))
    if(d=="%"):
        e.insert(0,int(first)%int(p))
    if(d=="^"):
        e.insert(0,int(first)**int(p))
    if(d=="!"):
       s=1
       for a in range(1,int(first)+1):
           s=s*a
       e.insert(0,s)
    if(d=="gcd"):
        q=int(first)
        r=int(p)
        p=gcd1(q,r)
        e.insert(0,p)
    if(d=="lcm"):
        g=math.gcd(int(first),int(p))
        e.insert(0,(int(first)*int(p))/g)
        
    if(d=="Divmod"):
        y,i=divmod(int(first),int(p))
        e.insert(0,"Quotient= "+str(y)+"   Remainder=  "+str(i))
def auto():
    global first
    first=int(e.get())
    y=first
    e.delete(0,END)
    l=0
    while(y>0):
        l=l+1
        y=y//10
    p=int(math.pow(first,2))
    f=int(math.pow(10,l))
    h=p%f
    if(h==first):
        e.insert(0,str(h)+"  is Automorphic")
        
    else:
        e.insert(0,str(first)+"is Not Automorphic")
def special():
    g=int(e.get())
    e.delete(0,END)
    h=g
    k=0
    while(h>0):
        p=h%10
        i=2
        t=1
        while(i<=p):
            t=t*i
            i=i+1
        k=k+t
        h=h//10
    if(g==k):
        e.insert(0,str(k)+" is special number")
    else:
         e.insert(0,str(g)+" is not special number")
def per():
    g=int(e.get())
    e.delete(0,END)
    h=g
    l=1
    s=0
    while(l<h):
        if(h%l==0):
            s=s+l
        l=l+1
    if(s==g):
        e.insert(0,str(s)+" is a perfect number")
    else:
        e.insert(0,str(g)+" is not a perfect number")

def uni():
    g=int(e.get())
    e.delete(0,END)
    h=g
    l=list()
    l1=0
    while(h>0):
        s=h%10
        l.append(s)
        h=h//10
    for a in range(10):
        j=0
        for b in l:
        
            if(a==b):
                j=j+1
        if(j>1):
            l1=1
            break
    
    if(l1==1):
        e.insert(0,str(g)+" is a not unique number")
    else:
        e.insert(0,str(g)+" is a unique number")
def niven():
    g=int(e.get())
    e.delete(0,END)
    h=g
    s=0
    while(h>0):
        s=s+h%10
        h=h//10
    if(g%s==0):
        e.insert(0,str(g)+" is a niven number")
    else:
        e.insert(0,str(g)+" is  not a niven number")
        
        
        
        
button1=Button(root,text="1",width="25",height="2",fg="red",bg="yellow",command=lambda:click(1),activebackground="blue")
button2=Button(root,text="2",width="25",height="2",fg="red",bg="yellow",command=lambda:click(2),activebackground="black")

button3=Button(root,text="3",width="25",height="2",fg="red",bg="yellow",command=lambda:click(3),activebackground="gold")

button4=Button(root,text="4",width="25",height="2",fg="red",bg="yellow",command=lambda:click(4),activebackground="purple")

button5=Button(root,text="5",width="25",height="2",fg="red",bg="yellow",command=lambda:click(5),activebackground="yellow")
button6=Button(root,text="6",width="25",height="2",fg="red",bg="yellow",command=lambda:click(6),activebackground="cyan")
button7=Button(root,text="7",width="25",height="2",fg="red",bg="yellow",command=lambda:click(7),activebackground="purple")
button8=Button(root,text="8",width="25",height="2",fg="red",bg="yellow",command=lambda:click(8),activebackground="white")
button9=Button(root,text="9",width="25",height="2",fg="red",bg="yellow",command=lambda:click(9),activebackground="navy blue")
button0=Button(root,text="0",width="25",height="2",fg="red",bg="yellow",command=lambda:click(0),activebackground="magenta")
buttonadd=Button(root,text="+",width="30",height="2",fg="black",bg="orange",command=add,activebackground="silver")
buttonminus=Button(root,text="-",width="30",height="2",fg="black",bg="orange",command=minus,activebackground="azure")
buttonmul=Button(root,text="*",width="30",height="2",fg="black",bg="orange",command=multiply,activebackground="green")
buttondiv=Button(root,text="/",width="30",height="2",fg="black",bg="orange",command=div,activebackground="lime")
buttonequal=Button(root,text="=",width="30",height="2",fg="black",bg="orange",command=equal,activebackground="olive")
buttonmod=Button(root,text="%",width="30",height="2",fg="black",bg="orange",command=mod,activebackground="plum")
buttonpow=Button(root,text="POW",width="30",height="2",fg="black",bg="orange",command=pow,activebackground="indigo")
buttonclear=Button(root,text="CLEAR",width="30",height="2",fg="black",bg="orange",command=clear,activebackground="maroon")
buttonintdiv=Button(root,text="//",width="30",height="2",fg="black",bg="orange",command=intdiv,activebackground="maroon")
buttonfact=Button(root,text="!",width="30",height="2",fg="black",bg="orange",command=fact,activebackground="red")
buttongcd=Button(root,text="gcd",width="30",height="2",fg="black",bg="orange",command=gcd,activebackground="crimson")
buttondivmod=Button(root,text="Divmod",width="30",height="2",fg="black",bg="orange",command=divmod1,activebackground="teal")
buttondivmod=Button(root,text="Divmod",width="30",height="2",fg="black",bg="orange",command=divmod1,activebackground="salmon")
buttonorder=Button(root,text="degree of polynomial",width="30",height="2",fg="black",bg="orange",command=degree,activebackground="hot pink")
buttonorder1=Button(root,text="root",width="30",height="2",fg="black",bg="orange",command=root1,activebackground="white")

buttonsin=Button(root,text="sin",width="30",height="2",fg="black",bg="orange",command=sin,activebackground="blue")

buttoncos=Button(root,text="cos",width="30",height="2",fg="black",bg="orange",command=cos,activebackground="yellow")

buttontan=Button(root,text="tan",width="30",height="2",fg="black",bg="orange",command=tan,activebackground="purple")
buttonmax=Button(root,text="max",width="30",height="2",fg="black",bg="orange",command=max1,activebackground="crimson")
buttonmin=Button(root,text="min",width="30",height="2",fg="black",bg="orange",command=min1,activebackground="pink")
buttonperm=Button(root,text="Perm",width="30",height="2",fg="black",bg="orange",command=perm,activebackground="black")
buttoncomb=Button(root,text="comb",width="30",height="2",fg="black",bg="orange",command=comb,activebackground="green")

buttonsqrt=Button(root,text="sqrt",width="30",height="2",fg="black",bg="orange",command=sqrt,activebackground="purple")
buttonlog2=Button(root,text="log2",width="30",height="2",fg="black",bg="orange",command=log2,activebackground="black")
buttonlog10=Button(root,text="log10",width="30",height="2",fg="black",bg="orange",command=log10,activebackground="silver")
buttonloge=Button(root,text="loge",width="30",height="2",fg="black",bg="orange",command=loge,activebackground="purple")
buttonpercent=Button(root,text="percent",width="30",height="2",fg="black",bg="orange",command=percent,activebackground="pink")
buttonlcm=Button(root,text="lcm",width="30",height="2",fg="black",bg="orange",command=lcm,activebackground="purple")
buttonrev=Button(root,text="reverse",width="30",height="2",fg="black",bg="orange",command=rev,activebackground="indigo")
buttonauto=Button(root,text="automorphic",width="30",height="2",fg="black",bg="orange",command=auto,activebackground="magenta")
buttonarm=Button(root,text="armstrong",width="30",height="2",fg="black",bg="orange",command=arm,activebackground="white")
buttonspe=Button(root,text="special",width="30",height="2",fg="black",bg="orange",command=special,activebackground="black")
buttonper=Button(root,text="perfect",width="30",height="2",fg="black",bg="orange",command=per,activebackground="purple")
buttonniven=Button(root,text="niven",width="30",height="2",fg="black",bg="orange",command=niven,activebackground="blue")
buttondiff=Button(root,text="prime or not",width="30",height="2",fg="black",bg="orange",command=diff,activebackground="green")
buttonuni=Button(root,text="unique",width="30",height="2",fg="black",bg="orange",command=uni,activebackground="pink")
buttonauto.grid(row=14,column=0)
buttonarm.grid(row=14,column=1)
buttonspe.grid(row=14,column=2)
buttonper.grid(row=15,column=0)
buttonuni.grid(row=15,column=1)
buttonniven.grid(row=15,column=2)
buttonrev.grid(row=13,column=1)
buttondiff.grid(row=13,column=2)
buttonlcm.grid(row=13,column=0)
buttonpercent.grid(row=12,column=2)
buttonlog2.grid(row=11,column=2)
buttonlog10.grid(row=11,column=1)
buttonloge.grid(row=12,column=0)

buttonperm.grid(row=10,column=2)
buttoncomb.grid(row=11,column=0)
buttonmax.grid(row=10,column=0)
buttonmin.grid(row=10,column=1)
buttonsin.grid(row=9,column=0)
buttonorder.grid(row=8,column=1)
buttonorder1.grid(row=8,column=2)
buttoncos.grid(row=9,column=1)
buttontan.grid(row=9,column=2)
buttondivmod.grid(row=8,column=0)
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button0.grid(row=4,column=0)
buttonadd.grid(row=5,column=0)
buttonminus.grid(row=5,column=1)
buttonmul.grid(row=5,column=2)
buttondiv.grid(row=6,column=0)
buttonmod.grid(row=6,column=1)
buttonpow.grid(row=6,column=2)
buttonequal.grid(row=4,column=1)
buttonclear.grid(row=4,column=2)
buttonintdiv.grid(row=7,column=0)
buttonfact.grid(row=7,column=1)
buttongcd.grid(row=7,column=2)
buttonsqrt.grid(row=12,column=1)
root.mainloop()
