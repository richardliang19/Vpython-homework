from vpython import*
import numpy as np
N = 50		#質點個數
g = 9.8		#重力加速度
size = 0.016
thick = size/5.0
m, k, d =  0.1/N, N*0.5, thick    #球大小、質點質量、各力常數、間距
t, dt = 0, 0.0001                                #初始時間、時間間隔
ball_cm = 0
damp = 5.0
scene = canvas(width=300, height = 600, center = vector(0, -2, 0))
mybox = box(pos=vector(0,0,0), length=1.5, height=0.08, width=1.5)
#balls = [sphere(radius=size, color=color.yellow) for i in range(N)]
cball = sphere(radius = 4*size/2.0,pos= vector(0,0,0), color = color.green)
lastball = sphere(radius = 8*size/2.0,pos= vector(0,0,0), color = color.red)
springs = [helix(radius = 8*size/2.0, thickness = thick, d= thick, coils = 1) for i in range(N-1)]

ball_pos, ball_v, ball_g = np.zeros((N, 3)), np.zeros((N,3)), np.zeros((N,3))
#以array建立初位置、初速度、重力加速度，全為0的N列3行的陣列

for i in range(N):
    ball_pos[i][1] = -d*i*0.9 #將球沿y方向的初位置，沿axis=0擺入pos array，並使兩端點距離為0.9倍繩子全長
    ball_g[i][1] = -g        #將重力加速度陣列的第2行改為-9.8，表示每個球在y方向受到的重力場

vtgraph =  graph(title = "v-t graph", width=600, height=400, xtitle="t", ytitle="v")
f1 = gcurve(color=color.green)
f2 = gcurve(color=color.red)

while True:
    rate(1/dt/3)
    t += dt        #計時器
    spring_axis = ball_pos[1:] - ball_pos[:-1]        #每個彈簧的軸方向
    b = np.sum(spring_axis**2, axis = 1)**0.5         #每個彈簧的長度
    spring_axis_unit = spring_axis / b[:, np.newaxis] #每個彈簧軸方向的單位向量
    fs = - k * (spring_axis - d*spring_axis_unit)     #每個彈簧的作用力
   
    ball_v[1:-1] += (fs[:-1] - fs[1:])/m*dt + ball_g[1:-1]*dt - damp*ball_v[1:-1]*dt    #計算第二個~倒數第二個球的速度
    ball_v[-1] +=(fs[-1])/m*dt + ball_g[-1]*dt - damp*ball_v[-1]*dt
    ball_pos+= ball_v*dt                            #計算球的位置
    T = t % (50*dt)                  #用餘數除法定出要更新圖形的時間點，每50個迴圈會歸零一次


    if t > 5: #設定釋放時機點，t < T0前球1不動，之後球1也受力落下
        damp = 0
        ball_v[0] += (-fs[0])/m*dt + ball_g[0]*dt   	#請寫入球1釋放後的受力，使球1開始運動
        
        
    for j in arange(N-1): #由第1根彈簧算到最個最後1根，個數比球少1個
        if (ball_pos[j][1] - ball_pos[j+1][1]) <= d:  #球和球間距小於彈簧原長
            ball_v[j] = ball_v[j+1] = (ball_v[j] + ball_v[j+1])/2  #碰撞後速度
            ball_pos[j+1][1] = ball_pos[j][1] - d                  #碰撞後球的間距

    if T + dt >50*dt and T < 50*dt:  #在T被歸零前的那瞬間更新畫面圖形
        #for i in range(N):        #畫球
            #balls[i].pos = vector(ball_pos[i][0], ball_pos[i][1], ball_pos[i][2])
        for i in range(N-1):      #畫彈簧
            springs[i].pos = vector(ball_pos[i][0], ball_pos[i][1], ball_pos[i][2])
            springs[i].axis = vector(ball_pos[i+1][0], ball_pos[i+1][1], ball_pos[i+1][2]) -vector(ball_pos[i][0], ball_pos[i][1], ball_pos[i][2])
    
    ball_cm = np.sum(ball_pos, axis = 0)/N  #這是個1維3個元素的array
    ball_cv = np.sum(ball_v, axis = 0)/N
    cball.pos = vector(ball_cm[0],ball_cm[1],ball_cm[2])
    lastball.pos = vector(ball_pos[-1][0], ball_pos[-1][1], ball_pos[-1][2])
    
    if t>5:
        f1.plot(pos=(t,ball_cv[1]))
        f2.plot(pos=(t,ball_v[-1][1]))
