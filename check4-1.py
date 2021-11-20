from vpython import *  

m1 = 2.0                   
x1 = -20.0                  
v1= 6.0                    
size1 = 1.0                 

m2 = 1.0                 
x2 = -5.0                   
v2= 3.0                    
size2 = 1.0                

Force = 5.0               
spring_L = 5.0             
spring_k = 2.0 

scene = canvas(width=1000, height=300, background=vec(0.6,0.8,0.8), center=vec(5,0,10),forward=vec(0,0,-1),range=10, fov=0.004)
ball1 = sphere(radius=size1, color = color.red, make_trail = False)
ball1.pos = vector(x1,0,0)             
ball1.v = vector (v1,0,0)                    
v1_arrow = arrow(pos=ball1.pos,axis=ball1.v,shaftwidth=0.2*size1 ,color = color.red)

ball2 = sphere(radius=size2, color = color.blue,make_trail = False) 
ball2.pos = vector(x2,0,0)             
ball2.v = vector (v2,0,0)                      
v2_arrow = arrow(pos=ball2.pos,axis=ball2.v,shaftwidth=0.2*size2 ,color = color.blue)

spring = helix(pos=ball2.pos, radius=0.5, thickness =0.1) 
spring.coils = 10
spring.axis = vector(-spring_L,0,0)

t = 0                                            
dt = 0.001                                       
	
gd1 = graph(title = "K-purple, U-green, E-black", width=600, height=400, xtitle="t", ytitle="E")
f1 = gcurve(color=color.purple)
f2 = gcurve(color=color.green)
f3 = gcurve(color=color.black)
	
gd2 = graph(title = "P1 red, P2-blue, P-black", width=600, height=400, xtitle="t", ytitle="energy")
f4 = gcurve(color=color.red)
f5 = gcurve(color=color.blue)
f6 = gcurve(color=color.black)

while True :
    rate(1000)
    ball1.pos = ball1.pos+ball1.v*dt  
    ball2.pos = ball2.pos+ball2.v*dt  

    v1_arrow.pos = ball1.pos 
    v1_arrow.axis = ball1.v  

    v2_arrow.pos = ball1.pos 
    v2_arrow.axis = ball1.v  

    spring.pos=ball2.pos  
    ball1.pos = ball1.pos
    ball2.pos = ball2.pos
    L=0
    if mag(ball2.pos - ball1.pos) < spring_L :  
        ball1_a = -1 * spring_k * (spring_L - ( ball2.pos.x - ball1.pos.x )) / m1
        ball2_a = 1 * spring_k * (spring_L - ( ball2.pos.x - ball1.pos.x )) / m2  
        L=spring_L - ( ball2.pos.x - ball1.pos.x )
    else :                            
        ball1_a = 0
        ball2_a = 0
        spring.axis = vector(-spring_L,0,0)

    ball1.v = ball1.v + vector(ball1_a,0,0) *dt  
    ball2.v = ball2.v + vector(ball2_a,0,0) *dt
    t=t+dt
    K=0.5*m1*(ball1.v.x)**2+0.5*m2*(ball2.v.x)**2
    U=0.5*spring_k*(L)**2
    P1=m1*ball1.v.x
    P2=m2*ball2.v.x
    f1.plot(pos=(t,K))
    f2.plot(pos=(t,U))
    f3.plot(pos=(t,K+U))
    f4.plot(pos=(t,P1))
    f5.plot(pos=(t,P2))
    f6.plot(pos=(t,P1+P2))