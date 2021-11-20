from vpython import *

A = 2               #振幅
N = 200             #介質個數
omega = 2*pi*4      #振動角頻率
size = 0.1          #介質的大小
m1 = 0.2            #單個介質1的質量
m2 = 0.5            #單個介質2的質量
k = 4000.0          #每一小段彈簧的彈力常數
d = 0.1             #介質之間的初始間隔
t, dt = 0, 0.0005   #初始時間，時間差
T = 50*dt           #更新畫面的時間間隔
     
scene = canvas(title='Spring Wave', width=1200, height=300, range = 0.4*50/6, center = vector((N-1)*d/2, 0, 0)) 
ball = [sphere(radius=size, color=color.yellow, pos=vector(i*d, 0, 0), v=vector(0,0,0)) for i in range(N)]
#以list comprehensions方式產生N個球
for i in range(N):
    if i >= int(N/2): ball[i].color = color.blue

ball_pos = [vector(i*d,0,0) for i in range(N)]
ball_v = [vector(0,0,0) for i in range(N)]
spring_pos = [vector(i*d,0,0) for i in range(N-1)]
spring_axis = [vector(d,0,0) for i in range(N-1)]

def SpringForce(r):    #彈力
    return - k*(mag(r))*r/mag(r)
      
while True:
    rate(1/dt)
    t += dt

    if t <= 2*pi/omega/2: ball_pos[0] = vector(0, A*sin(omega*t), 0)    ##強迫第一個球沿x方向振動

    #在球與球之間放入彈簧
    #from index 0 to 49, the elements are 0,1, 2, 3, 4,... , 48, totally 49 springs
    for i in range(N-1):
        spring_pos[i] = ball_pos[i]
        spring_axis[i] = ball_pos[i+1] - ball_pos[i]

    #計算每一個球受相鄰兩條彈簧的彈力
    #from index 1 to 50, the elements are 1, 2, 3, 4,... , 49
    for i in range(1, int(N/2)):        #計算左半段繩子的運動
        ball_v[i] += (-SpringForce(spring_axis[i]) + SpringForce(spring_axis[i-1]))/m1*dt
    for i in range(int(N/2), N-1):      #計算右半段繩子的運動
        ball_v[i] += ( -SpringForce(spring_axis[i]) + SpringForce(spring_axis[i-1]))/m2*dt
    for i in range(1, N):               #算出所有球的位置
        ball_pos[i] += ball_v[i]*dt

    if t%T < T and t%T+dt > T:          #畫圖，每隔T秒更新一次畫面
        for i in range(N):
            ball[i].pos = ball_pos[i]