import turtle as t
import colorsys
t.tracer(100)
t.bgcolor('black')
t.pensize(2)
h=0.4
t.up()
t.goto(0,100)
t.down()
for i in range(260):
    c= colorsys.hsv_to_rgb(h, 1, 1)
    h += 0.002
    t.color(c)
    t.up()
    t.fd(i*4)
    t.down()
    t.circle(i,-100)
    t.fd(i)
    t.circle(i,-100)
done()