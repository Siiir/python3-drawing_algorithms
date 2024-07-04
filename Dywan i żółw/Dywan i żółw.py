# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 13:27:35 2021

@author: Tomasz Nehring
"""


#%%Imports & definitions
import turtle

size= 400

#Functions
class how(object):
    @staticmethod
    def color(drawingProcedure, color):
        def newProc(*args, **kwargs):
            Turtle.fillcolor(color); Turtle.begin_fill()
            drawingProcedure(*args, **kwargs)
            Turtle.end_fill()
        return newProc
    @staticmethod
    def withPenUp(procedure):
        def newProc(*args, **kwargs):
            Turtle.penup()
            procedure(*args, **kwargs)
            Turtle.pendown()  
        return newProc

class draw(object):
    @staticmethod
    def rect(x,y=None):
        if y is None: y=x
        for _ in range(2):
            Turtle.fd(x); Turtle.left(90)
            Turtle.fd(y); Turtle.left(90)
    @classmethod
    def redRect(cls, *args, **kwargs):
        how.color(cls.rect,"red")(*args, **kwargs)

    
    @classmethod
    def arrow(cls, size):
        Turtle.pencolor("black")
        
        Turtle.fillcolor("white")
        Turtle.begin_fill(); cls.rect(size); Turtle.end_fill();
        
        Turtle.fillcolor("green")
        Turtle.begin_fill(); Turtle.begin_poly()
        
        Turtle.left(90); Turtle.fd(size)
        Turtle.right(90); Turtle.fd(size)
        small= size/4 *2**0.5
        Turtle.right(135); Turtle.fd(small)
        Turtle.left(90);    Turtle.fd(small)
        Turtle.right(90);   Turtle.fd(2*small)
        Turtle.right(90);   Turtle.fd(small)
        Turtle.left(90);    Turtle.fd(small)
        
        Turtle.end_poly(); Turtle.end_fill()
        
        Turtle.left(135)

    @classmethod
    def smallPack(cls,y):
        cls.redRect(y/2, y)
        Turtle.fd(y/2)
        cls.arrow(y)
        Turtle.bk(y/2)

    @classmethod
    def bigPack(cls,size):
        smallY= 0.4*size
        for _ in range(4):
            cls.smallPack(smallY)
            how.withPenUp(Turtle.fd)(size)
            Turtle.left(90)
            
        start= Turtle.pos()
        Turtle.pu();
        Turtle.fd(smallY); Turtle.left(90)
        Turtle.fd(smallY); Turtle.right(90)
        Turtle.pd();
        cls.redRect(0.2*size)
        how.withPenUp(Turtle.setpos)(*start)
        
    @classmethod
    def blanket(cls,size=size):
        packSize= size/2
        for _ in range(4):
            cls.bigPack(packSize)
            how.withPenUp(Turtle.fd)(size); Turtle.left(90)

def dywan():  draw.blanket(size)


#%%Main objects
#Screen
Screen= turtle.Screen();
Screen.title("Dywan i żółw");  Screen.bgcolor("white")
Screen.setworldcoordinates(0, 0, size, size)

#Turtle
Turtle= turtle.RawTurtle(Screen, visible=True)
Turtle.speed(0.1)
Turtle.shape("turtle"); Turtle.resizemode("user")


#%%Action
dywan()
Turtle.color("#0F0"); Turtle.shapesize(8,8); Turtle.pu()
Turtle.setposition(size/2,size/2)
from random import randint
while True:
    Turtle.left(15)
    Turtle.right(randint(1,20))


#%%End
Screen.exitonclick()
