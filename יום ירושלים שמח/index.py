from turtle import *
import colorsys
bgcolor("black")
tracer(40)
h = 0
text= ['שמח', 'יום ירושלים']
for i in range(90):
    color(colorsys.hsv_to_rgb(h, 1,1))
    h += 0.06
    up()
    fd(i*5)
    down()
    write(text[i%2],font=('Arial', int((i+4)/4),
    'bold'))
    lt(48)
done()