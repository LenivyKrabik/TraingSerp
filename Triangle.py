from tkinter import *
from random import *
import math
import time
tk = Tk()
side=900
canvas=Canvas(tk, width=side, height=side)
canvas.pack()
class Dot():
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def inside(self):
        self.a=math.sqrt((self.x-d1.x)**2+(self.y-d1.y)**2)
        self.b=math.sqrt((self.x-d2.x)**2+(self.y-d2.y)**2)
        self.c=math.sqrt((d2.x-d1.x)**2+(d2.y-d1.y)**2)

        self.p=((self.a+self.b+self.c)/2)

        self.S1=math.sqrt(self.p*(self.p-self.a)*(self.p-self.b)*(self.p-self.c))

        self.a=math.sqrt((self.x-d3.x)**2+(self.y-d3.y)**2)
        self.b=math.sqrt((self.x-d2.x)**2+(self.y-d2.y)**2)
        self.c=math.sqrt((d2.x-d3.x)**2+(d2.y-d3.y)**2)

        self.p=((self.a+self.b+self.c)/2)

        self.S2=math.sqrt(self.p*(self.p-self.a)*(self.p-self.b)*(self.p-self.c))

        self.a=math.sqrt((self.x-d1.x)**2+(self.y-d1.y)**2)
        self.b=math.sqrt((self.x-d3.x)**2+(self.y-d3.y)**2)
        self.c=math.sqrt((d3.x-d1.x)**2+(d3.y-d1.y)**2)

        self.p=((self.a+self.b+self.c)/2)

        self.S3=math.sqrt(self.p*(self.p-self.a)*(self.p-self.b)*(self.p-self.c))

        self.S=int(self.S1+self.S2+self.S3)

        if S+1>self.S and self.S>S-1:
            return True
        else:
            return False

#Генеруємо прийемний оку трикутник
while True:
    d1=Dot(randint(0,side),randint(0,side))
    #Генерємо точки за 200 від інших
    while True:
        x=randint(0,side)
        y=randint(0,side)
        if not(math.sqrt((d1.x-x)**2+(d1.y-y)**2)<200):
            break
    d2=Dot(x,y)
    while True:
        x=randint(0,side)
        y=randint(0,side)
        if not(math.sqrt((d1.x-x)**2+(d1.y-y)**2)<200) and not(math.sqrt((d2.x-x)**2+(d2.y-y)**2)<200):
            break
    d3=Dot(x,y)
    
    a=math.sqrt((d2.x-d1.x)**2+(d2.y-d1.y)**2) #Сторони
    b=math.sqrt((d3.x-d2.x)**2+(d3.y-d2.y)**2)
    c=math.sqrt((d3.x-d1.x)**2+(d3.y-d1.y)**2)
    
    p=((a+b+c)/2) #Півпериметр
    
    S=math.sqrt(p*(p-a)*(p-b)*(p-c)) #Площа
    
    ratio=(a+b+c)/S
    if ratio<0.01:
        break

canvas.create_line(d1.x,d1.y,d2.x,d2.y)
canvas.create_line(d2.x,d2.y,d3.x,d3.y)
canvas.create_line(d3.x,d3.y,d1.x,d1.y)

DotRaneX=[min(d1.x,d2.x,d3.x),max(d1.x,d2.x,d3.x)]
DotRaneY=[min(d1.y,d2.y,d3.y),max(d1.y,d2.y,d3.y)]

Dins=Dot(randint(DotRaneX[0],DotRaneX[1]),randint(DotRaneY[0],DotRaneY[1]))





while Dins.inside()==False:
    Dins=Dot(randint(DotRaneX[0],DotRaneX[1]),randint(DotRaneY[0],DotRaneY[1]))
    
canvas.create_rectangle(Dins.x,Dins.y,Dins.x,Dins.y,outline='#FF0000')
canvas.pack()
while True:
    todot = choice([d1,d2,d3])
    Dins = Dot(((Dins.x+todot.x)/2), ((Dins.y+todot.y)/2))
    canvas.create_rectangle(Dins.x,Dins.y,Dins.x,Dins.y)
    tk.update()
    time.sleep(0.01)
    
        

