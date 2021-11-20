from vpython import *

A = 1            #振幅
N = 50             #介質個數
omega = 3*pi/1.0   #振動角頻率
size = 0.1         #介質的大小
m = 0.1            #介質的質量
k = 500.0          #每一小段彈簧的彈力常數
d = 0.4            #介質之間的初始間隔
g = 9.8
b = 0.1
scene = canvas(title='Spring Wave', width=300, height=800, range = 0.4*50/6, center = vector(0, -(N-1)*d/2, 0)) 
ball = [sphere(radius=size, color=color.yellow, pos=vector(0, -i*d, 0), v=vector(0,0,0)) for i in range(N)]
#以list comprehensions方式產生N個球
spring = [helix(radius = size/2.0, thickness = d/15.0, pos=vector(0, -i*d, 0), axis=vector(d,0,0)) for i in range(N-1)]
#以list comprehensions方式產生N-1條彈簧


def SpringForce(r):    #彈力
    return - k*(mag(r)-d)*r/mag(r)
      
t, dt = 0, 0.001       #初始時間，時間差
while True:
    rate(1000)
    t += dt

    ball[0].pos = vector(A*sin(omega*t), 0, A*cos(omega*t))    ##強迫第一個球沿x方向振動

    #在球與球之間放入彈簧
    #from index 0 to 49, the elements are 0,1, 2, 3, 4,... , 48, totally 49 springs
    for i in range(N-1):
        spring[i].pos = ball[i].pos
        spring[i].axis = ball[i+1].pos - ball[i].pos

    #計算每一個球受相鄰兩條彈簧的彈力
    #from index 1 to 50, the elements are 1, 2, 3, 4,... , 49
    for i in range(1, N):      
        if i == N-1: ball[-1].v += (SpringForce(spring[-1].axis)+vector(0,-m*g,0)-b * ball[i].v)/m*dt                        #最後一個球
        else : ball[i].v += (-SpringForce(spring[i].axis) + SpringForce(spring[i-1].axis)+vector(0,-m*g,0)-b * ball[i].v)/m*dt  #非最後且非第一個的球

        ball[i].pos += ball[i].v*dt