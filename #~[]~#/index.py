from turtle import*
import colorsys
tracer(50)
bgcolor('black')
pensize(1)
h=0.4
for i in range(1000):
    c= colorsys.hsv_to_rgb(h, 1, 1)
    color(c)
    h +=0.005
    goto(0,0)
    forward(i*2)
    circle(-10,50)
    left(22)
done()