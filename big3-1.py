from vpython import *
g = 9.8                 
size = 0.05                     
L = 0.5                 
k = 10                  
m = 0.1                 
Fg = m*vector(0,-g,0)   

def SpringForce(r,L):
    return -k*(mag(r)-L)*r/mag(r)

scene = canvas(width=600, height=600, center=vector(0, -L*0.8, 0), range=1.2*L)
ceiling = box(length=0.4, height=0.005, width=0.4, opacity = 0.2)
ball = sphere(radius = size,  color=color.yellow, make_trail = True, retain = 1000, interval=1)
spring = helix(radius=0.02, thickness =0.01)

gd1 = graph(title = "Energy check: green for K, red for Uk, blue for Ug, black for total", width=600, height=400, xtitle="t", ytitle="energy")
f1 = gcurve(color=color.green)
f2 = gcurve(color=color.red)
f3 = gcurve(color=color.blue)
f4 = gcurve(color=color.black) 

v_vector = arrow(shaftwidth = 0.02, color=color.green)
Ftot_vector = arrow(shaftwidth = 0.02, color=color.red)
mg_vector = arrow(shaftwidth = 0.02, color=color.yellow)
Fs_vector = arrow(shaftwidth = 0.02, color=color.white)
X = 0.2

v_text = label(box = False, opacity = 0, height = 25, color=color.green, text = 'v')
Fs_text = label(box = False, opacity = 0, height = 25, color=color.white, text = 'Fs')
mg_text = label(box = False, opacity = 0, height = 25, color=color.yellow, text = 'Fg')
Ftot_text = label(box = False, opacity = 0, height = 25, color=color.red, text = 'F_tot')
	
ball.pos = vector(0, -L, 0)     
ball.v = vector(0, 0, 0)        
spring.pos = vector(0, 0, 0)    

dt = 0.001
t = 0.0

while t<10:
    rate(0.5/dt)
    spring.axis = ball.pos - spring.pos           
    ball.a = (Fg + SpringForce(spring.axis,L))/m  
    ball.v += ball.a*dt      
    ball.pos += ball.v*dt    
    
    t=t+dt
    
    v_vector.pos = ball.pos + vector(2.5*size,0,0)      
    Ftot_vector.pos = ball.pos + vector(-2.5*size,0,0)  
    mg_vector.pos = ball.pos    
    Fs_vector.pos = ball.pos    

    v_vector.axis = ball.v * X                               
    Ftot_vector.axis = (Fg + SpringForce(spring.axis,L)) * X  
    mg_vector.axis = Fg * X                                   
    Fs_vector.axis = SpringForce(spring.axis,L) * X           

    v_text.pos = v_vector.pos + v_vector.axis*1.2
    Ftot_text.pos = Ftot_vector.pos + Ftot_vector.axis*1.2
    mg_text.pos = mg_vector.pos + mg_vector.axis*1.2
    Fs_text.pos = Fs_vector.pos + Fs_vector.axis*1.2

    f1.plot(pos=(t,0.5*m*mag(ball.v)*mag(ball.v)))
    f2.plot(pos=(t,0.5 * k * (mag(spring.axis) - L)**2))
    f3.plot(pos=(t,m * g *(ball.pos.y+L)))
    f4.plot(pos=(t, 0.5*m*mag(ball.v)*mag(ball.v) + 0.5 * k * (mag(spring.axis) - L)**2  + m * g * (ball.pos.y+L)))
    