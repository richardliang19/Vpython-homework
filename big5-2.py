from vpython import *  #引用視覺畫套件Vpython
"""
    1. 參數設定，設定變數及定義萬有引力公式
"""
G = 6.67*10**(-11) ; M = 6*10**24 ; m1 = 1000 ; m2 =800
Re = 6.4*10**6 ; H = 5*Re ; t1 = 0 ; t2 = 0 ; dt = 5
def Fg(x,M,m):                                 #定義公式
    return -G*M*m/(x**2)




"""
    2. 畫面設定
"""
scene = canvas(align = 'left',  width=800, height=300, center=vec(0,0,0), background=vec(0.6,0.8,0.8)) #設定視窗
sun = sphere(pos=vec(0,0,0), radius=Re,color =color.yellow) #放置物件地球
mater1 = sphere(pos=vec(1.2*H,0,0), radius=0.2*Re, make_trail=True,texture=textures.earth) #放置物件衛星
mater2 = sphere(pos=vec(H,0,0), radius=0.1*Re,color=color.red, make_trail=True) #放置物件衛星

V0_1= (G*M/H/1.2)**0.5
V0_2= (G*M/H)**0.5
mater1v=vector(0,0.8*V0_1,0)
mater2v=vector(0,0.8*V0_2,0)

pre_x1 = 1.2*H
pre_x2 = H


"""
    3. 執行迴圈
"""
while True:  #執行迴圈
    rate(2000)

    dist1 = ((mater1.pos.x-sun.pos.x)**2+(mater1.pos.y-sun.pos.y)**2+(mater1.pos.z-sun.pos.z)**2)**0.5 #距離純量
    radiavector1 = (mater1.pos-sun.pos)/dist1 #距離單位向量
    Fg_vector1 = Fg(dist1,M,m1)*radiavector1 # 萬有引力向量=萬有引力量值*單位向量
    
    pre_pre_x1 =pre_x1
    pre_x1 = mater1.pos.x

    mater1v += Fg_vector1/m1*dt   #Δv = F/m *dt
    mater1.pos = mater1.pos + mater1v*dt  # S = S0 + v *dt

    dist2 = ((mater2.pos.x-sun.pos.x)**2+(mater2.pos.y-sun.pos.y)**2+(mater2.pos.z-sun.pos.z)**2)**0.5 #距離純量
    radiavector2 = (mater2.pos-sun.pos)/dist2 #距離單位向量
    Fg_vector2 = Fg(dist2,M,m2)*radiavector2 # 萬有引力向量=萬有引力量值*單位向量
    
    pre_pre_x2 =pre_x2
    pre_x2 = mater2.pos.x

    mater2v += Fg_vector2/m2*dt   #Δv = F/m *dt
    mater2.pos = mater2.pos + mater2v*dt  # S = S0 + v *dt

    t1 = t1+dt
    t2 = t2+dt
    
    if pre_x1 < pre_pre_x1 and pre_x1 < mater1.pos.x :
        left1=mater1.pos.x
    
    if pre_x2 < pre_pre_x2 and pre_x2 < mater2.pos.x :
        left2=mater2.pos.x
    
    if pre_x1 > pre_pre_x1 and pre_x1 > mater1.pos.x :
        right1=mater1.pos.x
        print(abs(right1-left1)**3/t1**2)
        t1=0
    
    if pre_x2 > pre_pre_x2 and pre_x2 > mater2.pos.x :
        right2=mater2.pos.x
        print(abs(right2-left2)**3/t2**2)
        t2=0