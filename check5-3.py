from vpython import *  #引用視覺畫套件Vpython
"""
    1. 參數設定，設定變數及定義萬有引力公式
"""
G = 6.67*10**(-11) ; M = 6*10**24 ; m = 1000  
Re = 6.4*10**6 ; H = 5*Re ; t = 0 ; dt = 10
def Fg(x):                                 #定義公式
    return -G*M*m/(x**2)
Fe = G*M*m/Re**2 #定義地球表面重力強度

"""
    2. 畫面設定
"""
scene = canvas(align = 'left',title ='4_01_Gravity force',  width=800, height=300, center=vector(0,0,0), background=vector(0.6,0.8,0.8)) #設定視窗
earth = sphere(pos=vector(0,0,0), radius=Re, texture=textures.earth) #放置物件地球
mater = sphere(pos=vector(H,0,0), radius=0.1*Re,color=color.red, make_trail=True) #放置物件衛星
V0= (G*M/H)**0.5
materv=vector(0,0.8*V0,0)

"""
    3. 執行迴圈
"""

pre_x = H
while True:  #執行迴圈
    rate(1000)
    
    dist = ((mater.pos.x-earth.pos.x)**2+(mater.pos.y-earth.pos.y)**2+(mater.pos.z-earth.pos.z)**2)**0.5 #距離純量
    radiavector = (mater.pos-earth.pos)/dist #距離單位向量
    Fg_vector = Fg(dist)*radiavector # 萬有引力向量=萬有引力量值*單位向量
    
    pre_pre_x =pre_x
    pre_x = mater.pos.x

    materv += Fg_vector/m*dt   #Δv = F/m *dt
    mater.pos = mater.pos + materv*dt  # S = S0 + v *dt

    t = t+dt
    if pre_x > pre_pre_x and pre_x > mater.pos.x :
        print(t)  
        t = 0


