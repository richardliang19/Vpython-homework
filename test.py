from vpython import*
size = 0.5 #設定球的大小為0.05公尺
scene = canvas(width=600, height=400, center=vector(2.5,0,0), background=vector(0,0,0))

ball = sphere(radius=size, color=color.yellow, pos=vector(0,0,0), v=vector(1,0,0),a=vector(0,0,0))
sphere(color=color.orange,radius=size, pos=vector(0,0.85,0),v=vector(0,0,0),a=vector(0,0,0)) 
sphere(color=color.orange,radius=size, pos=vector(0,-0.85,0),v=vector(0,0,0),a=vector(0,0,0)) 
dt = 0.001 #模擬的時間間隔
t = 0.0  #設定模擬的初始時間
while t < 5:          
    rate(1/dt)      #設定迴圈的執行速度，每秒執行1/dt次
    t +=dt #計時器
    ball.v= ball.v+ball.a*dt
    ball.pos = ball.pos + ball.v*dt  #球的每一時刻位置，每次迴圈改變ball.v *dt的位移)
    sphere(color=color.orange,radius=size, pos=ball.pos,v=vector(0.02,0,0),a=vector(0,0,0))
