from vpython import *  

m1 = 2.0                   
x1 = -20.0                 
v1= 6.0                    
size1 = 1.0                

m2 = 2.0                  
x2 = -5.0                   
v2= 0.000000000001                    
size2 = 1.0                 

Force = 5.0               
spring_L = 5.0            
spring_k = 10.0 

scene = canvas(width=1000, height=300, background=vec(0.6,0.8,0.8), center=vec(5,0,10),forward=vec(0,0,-1),range=10, fov=0.004)
ball1 = sphere(radius=size1, color = color.red, make_trail = True)  
ball1.pos = vector(-20,2,0)             
ball1.v = vector (v1,0,0)                        
v1_arrow = arrow(pos=ball1.pos,axis=ball1.v,shaftwidth=0.2*size1 ,color = color.red)

ball2 = sphere(radius=size2, color = color.blue,make_trail = True) 
ball2.pos = vector(x2,0,0)            
ball2.v = vector (v2,0,0)                        
v2_arrow = arrow(pos=ball2.pos,axis=ball2.v,shaftwidth=0.2*size2 ,color = color.blue)

t = 0                                            
dt = 0.001                                      

while True :
    rate(1000)
    ball1.pos = ball1.pos+ball1.v*dt  
    ball2.pos = ball2.pos+ball2.v*dt  

    v1_arrow.pos = ball1.pos 
    v1_arrow.axis = ball1.v  

    v2_arrow.pos = ball1.pos 
    v2_arrow.axis = ball1.v  

    ball1.pos = ball1.pos
    ball2.pos = ball2.pos
    L=0
    if mag(ball2.pos - ball1.pos) < spring_L :  
        ball1_a = -1 * norm(ball2.pos-ball1.pos) * spring_k * (spring_L - mag( ball2.pos - ball1.pos )) / m1
        ball2_a = 1 * norm(ball2.pos-ball1.pos) * spring_k * (spring_L - mag( ball2.pos - ball1.pos )) / m2
        L=spring_L - ( ball2.pos.x - ball1.pos.x )
        
    else :                            
        ball1_a = vector(0,0,0)
        ball2_a = vector(0,0,0)

    ball1.v = ball1.v + ball1_a *dt 
    ball2.v = ball2.v + ball2_a *dt
    t=t+dt
    if t>4.0 and t< 4.1:
        cos_theta = dot(ball1.v,ball2.v)/(ball1.v.mag*ball2.v.mag)
        theta = acos(cos_theta)*360/(2*pi)
        print (theta)

