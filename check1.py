'''
    a ball is moving along x-axis, a = 3, v = -2 initially , starting from original point
    it'll draw this motion x-t graph, v-t graph and a-t graph 
    also print when it turn and its velocity, position 
'''

from vpython import *

size = 0.1

scene = canvas(width=600, height=400, center=vector(2.5, 0, 0), background=vector(0, 0, 0))
#set screen and background

x = arrow(pos=vector(0, 0, 0), axis=vector(1, 0, 0), shaftwidth=0.02, color=color.green)
y = arrow(pos=vector(0, 0, 0), axis=vector(0, 1, 0), shaftwidth=0.02, color=color.red)
z = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, 1), shaftwidth=0.02, color=color.blue)
ball = sphere(radius=size, color=color.yellow, pos=vector(0, 0, 0), v=vector(-2.0, 0, 0), a=vector(3.0, 0, 0))

gd1 = graph(title="x-t plot", width=600, height=400, xtitle="t", ytitle="x")
f1 = gcurve(color=color.blue)
gd2 = graph(title="v-t plot", width=600, height=400, xtitle="t", ytitle="v")
f2 = gcurve(color=color.green)
gd3 = graph(title="a-t plot", width=600, height=400, xtitle="t", ytitle="a")
#set func graph

f3 = gcurve(color=color.red)
dt = 0.001
t = 0.0

while t <= 2:
    rate(2 * 1 / dt)
    t = t + dt
    ball.v = ball.v + ball.a * dt
    ball.pos = ball.pos + ball.v * dt

    f1.plot(pos=(t, ball.pos.x))  #draw graph
    f2.plot(pos=(t, ball.v.x))
    f3.plot(pos=(t, ball.a.x))

    if ball.v.x < 0 and ball.v.x + ball.a.x * dt > 0:
        print(t)
        print(ball.v.x)
        print(ball.a.x)

