from vpython import *
g = 9.8         #重力加速度
k = 80.0        #彈力常數
L0 = 0.6        #彈簧原長
H = 1.5         #球的初始高度
m = 0.5         #球的質量
d = 0.15        #震盪子的水平間距
size = 0.06     #球的大小
n = 40          #球的個數
T = 0.05        #相鄰兩球落下的時間差

scene = canvas(width=800, height=400, center=vector(d*n/2-d/2,L0,0))
floor = box(length=d*n, height=0.005, width=0.3, color=color.yellow, pos=vector(d*n/2-d/2,0,0))    #畫地板

def SpringForce(r,L):    #彈力
    return -k*(mag(r)-L)*r/mag(r)

dt = 0.001    #時間間隔
t = 0.0       #初始時間

ball = []
spring = []
touched = [False] * n   
a=[vector(0,0,0)]*n
for i in range(0,n,1):
    ball.append(sphere(radius = size, color =color.red, pos=vector(i*d,H,0), v=vector(0,0,0)))
    spring.append(helix(radius=0.03, thickness=0.01, pos=vector(i*d,0,0), axis=vector(0,L0,0)))

while True:

    rate(1/dt/3)        #以1/3的速度慢速模擬
    t = t + dt          #計時器

    for j in range(0,n,1):
        if t > j*T: 
            a[j]=vector(0,-g,0)

    for i in range(0,n,1):
        if ball[i].pos.y - spring[i].pos.y - spring[i].axis.y <= size:      #球的下緣接觸到彈簧的條件
            touched[i] = True  #接觸到了，將原先預設False改為True
        if touched[i]:
            spring[i].axis = ball[i].pos-spring[i].pos - vector(0,size,0)   #球接觸到彈簧之後，將彈簧的尾端鎖在球的下緣

        a[i] = a[i] + SpringForce(spring[i].axis,L0)/m     #球的加速度
        ball[i].v = ball[i].v + a[i]*dt                    #球的速度
        ball[i].pos = ball[i].pos + ball[i].v*dt           #球的位置