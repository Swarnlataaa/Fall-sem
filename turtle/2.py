import turtle
turtle.bgcolor('black')
turtle.speed(0)


colors=["yellow","red","yellow","red",]
for i in range(120):
    for c in colors:
        turtle.color(c)
        turtle.circle(120-i,100)
        turtle.lt(90)
        turtle.circle(200-i,100)
        turtle.rt(60)
        turtle.end_fill()
turtle.mainloop()
