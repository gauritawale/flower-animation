from turtle import *
import colorsys
import turtle

# Set up the screen
a = turtle.Screen()
a.title("Flower Animation")
a.bgcolor("white")
a.setup(width=600, height=600)

# Set up the turtle
speed(0)  
tracer(100)  
bgcolor('black')
h = 0  

# Drawing the flower
for i in range(16):
    for j in range(18):
        c = colorsys.hsv_to_rgb(h, 1, 1)  
        color(c) 
        h += 0.005 
        rt(90)
        circle(150 - j * 6, 90)  
        lt(90)
        circle(150 - j * 6, 90) 
        rt(180) 
    circle(40, 24) 
    update()  

update() 
done()
