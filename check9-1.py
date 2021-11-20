from vpython import *  

G=2000 
M=1.0     
m=1.0    
dt = 0.001          
t = 0
R = 10     

scene = canvas(width=1000, height=600, background=vec(0.6,0.8,0.8),range = 0.9*R)
scene.center = vec(0,0,0)					
ball = sphere(pos=vector(0,0,0), radius = 0.5, color=color.green, v = vec(0,0,0), make_trail = True)

balllist = []  

for N in range(-3,4,1):
    for M in range(-3,4,1):
        for K in range(-3,4,1):
            balllist.append(sphere(pos=vector(N*0.1*R,M*0.1*R,K*0.1*R), radius = 0.1, color=color.red))

while True:
    rate (1000)

    t = t+dt
    ball.pos = ball.pos