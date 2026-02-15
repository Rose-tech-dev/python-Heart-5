import math
from turtle import *

def heartx(t):
    return 16 * math.sin(t)**3

def hearty(t):
    return (13 * math.cos(t)
            - 5 * math.cos(2*t)
            - 2 * math.cos(3*t)
            - math.cos(4*t))

speed(0)
bgcolor("black")
color("deep pink")
pensize(2)

for i in range(1000):
    t = i * 0.02
    goto(heartx(t) * 15, hearty(t) * 15)

hideturtle()
done()