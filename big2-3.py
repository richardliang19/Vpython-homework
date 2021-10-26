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
back=False
period_t=0
N=20
plot_t=0
circlecount=0
while True:
    if circlecount>3:
        break
    rate(1/dt)
    pre_pre_theta = pre_theta
    pre_theta = theta
    theta += omega*dt    #t時刻的角度
    ball.pos = vector(R*cos(theta), R*sin(theta), 0)
    t += dt              #計時器

    if back:
        plot_t = t % (period_t/N) #將週期切成N等分，並用餘數除法設定畫圖時間點
        if plot_t + dt >= period_t/N  and plot_t <  period_t/N: #畫圖時間判斷點
            cylinder(radius=size/50, color=color.black, pos=vector(0,0,0) , axis= ball.pos) #畫細線
    if pre_theta%(2*pi) > pre_pre_theta%(2*pi) and pre_theta%(2*pi) > theta%(2*pi):
        print ('period = ', t)
        circlecount+=1
        back=True
        period_t=t
        t = 0



    
    