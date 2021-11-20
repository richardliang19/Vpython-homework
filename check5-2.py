from vpython import *  

G = 6.67*10**(-11) ; M = 6*10**24 ; m = 1000  
Re = 6.4*10**6 ; H = 5*Re ; t = 0 ; dt = 1
def Fg(x):                                
    return -G*M*m/(x**2)

Fe = G*M*m/Re**2 

scene = canvas(align = 'left',title ='4_01_Gravity force',  width=800, height=300, center=vec(0,0,0), background=vec(0.6,0.8,0.8)) 
earth = sphere(pos=vec(0,0,0), radius=Re, texture=textures.earth)
mater1 = sphere(pos=vec(H,0,0), radius=0.1*Re,color=color.blue, make_trail=True) 
mater2 = sphere(pos=vec(H,0,0), radius=0.1*Re,color=color.red, make_trail=True) 
mater3 = sphere(pos=vec(H,0,0), radius=0.1*Re,color=color.yellow, make_trail=True) 
V0= (G*M/H)**0.5
mater1v=vector(0,0.7*V0,0)
mater2v=vector(0,V0,0)
mater3v=vector(0,1.2*V0,0)

while True: 
    rate(10000)
    dist = ((mater1.pos.x-earth.pos.x)**2+(mater1.pos.y-earth.pos.y)**2+(mater1.pos.z-earth.pos.z)**2)**0.5 
    radiavector1 = (mater1.pos-earth.pos)/dist 
    Fg_vector1 = Fg(dist)*radiavector1 
    
    mater1v += Fg_vector1/m*dt   
    mater1.pos = mater1.pos + mater1v*dt  
    
    dist = ((mater2.pos.x-earth.pos.x)**2+(mater2.pos.y-earth.pos.y)**2+(mater2.pos.z-earth.pos.z)**2)**0.5 
    radiavector2 = (mater2.pos-earth.pos)/dist 
    Fg_vector2 = Fg(dist)*radiavector2 
    
    mater2v += Fg_vector2/m*dt  
    mater2.pos = mater2.pos + mater2v*dt  

    dist = ((mater3.pos.x-earth.pos.x)**2+(mater3.pos.y-earth.pos.y)**2+(mater3.pos.z-earth.pos.z)**2)**0.5
    radiavector3 = (mater3.pos-earth.pos)/dist 
    Fg_vector3 = Fg(dist)*radiavector3 
    
    mater3v += Fg_vector3/m*dt  
    mater3.pos = mater3.pos + mater3v*dt  

    t = t+dt
 
