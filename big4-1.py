from vpython import *  

m1 = 1
m2 = 5
m3 = 30
g=9.8                
size = 1              
height_1 = 20.0       
height_2 = 18.0       
dt = 0.001                              

scene = canvas(width=400, height=600, center = vec(0,height_1,0), background=vec(0.6,0.8,0.8)) 
floor = box(length=15, height=0.01, width=10, color=color.blue)                        
ball_1 = sphere(radius = 1, color=color.yellow ) 
ball_2 = sphere(radius = 2, color=color.green ) 
ball_3 = sphere(radius = 3, color=color.blue)

ball_1.pos = vector( 0, 20.0, 0)       
ball_1.v = vector( 0, 0, 0)                   
ball_2.pos = vector( 0, 17.0, 0)            
ball_2.v = vector( 0, 0, 0)                   
ball_3.pos = vector( 0, 12.0, 0)
ball_3.v = vector( 0, 0, 0)


pre_pos=vector(0,0,0)

while True:             
    rate(1000)                        
    pre_pre_pos=pre_pos
    pre_pos=vector(0,ball_1.pos.y,0)

    ball_1.pos += ball_1.v*dt
    ball_1.v.y += - g*dt

    if ball_1.pos.y <= 1 and ball_1.v.y < 0:     
        ball_1.v.y = - 1* ball_1.v.y

    ball_2.pos += ball_2.v*dt
    ball_2.v.y += - g*dt
    
    if ball_2.pos.y <= 2 and ball_2.v.y < 0:     
        ball_2.v.y = - 1* ball_2.v.y
    
    ball_3.pos += ball_3.v*dt
    ball_3.v.y += - g*dt
    
    if ball_3.pos.y <= 3 and ball_3.v.y < 0:     
        ball_3.v.y = - 1* ball_3.v.y

    if mag(ball_2.pos-ball_3.pos) <= 5  :
        v2y = ((m2-m3)/(m2+m3)*ball_2.v.y) +(2*m3/(m2+m3)*ball_3.v.y)
        v3y = (2*m2/(m2+m3)*ball_2.v.y) + ((m3-m2)/(m2+m3)*ball_3.v.y)      
        ball_2.v = vector (0 , v2y , 0)
        ball_3.v = vector (0 , v3y , 0) 

    if mag(ball_1.pos-ball_2.pos) <= 3  :
        v1y = ((m1-m2)/(m1+m2)*ball_1.v.y) +(2*m2/(m1+m2)*ball_2.v.y)
        v2y = (2*m1/(m1+m2)*ball_1.v.y) + ((m2-m1)/(m1+m2)*ball_2.v.y)      
        ball_1.v = vector (0 , v1y , 0)
        ball_2.v = vector (0 , v2y , 0)
    
    if ball_1.pos.y<pre_pos.y and pre_pos.y>pre_pre_pos.y:
        print(ball_1.pos.y)
    

    