'''
    demonstrate projectile motion when degree from 0~2pi
    also draw the relations between horizontal distance and degree, also time and degree
'''

from vpython import *

g = 9.8                 
size =0.3            
height = 0           
m = 1                
Fg = vector(0, -m*g, 0) 
OAO=0
scene = canvas(width=600, height=600,x=0, y=0, center = vector(0,0,0)) 
floor = box(length=25, height=0.05, width=10, color=color.green)  	
ball = sphere(radius = size, color=color.yellow, make_trail= True, trail_type="points", interval=10) 	
show_angle = label(pos=vector(0,-7*size,0), box = False, height = 20, color=color.yellow)

ball.a=Fg/m
theta= 3*pi/180
v0=10
ball.v = vector(v0*cos(theta), v0*sin(theta), 0)
ball.pos=vector(0,size,0)
gd1 = graph(title = "theta-R plot", width=600, height=400, xtitle="theta", ytitle="R")
f1 = gcurve(color=color.red)
gd2 = graph(title = "theta-T plot", width=600, height=400, xtitle="theta", ytitle="T")
f2 = gcurve(color=color.blue)
t=0.0
dt=0.001
while True:
    rate(10/dt)
    
    t=t+dt
    ball.v = ball.v + ball.a*dt
    ball.pos = ball.pos + ball.v*dt
    if ball.pos.y <= size:
        print("T=",t,",R=",ball.pos.x,",theta=",theta*180/pi)
        f1.plot(pos=(theta*180/pi,ball.pos.x))
        f2.plot(pos=(theta*180/pi,t))
        t=0
        theta = theta + 3 * pi/180     
        if theta>pi:
            break
        ball.pos = vector(0, size, 0)  
        ball.v = vector(v0*cos(theta), v0*sin(theta), 0)  
    show_angle.text = 'theta = %1.0f deg' %(theta/pi*180)
        
            


