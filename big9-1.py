from vpython import *  

k = 9*10**9 ;  size = 0.1  ;  b_N = 36

t = 0 ; dt = 0.001

Q1_charge = 10**(-5)
Q2_charge = -(10)**(-5)

q_charge = 1 * 10 **(-7)  
q_position = vector (1 , 1 , 0) 
q_m = 10**(-3)                  
q_v = vector (0.0 , 2.0 , 0.0)  

scene = canvas(title='dipole', height=600, width=1200, range=3.5,
                auto_scale=False, background=vec(0.3,0.4,0.4), fov=0.004)


q = sphere(pos = q_position , radius = 0.5*size , color = color.green , v = q_v, make_trail=True)

Qx1 = sphere(pos = vec(2,0,0) , radius = size , color = color.blue)
Qx2 = sphere(pos = vec(-2,0,0) , radius = size , color = color.blue)
Qy1 = sphere(pos = vec(0,2,0), radius = size , color = color.red)
Qy2 = sphere(pos = vec(0,-2,0), radius = size , color = color.red)

def Force_E(r, q):
    rx1 = r - Qx1.pos
    rx2 = r - Qx2.pos
    ry1 = r - Qy1.pos
    ry2 = r - Qy2.pos
    return k*q*Q1_charge*rx1.norm()/(rx1.mag*rx1.mag)+  k*q*Q1_charge*rx2.norm()/(rx2.mag*rx2.mag) + k*q*Q2_charge*ry1.norm()/(ry1.mag*ry1.mag)+  k*q*Q2_charge*ry2.norm()/(ry2.mag*ry2.mag)

field_ball_x1=[]
for N in range(0,b_N,1):#build field ball from ballx1
    field_ball_x1.append(sphere(pos=vector(size*cos(2*pi*N/b_N), size*sin(2*pi*N/b_N),0)+Qx1.pos,
                             radius=0.01, color=vec(1,1,0), make_trail=True, v=vector(0,0,0)))

field_ball_x2=[]
for N in range(0,b_N,1):#build field ball from ballx2
    field_ball_x2.append(sphere(pos=vector(size*cos(2*pi*N/b_N), size*sin(2*pi*N/b_N),0)+Qx2.pos,
                             radius=0.01, color=vec(1,1,0), make_trail=True, v=vector(0,0,0)))


field_ball_y1=[]
for N in range(0,b_N,1):#build field ball from bally1
    field_ball_y1.append(sphere(pos=vector(size*cos(2*pi*N/b_N), size*sin(2*pi*N/b_N),0)+Qy1.pos,
                             radius=0.01, color=vec(0.8,0.8,0.3), make_trail=True, v=vector(0,0,0)))

field_ball_y2=[]
for N in range(0,b_N,1):#build field ball from bally2
    field_ball_y2.append(sphere(pos=vector(size*cos(2*pi*N/b_N), size*sin(2*pi*N/b_N),0)+Qy2.pos,
                             radius=0.01, color=vec(0.8,0.8,0.3), make_trail=True, v=vector(0,0,0)))

while True:
    rate(1000)        
    for N in field_ball_x1:
        N.v = Force_E(N.pos, 1.0).norm()
        N.pos += N.v*dt

    for N in field_ball_x2:
        N.v = Force_E(N.pos, 1.0).norm()
        N.pos += N.v*dt

    for N in field_ball_y1:
        N.v = Force_E(N.pos, -1.0).norm()
        N.pos += N.v*dt

    for N in field_ball_y2:
        N.v = Force_E(N.pos, -1.0).norm()
        N.pos += N.v*dt

    if mag(q.pos-Qx1.pos)>=size and mag(q.pos-Qx2.pos)>=size and mag(q.pos-Qy1.pos)>=size and mag(q.pos-Qy2.pos)>=size :    
        q.v = q.v + Force_E(q.pos, q_charge)/q_m *dt
        q.pos = q.pos+q.v*dt
    else :
        q.pos = q.pos