from vpython import *
g = 9.8                 
size = 0.05                    
L = 0.5                 
k = 100000              
m = 0.1                 
theta = 30 * pi/180     
Fg = m*vector(0,-g,0)   
R=1.0

def SpringForce(r,L):
    return -k*(mag(r)-L)*r/mag(r)

def SpringDamp(v, r):  
    cos_theta = dot(v,r)/(mag(v)*mag(r))                   
    r_unit_vector = norm(r)                                 
    projection_vector = mag(v) * cos_theta * r_unit_vector  
    spring_damp = - 0.8 * projection_vector                
    return spring_damp

scene = canvas(width=600, height=600, center=vector(0, -L*0.8, 0), range=1.2*L)
ceiling = box(length=0.4, height=0.005, width=0.4, opacity = 0.2)
ball = sphere(radius = size,  color=color.blue, make_trail = True, retain = 1000, interval=1)
rod = cylinder(radius=size/10)
	
ball.pos = vector(L*sin(theta), -L*cos(theta), 0)  
ball.v = vector(0, 0, sqrt(g*L*sin(theta)*tan(theta)))                            
rod.pos = vector(0, 0, 0)                         

F_vector = arrow(color = color.yellow)
total_vector = arrow(color = color.red)
v_vector = arrow(color = color.green)
mg_vector = arrow(color = color.blue)
F_text = label(box = False, opacity = 0, height = 25, color=color.yellow, text = 'F')
total_text = label(box = False, opacity = 0, height = 25, color=color.red, text = "合力")
v_text = label(box = False, opacity = 0, height = 25, color=color.green, text = 'v')
mg_text = label(box = False, opacity = 0, height = 25, color=color.blue, text = "mg")

dt = 0.001    
t = 0.0       

pre_x = ball.pos.x        

while True:
    rate(1/dt)
    rod.axis = ball.pos - rod.pos                
    ball.a = (Fg + SpringForce(rod.axis,L) +SpringDamp(ball.v,rod.axis))/m   

    v_vector.pos = ball.pos
    mg_vector.pos = ball.pos
    F_vector.pos = ball.pos
    total_vector.pos = ball.pos

    pre_pre_x = pre_x      
    pre_x = ball.pos.x     
    
    ball.v += ball.a*dt    
    ball.pos += ball.v*dt  
    t += dt

    if mag(ball.v) > 0: 
        v_vector.axis = ball.v/mag(ball.v)/4  
    if mag(SpringForce(rod.axis,L)) > 0: 
        F_vector.axis = SpringForce(rod.axis,L)/mag(SpringForce(rod.axis,L))/4
    if mag(Fg)>0:
        mg_vector.axis = Fg/mag(Fg)/4
    if mag(ball.a)>0 :
        total_vector.axis= (ball.a)/mag(ball.a)/4

    v_text.pos = v_vector.pos + v_vector.axis*1.2
    mg_text.pos = mg_vector.pos + mg_vector.axis*1.2
    F_text.pos = F_vector.pos + F_vector.axis*1.2
    total_text.pos = total_vector.pos + total_vector.axis*1.2
    if pre_x > pre_pre_x and pre_x > ball.pos.x:   
        print ('simulated period = ', t, ', theoretical period = ', 2*pi*(L*cos(theta)/g)**0.5 )   
        t = 0  