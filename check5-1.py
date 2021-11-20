from vpython import *  

G = 6.67*10**(-11) ; M = 6*10**24 ; m = 1000  
Re = 6.4*10**6 ; H = 5*Re ; t = 0 ; dt = 1
def Fg(x):                                
    return -G*M*m/(x**2)


gd = graph(align='left',width=400,height=400,  
              title='K+U=E', xtitle='t', ytitle='E(red),K(black),U(green)',
              foreground=color.black,background=color.white)
f1 = gcurve(color=color.red) 
f2 = gcurve(color=color.black)  
f3 = gcurve(color=color.green)  
Fe = G*M*m/Re**2 

scene = canvas(align = 'left',title ='4_01_Gravity force',  width=800, height=300, center=vec(0,0,0), background=vec(0.6,0.8,0.8)) 
earth = sphere(pos=vec(0,0,0), radius=Re, texture=textures.earth)
mater = sphere(pos=vec(H,0,0), radius=0.1*Re,color=color.red, make_trail=True) 
V0= (G*M/H)**0.5
materv=vector(0,0.7*V0,0)

while True: 
    rate(10000)
    dist = ((mater.pos.x-earth.pos.x)**2+(mater.pos.y-earth.pos.y)**2+(mater.pos.z-earth.pos.z)**2)**0.5
    radiavector = (mater.pos-earth.pos)/dist 
    Fg_vector = Fg(dist)*radiavector 
    
    materv += Fg_vector/m*dt  
    mater.pos = mater.pos + materv*dt  
  
    t = t+dt
    K=0.5*m*(mag(materv))**2
    U=-G*M*m/dist
    f2.plot(pos=(t,K))  
    f3.plot(pos=(t,U))
    f1.plot(pos=(t,K+U))
