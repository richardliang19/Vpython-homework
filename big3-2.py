from vpython import *
g = 9.8                 
size = 0.03                       
L = 0.25                 
k = 100000              
m = 0.1                 
theta = 30 * pi/180     
Fg = m*vector(0,-g,0)   

def SpringForce(r,L):
    return -k*(mag(r)-L)*r/mag(r)

scene = canvas(width=600, height=600, center=vector(0, -L*0.8, 0), range=1.2*L)
ceiling = box(length=0.6, height=0.005, width=0.6, opacity = 0.6)#畫天花板
ball1 = sphere(radius = size,  color=color.red, make_trail = True, retain = 1000, interval=1)
ball2 = sphere(radius = size,  color=color.green, make_trail = True, retain = 1000, interval=1)
rod1 = cylinder(radius=size/10)
rod2 = cylinder(radius=size/10)
	
gd1 = graph(title = "E-t plot", width=600, height=400, xtitle="t", ytitle="energy")
f1 = gcurve(color=color.green)
f2 = gcurve(color=color.red)
f3 = gcurve(color=color.blue)


ball1.pos = vector(L, 0, 0)  
ball2.pos = vector(2*L, 0, 0)                         
rod1.pos = vector(0, 0, 0)   
rod2.pos = vector(L, 0, 0)                       
ball2.v=vector(0,0,0)
ball1.v=vector(0,0,0)
dt = 0.001    
t = 0.0       

while True:
    rate(1/dt)
    rod2.pos = ball1.pos                 
    rod1.axis = ball1.pos               
    rod2.axis = ball2.pos - ball1.pos  

    F1 = vector(0, -m*g, 0) + SpringForce(rod1.axis,L) - SpringForce(rod2.axis,L) 
    F2 = vector(0, -m*g, 0) + SpringForce(rod2.axis,L) 

    ball1.v += F1/m*dt
    ball1.pos += ball1.v*dt
    ball2.v += F2/m*dt
    ball2.pos += ball2.v*dt
    e1=0.5*m*mag(ball1.v)*mag(ball1.v)+m * g *(ball1.pos.y)
    e2=0.5*m*mag(ball2.v)*mag(ball2.v)+m * g *(ball2.pos.y)
    f1.plot(pos=(t,e1))
    f2.plot(pos=(t,e2))
    f3.plot(pos=(t,e1+e2))
    t=t+dt

    

    