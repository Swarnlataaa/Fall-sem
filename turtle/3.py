from turtle import *
color=["red","cyan","green","yellow",]
bgcolor("black")
speed(0)
for x in range(200):
    pencolor(color[x%6])
    width(x/100+1)
    forward (x)
    left(59)
hideturtle()
done()
