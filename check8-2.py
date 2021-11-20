from vpython import*
import numpy as np
N = 40		
g = 9.8		
size, m, k, d = 0.016, 0.1/N, N*1000.0, 2.0/N   
t, dt = 0, 0.0001                                
b_air = 0.1
scene = canvas(width=1200, height = 600, center = vector(d*N/2.0*0.9, 0, 0)) 

c = curve([vector(d*i*0.9, 0, 0) for i in range(N)], radius = 0.01) 

ball_pos, ball_v, ball_g = np.zeros((N, 3)), np.zeros((N,3)), np.zeros((N,3))

for i in range(N):
    ball_pos[i][0] = d*i*0.9 
    ball_g[i][1] = -g        

while True:
    rate(5/dt)
    t += dt        
    spring_axis = ball_pos[1:] - ball_pos[:-1]        
    b = np.sum(spring_axis**2, axis = 1)**0.5         
    spring_axis_unit = spring_axis / b[:, np.newaxis] 
    fs = - k * (spring_axis - d*spring_axis_unit)     
    fs[b<=d] = 0                                      
    
    ball_v[1:-1] += (fs[:-1] - fs[1:])/m*dt + ball_g[1:-1]*dt - 5.0*ball_v[1:-1]*dt - b_air*ball_v[1:-1]/m*dt
    ball_v[-1] += fs[-1]/m*dt + ball_g[-1]*dt - 5.0*ball_v[-1]*dt - b_air*ball_v[-1]/m*dt

    ball_pos += ball_v *dt                            
    T = t % (100*dt)                 
    if T + dt >100*dt and T < 100*dt:  
        for i in range(N):        
            c.modify(i, pos=vector(ball_pos[i][0],ball_pos[i][1],ball_pos[i][2]))
    
    