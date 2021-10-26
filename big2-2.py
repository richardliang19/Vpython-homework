from vpython import *

g = 9.8                 #重力加速度 9.8 m/s^2
size =0.3            #球半徑 0.5 m
height = 0           #球初始高度 0 m
m = 1                #球質量1kg
Fg = vector(0, -m*g, 0) #重力
OAO=0
scene = canvas(width=600, height=600,x=0, y=0, center = vector(0,0,0)) #設定畫面
floor = box(length=25, height=0.05, width=10, color=color.green)  	#畫地板
ball = sphere(radius = size, color=color.yellow, make_trail= True, trail_type="points", interval=10) 	#畫球
show_angle = label(pos=vector(0,-7*size,0), box = False, height = 20, color=color.yellow)

ball.a=Fg/m
theta= 3*pi/180
v0=10
ball.v = vector(v0*cos(theta), v0*sin(theta), 0)
ball.pos=vector(0,size,0)
gd1 = graph(title = "theta-R plot", width=600, height=400, xtitle="theta", ytitle="R")
f1 = gcurve(color=color.red)
gd2 = graph(title = "theta-T plot", width=600, height=400, xtitle="theta", ytitle="T")
f2 = gcurve(color=color.blue)
t=0.0
dt=0.001
while True:
    rate(10/dt)
    
    t=t+dt
    ball.v = ball.v + ball.a*dt
    ball.pos = ball.pos + ball.v*dt
    if ball.pos.y <= size:
        print("T=",t,",R=",ball.pos.x,",theta=",theta*180/pi)
        f1.plot(pos=(theta*180/pi,ball.pos.x))
        f2.plot(pos=(theta*180/pi,t))
        t=0
        theta = theta + 3 * pi/180     #每次迴圈增加仰角3度
        if theta>pi:
            break
        ball.pos = vector(0, size, 0)  #位置重設
        ball.v = vector(v0*cos(theta), v0*sin(theta), 0)  #速度重設
    show_angle.text = 'theta = %1.0f deg' %(theta/pi*180)
        
            


