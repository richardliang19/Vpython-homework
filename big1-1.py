'''
    a person starts moving 
    a = +5 when t = 0~2s
    a = -5 when t = 2~6s 
    and it'll print the turning point time, position and velocity
'''
from vpython import *

size = 0.1

scene = canvas(width=600, height=400, center=vector(2.5,0,0), background=vector(0,0,0))
#set screen and background


x = arrow(pos=vector(0,0,0), axis=vector(1,0,0), shaftwidth=0.02, color=color.green)
y = arrow(pos=vector(0,0,0), axis=vector(0,1,0), shaftwidth=0.02, color=color.red)
z = arrow(pos=vector(0,0,0), axis=vector(0,0,1), shaftwidth=0.02, color=color.blue)
ball = sphere(radius=size, color=color.yellow, pos=vector(0,0,0), v=vector(0,0,0),a=vector(0,0,0))

gd1 = graph(title = "x-t plot", width=600, height=400, xtitle="t", ytitle="x")
f1 = gcurve(color=color.blue)
gd2 = graph(title = "v-t plot", width=600, height=400, xtitle="t", ytitle="v")
f2 = gcurve(color=color.green)
gd3 = graph(title = "a-t plot", width=600, height=400, xtitle="t", ytitle="a")
f3 = gcurve(color=color.red)
#set func graph and its color

dt = 0.001
t = 0.0
while t<=6:
    #start change its position by variance a,v
    if t<=2:
        ball.a.x=5.0
        rate(2*1/dt)
        ball.v = ball.v + ball.a*dt
        ball.pos = ball.pos + ball.v*dt 
    
        f1.plot(pos=(t,ball.pos.x))	#draw graph x-axis: t y-axis:position
        f2.plot(pos=(t,ball.v.x))   #draw graph x-axis: t y-axis:velocity
        f3.plot(pos=(t,ball.a.x))   #draw graph x-axis: t y-axis:acceleration
    else:
        ball.a.x=-5.0
        rate(2*1/dt)
        ball.v = ball.v + ball.a*dt
        ball.pos = ball.pos + ball.v*dt 
    
        f1.plot(pos=(t,ball.pos.x)) 
        f2.plot(pos=(t,ball.v.x))
        f3.plot(pos=(t,ball.a.x))

        if ball.v.x > 0 and ball.v.x + ball.a.x*dt < 0:
            print ("time at turning point:",t)
            print ("turning point:",ball.pos.x)
            print ("velocity at turning point",ball.v.x)
    t=t+dt