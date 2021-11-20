from vpython import *  

G = 6.67*10**(-11) ; M = 6*10**24 ; m = 1000  
Re = 6.4*10**6 ; H = 5*Re ; t = 0 ; dt = 10
def Fg(x):                                 
    return -G*M*m/(x**2)
Fe = G*M*m/Re**2 

scene = canvas(align = 'left',title ='4_01_Gravity force',  width=800, height=300, center=vector(0,0,0), background=vector(0.6,0.8,0.8)) 
earth = sphere(pos=vector(0,0,0), radius=Re, texture=textures.earth) 
mater = sphere(pos=vector(H,0,0), radius=0.1*Re,color=color.red, make_trail=True) 
V0= (G*M/H)**0.5
materv=vector(0,0.8*V0,0)

pre_x = H
while True:  
    rate(1000)
    
    dist = ((mater.pos.x-earth.pos.x)**2+(mater.pos.y-earth.pos.y)**2+(mater.pos.z-earth.pos.z)**2)**0.5 
    radiavector = (mater.pos-earth.pos)/dist 
    Fg_vector = Fg(dist)*radiavector 
    
    pre_pre_x =pre_x
    pre_x = mater.pos.x

    materv += Fg_vector/m*dt  
    mater.pos = mater.pos + materv*dt  

    t = t+dt
    if pre_x > pre_pre_x and pre_x > mater.pos.x :
        print(t)  
        t = 0


