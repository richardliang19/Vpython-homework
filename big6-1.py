from vpython import *  

G = 6.67 ; m1 = 5 ; m2 = 5 ; m3 = 5 ; R = 10 ;  t = 0 ; dt = 0.001

def Fg(x,M,m): 
    return -G*M*m/(x**2)
 
scene = canvas(width=1200, height=800, center=vec(0,0,0),background=vec(0.6,0.8,0.8),range=2*R)

ball_m1 = sphere(pos=vector(0,0,0), radius=0.5, color = color.blue, make_trail=True)
ball_m2 = sphere(pos=vector(R,0,0), radius=0.5, color = color.red, make_trail=True)
ball_m3 = sphere(pos=vector(R/2,((3)**0.5)*R/2,0), radius=0.5, color = color.yellow, make_trail=True)

V0 = (G*m1/R)**0.5
ball_m1_v = vector(V0/2,-((3)**0.5)*V0/2,0)
ball_m2_v = vector(V0/2,((3)**0.5)*V0/2,0)
ball_m3_v = vector(-V0,0,0)

F1_arrow = arrow(pos=ball_m1.pos,axis=vec(0,0,0),shaftwidth=0.1 ,color = color.black)
F13_arrow = arrow(pos=ball_m1.pos,axis=vec(0,0,0),shaftwidth=0.1 ,color = color.blue)
F12_arrow = arrow(pos=ball_m1.pos,axis=vec(0,0,0),shaftwidth=0.1 ,color = color.red)
v1_arrow = arrow(pos=ball_m1.pos,axis=vec(0,0,0),shaftwidth=0.1 ,color = color.yellow)

while True:
    rate(2000)
    
    dist_12 = mag(ball_m1.pos-ball_m2.pos) 
    radiavector_12 = (ball_m1.pos-ball_m2.pos)/dist_12
    Fg_vector_12 = Fg(dist_12,m1,m2)*radiavector_12 

    dist_13 = mag(ball_m1.pos-ball_m3.pos)  
    radiavector_13 = (ball_m1.pos-ball_m3.pos)/dist_13
    Fg_vector_13 = Fg(dist_13,m1,m3)*radiavector_13 

    dist_23 = mag(ball_m3.pos-ball_m2.pos) 
    radiavector_23 = (ball_m2.pos-ball_m3.pos)/dist_23
    Fg_vector_23 = Fg(dist_23,m3,m2)*radiavector_23 

    ball_m1_v += (Fg_vector_12+Fg_vector_13)/m1*dt  
    ball_m1.pos = ball_m1.pos + ball_m1_v*dt 

    ball_m2_v += (-Fg_vector_12+Fg_vector_23)/m2*dt
    ball_m2.pos = ball_m2.pos + ball_m2_v*dt 
    
    ball_m3_v += (-Fg_vector_13-Fg_vector_23)/m3*dt 
    ball_m3.pos = ball_m3.pos + ball_m3_v*dt 

    F1_arrow.pos = ball_m1.pos
    F1_arrow.axis = (Fg_vector_13+Fg_vector_12)

    F13_arrow.pos = ball_m1.pos
    F13_arrow.axis = (Fg_vector_13)

    F12_arrow.pos = ball_m1.pos
    F12_arrow.axis = (Fg_vector_12)

    v1_arrow.pos = ball_m1.pos
    v1_arrow.axis = ball_m1_v

    t = t+dt