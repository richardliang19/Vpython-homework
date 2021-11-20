"""
    建國中學 vpython 物理模擬
    作者: 物理 科賴奕帆老師
    高二物理
    gas collision
"""
from vpython import *
from random import *
"""
1. 參數設定
"""
t = 0.0 ; t1 = 0.0  ; dt = 0.0001 #時間參數
theta = 30.0 * pi / 180 #氣體入射角度
d = 3.0  #氣體與牆壁距離
r = 0.50  #氣柱半徑
v0 = 2.0  # 氣體初速率
m = 0.01  #單一氣體質量
per_N = 100.0 #每秒射出的氣體數


theta = 00.0 * pi / 180 #氣體入射角度, 改為平行入射
per_N = 5.0 #每秒射出的粒子數,改為每秒射入5個粒子

k = 9*10**9  #設定庫倫常數
Q_charge = 10**(-5)  #設定金原子電量    
q_charge = 10 **(-8) #設定粒子電量
q_m = 10**(-3)       #設定粒子質量


"""
2. 畫面設定
"""
scene = canvas(align = 'left' , center = vec ( 0.5*d , 0 , 0 ) , height=600, width=1000, range=3.5,
                auto_scale=False, background=vec(0.6,0.8,0.8) , fov = 0.004)  #設定畫面

#wall = box(pos=vec(0.0,0,0),length=0.6, height=5 ,  width=5, opacity = 0.9 , texture = textures.wood)  #設定牆壁             

gas = []  #氣體的List

Q = sphere(pos = vec(0,0,0) ,  radius = 0.2 , color = color.yellow)

def Force_E(r, q):
    r1 = r - Q.pos
    return k*q*Q_charge*r1.norm()/(r1.mag*r1.mag)

sum_F = 0  #計算程式中每顆小球撞擊牆壁時的總力
"""
3. 執行迴圈
"""
while True:
    rate(10000)
    t = t + dt       #時間
    t1 = t1 + dt  
    sum_F = 0     #每千分之一秒，程式內的總力要歸零重算

    if t1 > 1/ per_N:  # 設定per_N = 100.0時，則每1/100秒會射出一顆空氣分子
        t1 = 0  
        r_dom = random()  #空氣射出的位置隨機參數
        p_dom = random() #空氣射出的角度位置參數
        gas.append( sphere(pos = vector((-d*cos(theta)+r*r_dom*cos(p_dom*2*pi)*sin(theta)),(d*sin(theta)+r*r_dom*cos(p_dom*2*pi)*cos(theta)),(r*r_dom*sin(p_dom*2*pi))) , radius = 0.05, v = vec(v0*cos(theta),-v0*sin(theta),0) , Fx = 0 ,make_trail=True ,visible = True))
        # 每1/100秒會產生一個隨機位置的空氣分子，以相同的速度射出
    for N in gas :  #gas List內所有的空氣分子撞擊牆壁時，都會受到一個-Kx的向左受力
        N.v = N.v + Force_E(N.pos, q_charge)/q_m *dt
        N.pos = N.pos+N.v*dt
        
        if mag(N.pos -  vec(0,0,0) ) > 4: #若粒子離原點超過4的距離就會從List消除
            N.visible = False
            N = None