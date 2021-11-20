from vpython import * 

G = 6.67 ; m1 = 100; m2 = 10; m3 = 1; R_12 = 10; R_23 = 1; t = 0 ; dt = 0.001
v2 = (G*m1/R_12)**0.5
v3 = (G*m2/R_23)**0.5  

def Fg(x,y1,y2): 
    return -G*y1*y2/(x**2)

scene = canvas(width=1200, height=800, center=vec(0,0,0),background=vec(0.6,0.8,0.8),range=2*R_12)

ball_m1 = sphere(pos=vector(0,0,0), radius=1, color = color.yellow, make_trail=True)
ball_m2 = sphere(pos=vector(R_12,0,0), radius=0.3, color = color.blue, make_trail=True)
ball_m3 = sphere(pos=vector(R_12+R_23,0,0), radius=0.1, color = color.red, make_trail=True)

ball_m1_v = vector(0,0,0) ; ball_m2_v = vector(0,v2,0) ; ball_m3_v = vector(0,v2+v3,0)

Fearth_arrow = arrow(pos=ball_m3.pos,axis=vec(0,0,0),shaftwidth=0.6*ball_m3.radius ,color = color.blue)
Fsun_arrow = arrow(pos=ball_m3.pos,axis=vec(0,0,0),shaftwidth=0.6*ball_m3.radius ,color = color.yellow) 
Ftotal_arrow = arrow(pos=ball_m3.pos,axis=vec(0,0,0),shaftwidth=0.4*ball_m3.radius ,color = color.black)

while True:
    rate(1000)
    
    dist_12 = mag(ball_m1.pos-ball_m2.pos) 
    radiavector_12 = (ball_m2.pos-ball_m1.pos)/dist_12
    Fg_12_vector = Fg(dist_12,m1,m2)*radiavector_12
    
    dist_23 = mag(ball_m2.pos - ball_m3.pos) 
    radiavector_23 = (ball_m3.pos-ball_m2.pos)/dist_23
    Fg_23_vector = Fg(dist_23,m2,m3)*radiavector_23
    
    dist_13 = mag(ball_m3.pos -ball_m1.pos) 
    radiavector_13 = (ball_m3.pos -ball_m1.pos)/dist_13
    Fg_13_vector = Fg(dist_13,m1,m3)*radiavector_13

    ball_m2_v += Fg_12_vector/m2*dt
    ball_m2.pos = ball_m2.pos + ball_m2_v*dt

    ball_m3_v += (Fg_23_vector + Fg_13_vector)/m3*dt
    ball_m3.pos = ball_m3.pos + ball_m3_v*dt

    Fearth_arrow.pos= ball_m3.pos
    Fsun_arrow.pos= ball_m3.pos
    Ftotal_arrow.pos= ball_m3.pos

    Fearth_arrow.axis= Fg_23_vector/5
    Fsun_arrow.axis= Fg_13_vector/5
    Ftotal_arrow.axis= Fg_13_vector + Fg_23_vector/5

    t = t+dt

