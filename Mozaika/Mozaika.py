# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 08:01:31 2021

@author: komputer-PC
"""


#%%Definitions
import turtle as tu
from itertools import cycle
from math import dist

size= 400

def fillWith_color(color):
    def decorator(procedure):
        def newProc(*args,**kwargs):
            oldColor= Tu.fillcolor()
            Tu.fillcolor(color)
            Tu.begin_fill(); Tu.begin_poly()
            
            procedure(*args, **kwargs)
            
            Tu.end_poly(); Tu.end_fill()
            Tu.fillcolor(oldColor)
        return newProc
    return decorator

def withPD(procedure):
    def newProc(*args,**kwargs):
        Tu.pd()
        procedure(*args, **kwargs)
        Tu.pu()
    return newProc
    
@withPD
def rect(x, y=None):
    if y is None: y=x
    for _ in range(2):
        Tu.fd(x); Tu.left(90)
        Tu.fd(y); Tu.left(90)

@fillWith_color("green")
def greenSq(x): rect(x)

@fillWith_color("yellow")
def yellowSq(x): rect(x)

def count_Side(n, size=size):    
    vLength= 0
    vSide= 1
    for _ in range(n-1):
        vLength+= vSide/2
        vSide*=2
    vSide/=2
    
    vLength+= vSide/2+ 0.5
    vLength*=2
    
    return size/vLength


Marks= []
def steps(side, n, FunctionsI=  cycle((rect,))):
    savedCords= Tu.pos()
    while n:
        func= next(FunctionsI)
        func(side)
        Tu.fd(side/2); Tu.left(90)
        Tu.fd(side/2); Tu.right(90)
        side*=2;
        
        n-=1;
        
    Marks.append(Tu.pos())
    Tu.goto(savedCords)

def mozaika(n):
    #Drawing steps
    for _ in range(4):
        Functions= cycle((greenSq, yellowSq,))
        steps(count_Side(n),n-1, Functions)
        Tu.fd(size); Tu.left(90)
    #Drawing the top
    Tu.goto(Marks[0]);  d= dist(Marks[0],Marks[1])
    next(Functions)(d)
    Marks.clear()
        
        
#Debug constants
drawings= 2,2
Ns= (2,5,8,11)
assert drawings[0]*drawings[1]==len(Ns)



#%%Main objects
Sc= tu.Screen()
Sc.setworldcoordinates(0, 0, size*drawings[0], size*drawings[1])

#Turtle
##Effective
Tu= tu.RawPen(Sc);
Tu.pu()
##Debug-effective
Tu.speed(1)
##Graphical
Tu.shape("classic"); Tu.resizemode("auto")
Tu.pencolor("black")



#%%Action
I= iter(Ns)
for y in range(drawings[1]):
    for x in range(drawings[0]):
        Tu.setposition(x*size, y*size)
        mozaika(next(I))
Tu.hideturtle()

#%%Ending
Sc.exitonclick()