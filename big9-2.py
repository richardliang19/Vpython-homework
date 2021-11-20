
from vpython import *
from random import *

t = 0.0 ; t1 = 0.0  ; dt = 0.0001 
theta = 30.0 * pi / 180 
d = 3.0  
r = 0.50  
v0 = 2.0  
m = 0.01  
per_N = 100.0 


theta = 00.0 * pi / 180 
per_N = 5.0 

k = 9*10**9  
Q_charge = 10**(-5)  
q_charge = 10 **(-8) 
q_m = 10**(-3)       

scene = canvas(align = 'left' , center = vec ( 0.5*d , 0 , 0 ) , height=600, width=1000, range=3.5,
                auto_scale=False, background=vec(0.6,0.8,0.8) , fov = 0.004)              

e = []  

Q = sphere(pos = vec(0,0,0) ,  radius = 0.2 , color = color.yellow)

def Force_E(r, q):
    r1 = r - Q.pos
    return k*q*Q_charge*r1.norm()/(r1.mag*r1.mag)

sum_F = 0  

while True:
    rate(10000)
    t = t + dt       
    t1 = t1 + dt  
    sum_F = 0     

    if t1 > 1/ per_N:  
        t1 = 0  
        r_dom = random() 
        p_dom = random() 
        e.append( sphere(pos = vector((-d*cos(theta)+r*r_dom*cos(p_dom*2*pi)*sin(theta)),(d*sin(theta)+r*r_dom*cos(p_dom*2*pi)*cos(theta)),(r*r_dom*sin(p_dom*2*pi))) , radius = 0.05, v = vec(v0*cos(theta),-v0*sin(theta),0) , Fx = 0 ,make_trail=True ,visible = True))
        
    for N in e :  
        N.v = N.v + Force_E(N.pos, q_charge)/q_m *dt
        N.pos = N.pos+N.v*dt
        
        if mag(N.pos -  vec(0,0,0) ) > 4: 
            N.visible = False
            N = None