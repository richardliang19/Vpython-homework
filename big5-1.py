from vpython import *  

G = 6.67*10**(-11) ; M = 6*10**24 ; m = 1000  
Re = 6.4*10**6 ; H = 5*Re ; t = 0 ; dt = 2
def Fg(x):                                 
    return -G*M*m/(x**2)
Fe = G*M*m/Re**2 

scene = canvas(align = 'left',  width=2400, height=900, center=vector(0,0,0), background=vector(0.6,0.8,0.8)) 
earth = sphere(pos=vector(0,0,0), radius=Re, texture=textures.earth) 
mater = sphere(pos=vector(H,0,0), radius=0.1*Re,color=color.red, make_trail=True) 
V0= (G*M/H)**0.5
materv=vector(0,0.8*V0,0)
aT_arrow = arrow(pos=mater.pos,axis=vec(0,0,0),shaftwidth=0.6*mater.radius ,color = color.black)
aN_arrow = arrow(pos=mater.pos,axis=vec(0,0,0),shaftwidth=0.6*mater.radius ,color = color.blue) 
v_arrow = arrow(pos=mater.pos,axis=vec(0,0,0),shaftwidth=0.4*mater.radius ,color = color.red)
a_arrow = arrow(pos=mater.pos,axis=vec(0,0,0),shaftwidth=0.4*mater.radius ,color = color.white)

while True:  
    rate(500)
   
    dist = ((mater.pos.x-earth.pos.x)**2+(mater.pos.y-earth.pos.y)**2+(mater.pos.z-earth.pos.z)**2)**0.5 
    radiavector = (mater.pos-earth.pos)/dist 
    Fg_vector = Fg(dist)*radiavector 
    
    v_arrow.pos = mater.pos
    v_arrow.axis = materv*2500
    a_arrow.pos = mater.pos
    a_arrow.axis = Fg_vector/m*5000000

    aT_arrow.pos = mater.pos
    aT_arrow.axis = dot(Fg_vector/m,materv)*(norm(materv)/mag(materv))*5000000
    aN_arrow.pos = mater.pos
    aN_arrow.axis = (mag(cross(Fg_vector/m,materv))/mag(materv))*cross(norm(materv),vector(0,0,-1))*5000000

    materv += Fg_vector/m*dt   
    mater.pos = mater.pos + materv*dt  

    t = t+dt



