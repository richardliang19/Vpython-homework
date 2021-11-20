'''
    compare projectile motion with air resistance or not
    and draw another trail by laws derived from some mathematical calculating
    you'll find two trails match perfectly
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
ball1 = sphere(radius = size, color=color.yellow, make_trail= True, trail_type="points", interval=10) 	
ball2 = sphere(radius = size, color=color.red, make_trail= True, trail_type="points", interval=10) 
ball1.pos = vector(-12, 0, 0)   
ball1.v = vector(10, 10, 0)          
ball2.pos = vector(-12, 0, 0)    
ball2.v = vector(10, 10, 0)           
k=1
tmpt=0
dt = 0.001	
t = 0.0		
cool=[0,0]
while True:   
    rate(1/dt)    
    t = t + dt    
    if ball1.pos.y <= size and ball1.v.y < 0:    
        ball1.a =vector(0,0,0)
        ball1.v=vector(0,0,0)
        cool[0]=1
    else:
        ball1.a = Fg/m            
        ball1.v = ball1.v + ball1.a*dt          
        ball1.pos = ball1.pos + ball1.v * dt    

    
    if ball2.pos.y <= size and ball2.v.y < 0:    
        ball2.a =vector(0,0,0)
        ball2.v=vector(0,0,0)
        cool[1]=1
    else: 
        resist = -k* ball2.v
        ball2.a = Fg/m  + resist/m
        ball2.v = ball2.v + ball2.a*dt          
        ball2.pos = ball2.pos + ball2.v * dt    

    if cool[0]==1 and cool[1]==1 and OAO==0:
        dt = 0.001	
        t = 0.0		
        ball3 = sphere(radius = size, color=color.green, make_trail= True, trail_type="points", interval=1) 	
        ball3.pos = vector(-12, 0, 0)    
        ball3.v = vector(10, 10, 0)           
        while True:
            rate(1/dt)
            t=t+dt
            ball3.pos.x = (ball3.v.x * (1 - exp(-k*t))/k) -12
            ball3.pos.y = (- g*t/k + (k*ball3.v.y + g) * (1 - exp(-k*t))/k**2) 
            ball3.pos.z = 0
            if ball3.pos.y <= size and t>1:
                OAO=1
                break
            
            


