from vpython import *

A = 2               
N = 200             
omega = 2*pi*4     
size = 0.1          
m1 = 0.2           
m2 = 0.5            
k = 4000.0          
d = 0.1             
t, dt = 0, 0.0005   
T = 50*dt           
     
scene = canvas(title='Spring Wave', width=1200, height=300, range = 0.4*50/6, center = vector((N-1)*d/2, 0, 0)) 
ball = [sphere(radius=size, color=color.yellow, pos=vector(i*d, 0, 0), v=vector(0,0,0)) for i in range(N)]

for i in range(N):
    if i >= int(N/2): ball[i].color = color.blue

ball_pos = [vector(i*d,0,0) for i in range(N)]
ball_v = [vector(0,0,0) for i in range(N)]
spring_pos = [vector(i*d,0,0) for i in range(N-1)]
spring_axis = [vector(d,0,0) for i in range(N-1)]

def SpringForce(r):    
    return - k*(mag(r))*r/mag(r)
      
while True:
    rate(1/dt)
    t += dt

    if t <= 2*pi/omega/2: ball_pos[0] = vector(0, A*sin(omega*t), 0)    

    for i in range(N-1):
        spring_pos[i] = ball_pos[i]
        spring_axis[i] = ball_pos[i+1] - ball_pos[i]

    for i in range(1, int(N/2)):        
        ball_v[i] += (-SpringForce(spring_axis[i]) + SpringForce(spring_axis[i-1]))/m1*dt
    for i in range(int(N/2), N-1):      
        ball_v[i] += ( -SpringForce(spring_axis[i]) + SpringForce(spring_axis[i-1]))/m2*dt
    for i in range(1, N):               
        ball_pos[i] += ball_v[i]*dt

    if t%T < T and t%T+dt > T:          
        for i in range(N):
            ball[i].pos = ball_pos[i]