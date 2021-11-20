from vpython import *

A = 1           
N = 50            
omega = 3*pi/1.0   
size = 0.1         
m = 0.1            
k = 500.0          
d = 0.4            
g = 9.8
b = 0.1
scene = canvas(title='Spring Wave', width=300, height=800, range = 0.4*50/6, center = vector(0, -(N-1)*d/2, 0)) 
ball = [sphere(radius=size, color=color.yellow, pos=vector(0, -i*d, 0), v=vector(0,0,0)) for i in range(N)]

spring = [helix(radius = size/2.0, thickness = d/15.0, pos=vector(0, -i*d, 0), axis=vector(d,0,0)) for i in range(N-1)]



def SpringForce(r):  
    return - k*(mag(r)-d)*r/mag(r)
      
t, dt = 0, 0.001       
while True:
    rate(1000)
    t += dt

    ball[0].pos = vector(A*sin(omega*t), 0, A*cos(omega*t))    

    for i in range(N-1):
        spring[i].pos = ball[i].pos
        spring[i].axis = ball[i+1].pos - ball[i].pos

    for i in range(1, N):      
        if i == N-1: ball[-1].v += (SpringForce(spring[-1].axis)+vector(0,-m*g,0)-b * ball[i].v)/m*dt                        
        else : ball[i].v += (-SpringForce(spring[i].axis) + SpringForce(spring[i-1].axis)+vector(0,-m*g,0)-b * ball[i].v)/m*dt  

        ball[i].pos += ball[i].v*dt