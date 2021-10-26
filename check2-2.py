from vpython import *

size = 0.1     #球的大小
theta = 0.0    #初始角度
R = 1.0        #圓周運動半徑
omega = 2*pi   #角速度大小=單位時間繞過的角度
t = 0.0        #初始時間

scene = canvas(width=500, height=500, center=vector(0,0,0), background=vector(148.0/225,228.0/225,204.0/225))
ball = sphere(radius=size, color=color.blue, make_trail=True, interval = 1, retain = 900)

ball.pos = vector(R,0,0)    #球的初始位置
t = 0.0       #初始時間
dt = 0.001    #時間間隔
pre_theta = theta
while True:
    rate(1/dt)
    pre_pre_theta = pre_theta
    pre_theta = theta
    theta += omega*dt    #t時刻的角度
    ball.pos = vector(R*cos(theta), R*sin(theta), 0)
    t += dt              #計時器

    if pre_theta%(2*pi) > pre_pre_theta%(2*pi) and pre_theta%(2*pi) > theta%(2*pi):
        print ('period = ', t)
        t = 0



    
    