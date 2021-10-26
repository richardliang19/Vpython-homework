from vpython import *

size = 0.1
theta = 0.0
R = 1.0
omega = 2*pi

scene = canvas(width=500, height=500, center=vector(0,0,0), range=1.5*R, background=vector(148.0/255,228.0/255,204.0/255))
ball = sphere(radius=size, color=color.blue, make_trail=True, interval=1, retain=1000)
ball.pos = vector(R,0,0)

v_vector = arrow(color=color.green)  #畫描述v的箭頭
a_vector = arrow(color=color.red)
v_text = label(box = False, opacity = 0, height = 25, color=color.green, text = 'v')  #產生文字標籤'v'
a_text = label(box = False, opacity = 0, height = 25, color=color.red, text = 'a')
dt = 0.001
t = 0.0

pre_theta = theta

while True:
    rate(1/dt)
    t = t + dt

    pre_pre_theta = pre_theta    #前前時刻角度
    pre_theta = theta            #前一時刻角度
    theta = theta + omega*dt     #現在時刻角度

    pre_pre_ball_pos = vector(R*cos(pre_pre_theta),R*sin(pre_pre_theta),0) #球前前時刻的位置
    pre_ball_pos = vector(R*cos(pre_theta),R*sin(pre_theta),0)             #球前一時刻的位置
    now_ball_pos = vector(R*cos(theta),R*sin(theta),0)                     #球現在時刻的位置
    ball.pos = pre_ball_pos    #將球物件畫在前一時刻的位置（ps.上面三個可任挑，dt很小肉眼看不出來差別）
    
    ball_v_12 = (pre_ball_pos - pre_pre_ball_pos)/dt   #前半程平均速度
    ball_v_23 = (now_ball_pos - pre_ball_pos)/dt       #後半程平均速度
    ball.v = ball_v_12         #將球的速度指定為前半程平均速度（ps.這兩個平均速度也可任挑，理由同上）
    
    ball.a = (ball_v_23 - ball_v_12)/dt

    v_vector.pos = ball.pos    #將速度箭頭的位置放在球的位置
    a_vector.pos = ball.pos
    if mag(ball.v) > 0: 
        v_vector.axis = ball.v/mag(ball.v)*R/2    #將速度箭頭的軸方向指向速度方向，並將箭頭的長度設定為半徑的一半 #mag()向量大小
    if mag(ball.a) > 0: 
        a_vector.axis = ball.a/mag(ball.a)*R/2

    v_text.pos = v_vector.pos + v_vector.axis*1.2 #文字標籤'v'的位置
    a_text.pos = a_vector.pos + a_vector.axis*1.2
    print("simulated acceleration = ",mag(ball.a),"theoretical centripetal acceleration = ", mag(ball.v)*mag(ball.v)/R)