from vpython import *

size = 0.1     
theta = 0.0    
R = 1.0        
omega = 2*pi   
t = 0.0        

scene = canvas(width=500, height=500, center=vector(0,0,0), background=vector(148.0/225,228.0/225,204.0/225))
ball = sphere(radius=size, color=color.blue, make_trail=True, interval = 1, retain = 900)

ball.pos = vector(R,0,0)    
t = 0.0       
dt = 0.001    
pre_theta = theta
back=False
period_t=0
N=20
plot_t=0
circlecount=0
while True:
    if circlecount>3:
        break
    rate(1/dt)
    pre_pre_theta = pre_theta
    pre_theta = theta
    theta += omega*dt    
    ball.pos = vector(R*cos(theta), R*sin(theta), 0)
    t += dt              

    if back:
        plot_t = t % (period_t/N) 
        if plot_t + dt >= period_t/N  and plot_t <  period_t/N: 
            cylinder(radius=size/50, color=color.black, pos=vector(0,0,0) , axis= ball.pos) 
    if pre_theta%(2*pi) > pre_pre_theta%(2*pi) and pre_theta%(2*pi) > theta%(2*pi):
        print ('period = ', t)
        circlecount+=1
        back=True
        period_t=t
        t = 0



    
    