from vpython import *

g = 9.8               
size =0.3          
height = 0           
m = 1.0                 
Fg = vector(0, -m*g, 0) 

scene = canvas(width=600, height=600,x=0, y=0, center = vector(0,0,0)) 
floor = box(length=25, height=0.05, width=10, color=color.green)  
ball1 = sphere(radius = size, color=color.yellow, make_trail= True, trail_type="points", interval=100) 	
ball2 = sphere(radius = size, color=color.red, make_trail= True, trail_type="points", interval=100) 	
ball1.pos = vector(-12, 0, 0)    
ball1.v = vector(5, 5, 0)           
ball2.pos = vector(-12, 0, 0)    
ball2.v = vector(5, 5, 0)           
k=0.2

dt = 0.001	
t = 0.0		

while t<5:    
    rate(1/dt)   
    t = t + dt    
    
    ball1.a = Fg/m            
    ball1.v = ball1.v + ball1.a*dt          
    ball1.pos = ball1.pos + ball1.v * dt    
    if ball1.pos.y <= size and ball1.v.y < 0:    
        ball1.v.y = - ball1.v.y  

    resist = -k* ball2.v
    ball2.a = Fg/m  + resist/m
    ball2.v = ball2.v + ball2.a*dt         
    ball2.pos = ball2.pos + ball2.v * dt    
    if ball2.v.x<0:
        ball2.v=(0,0,0)
    if ball2.pos.y <= size and ball2.v.y < 0:   
        ball2.v.y = - ball2.v.y   

print(t, ball1.v)
print(t, ball2.v)