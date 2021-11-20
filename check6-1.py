from vpython import * 

G = 6.67 ; m1 = 10 ; m2 = 3 ; R = 10 ; v_m2 = (G*m1/R)**0.5 ; t = 0 ; dt = 0.001

def Fg(x):
    return -G*m1*m2/(x**2)

gd = graph(align='left',width=400,height=400,  
              title='K1+K2+U=E', xtitle='t', ytitle='E(red),K1(black),K2(blue),U(green)',
              foreground=color.black,background=color.white)
f1 = gcurve(color=color.red)  
f2 = gcurve(color=color.black)  
f3 = gcurve(color=color.blue)  
f4 = gcurve(color=color.green)

 
scene = canvas(width=1200, height=800, center=vec(0,0,0),
                background=vec(0.6,0.8,0.8),range=2*R)

ball_m1 = sphere(pos=vector(0,0,0), radius=1, color = color.blue, make_trail=True)
ball_m2 = sphere(pos=vector(R,0,0), radius=0.3, color = color.red, make_trail=True)
ball_m1_v = vector(0,-0.3*v_m2,0)
ball_m2_v = vector(0,v_m2,0)

while True:
    rate(2000)
    dist = ((ball_m1.pos.x-ball_m2.pos.x)**2+(ball_m1.pos.y-ball_m2.pos.y)**2+(ball_m1.pos.z-ball_m2.pos.z)**2)**0.5
    radiavector = (ball_m2.pos-ball_m1.pos)/dist
    Fg_vector = Fg(dist)*radiavector 

    ball_m2_v += Fg_vector/m2*dt 
    ball_m2.pos = ball_m2.pos + ball_m2_v*dt

    ball_m1_v += -Fg_vector/m1*dt 
    ball_m1.pos = ball_m1.pos + ball_m1_v*dt 
    
    K1 = 0.5*m1*(mag(ball_m1_v)**2)
    K2 = 0.5*m2*(mag(ball_m2_v)**2)
    U = -G*m1*m2/dist 
    E = K1+ K2 + U 
    f1.plot(pos=(t,E))  
    f2.plot(pos=(t,K1))
    f3.plot(pos=(t,K2))    
    f4.plot(pos=(t,U)) 
    t = t+dt