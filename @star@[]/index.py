from turtle import *
bgcolor("black")
tracer(5)
import colorsys
h = 0.4
for i in range(300):
    color(colorsys.hsv_to_rgb(h, 1,1))
    h += 0.005
    for j in range(2):
        fd(i)
        lt(60)
        rt(20)
    rt(240)
    lt(51)
    circle(10)
done()