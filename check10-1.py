from vpython import *  

R = 20              
B_r = 0.1*R          
theta = 0*pi/180      
w = 1                 
t=0
dt = 0.001         

scene = canvas(width=1000, height=800, center = vec(0,0,0), background=vec(0.3,0.4,0.4), forward=vec(0,0,-1),range=60) 

ball = sphere(radius = B_r , color=color.yellow, make_trail= True, interval=100)
ball.pos = vector( R*cos(theta), R*sin(theta), 0) 
ball.v = vector( 0, 0, 0) 

v_arrow = arrow(pos=ball.pos,axis=vec(0,0,0),shaftwidth=0.2*B_r ,color = color.red)  
a_arrow = arrow(pos=ball.pos,axis=vec(0,0,0),shaftwidth=0.2*B_r ,color = color.white)  

def keyinput(evt):  # keyboard interrupt callback function
    global R, w     # define the global variables that you want to change by this function
    length = {'q' :0.2, 'w' : -0.2}
    angle_v = {'a' : 0.1, 's': -0.1}
    
    s = evt.key
    if s in length : R = R + length[s]
    if s in angle_v: w = w + angle_v[s]
scene.bind('keydown', keyinput)  

while True :             
    rate(1000)     
    
    theta = theta + w * dt          
    ball.pos = vector (R*cos(theta), R*sin(theta), 0 )

    v_arrow.pos = ball.pos
    v_arrow.axis = cross(vector(0,0,1),ball.pos).norm() * R * w
    a_arrow.pos = ball.pos
    a_arrow.axis = - ball.pos.norm() * R * w * w

    t = t + dt