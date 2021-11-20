from vpython import*
import numpy as np
N = 100		
g = 9.8		
size, m, k, d = 0.016, 0.1/N, N*1000.0, 2.0/N   
t, dt = 0, 0.0001                                
T = 0
scene = canvas(width=1200, height = 600, center = vector(d*N/2.0*0.9, 0, 0)) 

c = curve([vector(d*i*0.9, d*i*0.2, 0) for i in range(N)], radius = 0.01) 

leftarrow = arrow(pos=vector(0,0,0),axis=vector(0,0,0),shaftwidth=0.01 ,color = color.blue)
rightarrow = arrow(pos=vector(d*99*0.9,d*99*0.2,0),axis=vector(0,0,0),shaftwidth=0.01 ,color = color.green)
mgarrow = arrow(pos=vector(0,0,0),axis=vector(0,0,0),shaftwidth=0.01 ,color = color.red)
cylinder1 = cylinder(pos=vector(0,0,0),axis=vector(0,0,0),radius = 0.005,color = color.yellow)
cylinder2 = cylinder(pos=vector(0,0,0),axis=vector(0,0,0),radius = 0.005,color = color.yellow)

mg = []

ball_pos, ball_v, ball_g = np.zeros((N, 3)), np.zeros((N,3)), np.zeros((N,3))

for i in range(N):
    ball_pos[i][0] = d*i*0.9 
    ball_pos[i][1] = d*i*0.1
    ball_g[i][1] = -g      

while True:
    rate(1/dt)
    t += dt       
    spring_axis = ball_pos[1:] - ball_pos[:-1]        
    b = np.sum(spring_axis**2, axis = 1)**0.5         
    spring_axis_unit = spring_axis / b[:, np.newaxis] 
    fs = - k * (spring_axis - d*spring_axis_unit)     
    fs[b<=d] = 0                                      
    
    ball_v[1:-1] += (fs[:-1] - fs[1:])/m*dt + ball_g[1:-1]*dt - 5.0*ball_v[1:-1]*dt    

    ball_pos += ball_v *dt                           
    T = t % (50*dt)                  
    if T + dt >50*dt and T < 50*dt:  
        for i in range(N):      
            c.modify(i, pos=vector(ball_pos[i][0],ball_pos[i][1],ball_pos[i][2]))
    leftarrow.pos = vector(ball_pos[0][0],ball_pos[0][1],ball_pos[0][2])
    leftarrow.axis = vector(ball_pos[0][0]-ball_pos[1][0],ball_pos[0][1]-ball_pos[1][1],ball_pos[0][2]-ball_pos[1][2])*8
    rightarrow.pos = vector(ball_pos[-1][0],ball_pos[-1][1],ball_pos[-1][2])
    rightarrow.axis = vector(ball_pos[-1][0]-ball_pos[-2][0],ball_pos[-1][1]-ball_pos[-2][1],ball_pos[-1][2]-ball_pos[-2][2])*8
    mg= np.sum(ball_pos,axis=0)/100
    mgarrow.pos = vector(mg[0],mg[1],0)
    mgarrow.axis = vector(0,-g,0)/15

    cylinder1.pos = leftarrow.pos
    cylinder1.axis = -leftarrow.axis*8
    cylinder2.pos = rightarrow.pos
    cylinder2.axis = -rightarrow.axis*8

    