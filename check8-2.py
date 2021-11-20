from vpython import*
import numpy as np
N = 40		#質點個數
g = 9.8		#重力加速度
size, m, k, d = 0.016, 0.1/N, N*1000.0, 2.0/N    #球大小、質點質量、各力常數、間距
t, dt = 0, 0.0001                                #初始時間、時間間隔
T = 0
b_air = 0.1
scene = canvas(width=1200, height = 600, center = vector(d*N/2.0*0.9, 0, 0)) 

c = curve([vector(d*i*0.9, 0, 0) for i in range(N)], radius = 0.01) 


#畫曲線描點，並給定初始狀態每個點的初位置
ball_pos, ball_v, ball_g = np.zeros((N, 3)), np.zeros((N,3)), np.zeros((N,3))
#以array建立初位置、初速度、重力加速度，全為0的N列3行的陣列

for i in range(N):
    ball_pos[i][0] = d*i*0.9 #將球沿x方向的初位置，沿axis=0擺入pos array，並使兩端點距離為0.9倍繩子全長
    ball_g[i][1] = -g        #將重力加速度陣列的第2行改為-9.8，表示每個球在y方向受到的重力場

while True:
    rate(5/dt)
    t += dt        #計時器
    spring_axis = ball_pos[1:] - ball_pos[:-1]        #每個彈簧的軸方向
    b = np.sum(spring_axis**2, axis = 1)**0.5         #每個彈簧的長度
    spring_axis_unit = spring_axis / b[:, np.newaxis] #每個彈簧軸方向的單位向量
    fs = - k * (spring_axis - d*spring_axis_unit)     #每個彈簧的作用力
    fs[b<=d] = 0                                      #彈簧長度小於原長設為零，表示繩子的鬆弛狀態
    
    ball_v[1:-1] += (fs[:-1] - fs[1:])/m*dt + ball_g[1:-1]*dt - 5.0*ball_v[1:-1]*dt - b_air*ball_v[1:-1]/m*dt
    ball_v[-1] += fs[-1]/m*dt + ball_g[-1]*dt - 5.0*ball_v[-1]*dt - b_air*ball_v[-1]/m*dt
                                                      #計算第二個~倒數第二個球的速度
    ball_pos += ball_v *dt                            #計算球的位置
    T = t % (100*dt)                  #用餘數除法定出要更新圖形的時間點，每50個迴圈會歸零一次
    if T + dt >100*dt and T < 100*dt:  #在T被歸零前的那瞬間更新畫面圖形
        for i in range(N):        #畫球
            c.modify(i, pos=vector(ball_pos[i][0],ball_pos[i][1],ball_pos[i][2]))
    
    