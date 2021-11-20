'''
    https://www.youtube.com/watch?v=uiyMuHuCFo4
'''
from vpython import*
import numpy as np
N = 50		
g = 9.8		
size = 0.016
thick = size/5.0
m, k, d =  0.1/N, N*0.5, thick    
t, dt = 0, 0.0001                               
ball_cm = 0
damp = 5.0
scene = canvas(width=300, height = 600, center = vector(0, -2, 0))
mybox = box(pos=vector(0,0,0), length=1.5, height=0.08, width=1.5)

cball = sphere(radius = 4*size/2.0,pos= vector(0,0,0), color = color.green)
lastball = sphere(radius = 8*size/2.0,pos= vector(0,0,0), color = color.red)
springs = [helix(radius = 8*size/2.0, thickness = thick, d= thick, coils = 1) for i in range(N-1)]

ball_pos, ball_v, ball_g = np.zeros((N, 3)), np.zeros((N,3)), np.zeros((N,3))

for i in range(N):
    ball_pos[i][1] = -d*i*0.9 
    ball_g[i][1] = -g        

vtgraph =  graph(title = "v-t graph", width=600, height=400, xtitle="t", ytitle="v")
f1 = gcurve(color=color.green)
f2 = gcurve(color=color.red)

while True:
    rate(1/dt/3)
    t += dt         
    spring_axis = ball_pos[1:] - ball_pos[:-1]        
    b = np.sum(spring_axis**2, axis = 1)**0.5         
    spring_axis_unit = spring_axis / b[:, np.newaxis] 
    fs = - k * (spring_axis - d*spring_axis_unit)    
   
    ball_v[1:-1] += (fs[:-1] - fs[1:])/m*dt + ball_g[1:-1]*dt - damp*ball_v[1:-1]*dt    
    ball_v[-1] +=(fs[-1])/m*dt + ball_g[-1]*dt - damp*ball_v[-1]*dt
    ball_pos+= ball_v*dt                            
    T = t % (50*dt)                 

    if t > 5: 
        damp = 0
        ball_v[0] += (-fs[0])/m*dt + ball_g[0]*dt   	
        
        
    for j in arange(N-1): 
        if (ball_pos[j][1] - ball_pos[j+1][1]) <= d:  
            ball_v[j] = ball_v[j+1] = (ball_v[j] + ball_v[j+1])/2  
            ball_pos[j+1][1] = ball_pos[j][1] - d                  

    if T + dt >50*dt and T < 50*dt: 
        for i in range(N-1):      
            springs[i].pos = vector(ball_pos[i][0], ball_pos[i][1], ball_pos[i][2])
            springs[i].axis = vector(ball_pos[i+1][0], ball_pos[i+1][1], ball_pos[i+1][2]) -vector(ball_pos[i][0], ball_pos[i][1], ball_pos[i][2])
    
    ball_cm = np.sum(ball_pos, axis = 0)/N  
    ball_cv = np.sum(ball_v, axis = 0)/N
    cball.pos = vector(ball_cm[0],ball_cm[1],ball_cm[2])
    lastball.pos = vector(ball_pos[-1][0], ball_pos[-1][1], ball_pos[-1][2])
    
    if t>5:
        f1.plot(pos=(t,ball_cv[1]))
        f2.plot(pos=(t,ball_v[-1][1]))
