from vpython import *  

g=9.8    ;   size = 0.5  ; m1 =2 ; m2 =4 ; t = 0 ; dt = 0.001
v0 = 20   ;   theta_0 = 60*pi/180   ;   s0 = vector( -25.0, size, 0.0)
J_vector = norm(vector(1,0,0)) 
J_mag = 20 
scene = canvas(title='拋體運動', width=1000, height=600, center=vec(0,10,0),background=vec(0.6,0.8,0.8))
floor = box(length=60, height=0.01, width=4, texture=textures.wood)                  
ball1 = sphere(radius = size,  color=color.red, make_trail = True)          
ball2 = sphere(radius = size,  color=color.green, make_trail = True)          
ball3 = sphere(radius = 0.01*size,  color=color.black, make_trail = True)          
ball1.pos = s0    ;  ball1.v = vector(v0*cos(theta_0), v0*sin(theta_0) , 0.0)      
ball2.pos = s0    ;  ball2.v = vector(v0*cos(theta_0), v0*sin(theta_0) , 0.0)    
ball3.pos = s0    ;  ball3.v = vector(0, 0 , 0)      

start = 0
def keyinput(evt):       
    global start     
    key_s = {'a' :1.0}
    s = evt.key    
    if s in key_s : start = start + key_s[s]
    if start > 0:
        ball1.pos += ball1.v*dt
        ball1.v += vector(0,- g*dt,0)
        ball2.pos += ball2.v*dt
        ball2.v += vector(0,- g*dt,0)
        if start > 1.9 and start <2.1:   
            ball1.v += J_vector*J_mag/m1      
            ball2.v += - J_vector*J_mag/m2    
            start = start + 1                
scene.bind('keydown', keyinput)                    
while ball3.pos.y>=0:       
    rate(500)                   
    t = t + dt

    ball3.pos = (m1*ball1.pos+m2*ball2.pos)/(m1+m2)  

    if t >= 0:
        ball1.pos += ball1.v*dt
        ball1.v += vector(0,- g*dt,0)
        ball2.pos += ball2.v*dt
        ball2.v += vector(0,- g*dt,0)
        if ball1.v.y < 0  and start < 1:  
            ball1.v += J_vector*J_mag/m1    
            ball2.v += - J_vector*J_mag/m2     
            start = start + 1                