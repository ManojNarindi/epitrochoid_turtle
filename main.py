import turtle
import math as m
import numpy as np

radius1 = 100
k = int(input())

manoj = turtle.Turtle()

def rotation0fcoordinates(x,y,deg):
    theta = (np.pi / 180)*deg
    Xnew = (x*m.cos(theta)) + ((y-(radius1+(radius1/k)))*m.sin(theta))
    Ynew = ((y-(radius1+(radius1/k)))*m.cos(theta)) - (x*m.sin(theta))
    return Xnew,Ynew

manoj.penup()
manoj.setpos(-radius1,0)
manoj.pendown()

for alpha in range((int(k*360))):
    theta = (np.pi / 180) * alpha
    x = (radius1/k)*m.sin(theta)
    y = (radius1/k)*m.cos(theta)
    print(alpha)
    manoj.setpos(rotation0fcoordinates(x,y,alpha/k+90))

turtle.done()