from vpython import *  #引用視覺畫套件Vpython
"""
    1. 參數設定，設定變數及定義萬有引力公式
"""
G = 6.67*10**(-11) ; M = 6*10**24 ; m = 1000  
Re = 6.4*10**6 ; H = 5*Re ; t = 0 ; dt = 1
def Fg(x):                                 #定義公式
    return -G*M*m/(x**2)

Fe = G*M*m/Re**2 #定義地球表面重力強度



"""
    2. 畫面設定
"""
scene = canvas(align = 'left',title ='4_01_Gravity force',  width=800, height=300, center=vec(0,0,0), background=vec(0.6,0.8,0.8)) #設定視窗
earth = sphere(pos=vec(0,0,0), radius=Re, texture=textures.earth) #放置物件地球
mater1 = sphere(pos=vec(H,0,0), radius=0.1*Re,color=color.blue, make_trail=True) #放置物件衛星
mater2 = sphere(pos=vec(H,0,0), radius=0.1*Re,color=color.red, make_trail=True) #放置物件衛星
mater3 = sphere(pos=vec(H,0,0), radius=0.1*Re,color=color.yellow, make_trail=True) #放置物件衛星
V0= (G*M/H)**0.5
mater1v=vector(0,0.7*V0,0)
mater2v=vector(0,V0,0)
mater3v=vector(0,1.2*V0,0)
"""
    3. 執行迴圈
"""
while True:  #執行迴圈
    rate(10000)
    dist = ((mater1.pos.x-earth.pos.x)**2+(mater1.pos.y-earth.pos.y)**2+(mater1.pos.z-earth.pos.z)**2)**0.5 #距離純量
    radiavector1 = (mater1.pos-earth.pos)/dist #距離單位向量
    Fg_vector1 = Fg(dist)*radiavector1 # 萬有引力向量=萬有引力量值*單位向量
    
    mater1v += Fg_vector1/m*dt   #Δv = F/m *dt
    mater1.pos = mater1.pos + mater1v*dt  # S = S0 + v *dt
    
    dist = ((mater2.pos.x-earth.pos.x)**2+(mater2.pos.y-earth.pos.y)**2+(mater2.pos.z-earth.pos.z)**2)**0.5 #距離純量
    radiavector2 = (mater2.pos-earth.pos)/dist #距離單位向量
    Fg_vector2 = Fg(dist)*radiavector2 # 萬有引力向量=萬有引力量值*單位向量
    
    mater2v += Fg_vector2/m*dt   #Δv = F/m *dt
    mater2.pos = mater2.pos + mater2v*dt  # S = S0 + v *dt

    dist = ((mater3.pos.x-earth.pos.x)**2+(mater3.pos.y-earth.pos.y)**2+(mater3.pos.z-earth.pos.z)**2)**0.5 #距離純量
    radiavector3 = (mater3.pos-earth.pos)/dist #距離單位向量
    Fg_vector3 = Fg(dist)*radiavector3 # 萬有引力向量=萬有引力量值*單位向量
    
    mater3v += Fg_vector3/m*dt   #Δv = F/m *dt
    mater3.pos = mater3.pos + mater3v*dt  # S = S0 + v *dt

    t = t+dt
 
