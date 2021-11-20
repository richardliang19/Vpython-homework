from vpython import *

A = 0.4            
N = 50            
omega = 2*pi/1.0   
size = 0.1         
m = 0.1            
k = 500.0         
d = 0.4            
     
scene = canvas(title='Spring Wave', width=1200, height=300, range = 0.4*50/6, center = vector((N-1)*d/2, 0, 0)) 
ball = [sphere(radius=size, color=color.yellow, pos=vector(i*d, 0, 0), v=vector(0,0,0)) for i in range(N)]

spring = [helix(radius = size/2.0, thickness = d/15.0, pos=vector(i*d, 0, 0), axis=vector(d,0,0)) for i in range(N-1)]



def SpringForce(r):    
    return - k*(mag(r)-d)*r/mag(r)
      
t, dt = 0, 0.001       
while True:
    rate(1000)
    t += dt

    ball[0].pos = vector(0, A*sin(omega*t), 0)    
  
    for i in range(N-1):
        spring[i].pos = ball[i].pos
        spring[i].axis = ball[i+1].pos - ball[i].pos

    for i in range(1, N):      
        if i != N-1:                         
            ball[i].v += (-SpringForce(spring[i].axis) + SpringForce(spring[i-1].axis))/m*dt  

        ball[i].pos += ball[i].v*dt