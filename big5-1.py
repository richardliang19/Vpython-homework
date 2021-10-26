from vpython import *  #引用視覺畫套件Vpython
"""
    1. 參數設定，設定變數及定義萬有引力公式
"""
G = 6.67*10**(-11) ; M = 6*10**24 ; m = 1000  
Re = 6.4*10**6 ; H = 5*Re ; t = 0 ; dt = 2
def Fg(x):                                 #定義公式
    return -G*M*m/(x**2)
Fe = G*M*m/Re**2 #定義地球表面重力強度

"""
    2. 畫面設定
"""

scene = canvas(align = 'left',  width=2400, height=900, center=vector(0,0,0), background=vector(0.6,0.8,0.8)) #設定視窗
earth = sphere(pos=vector(0,0,0), radius=Re, texture=textures.earth) #放置物件地球
mater = sphere(pos=vector(H,0,0), radius=0.1*Re,color=color.red, make_trail=True) #放置物件衛星
V0= (G*M/H)**0.5
materv=vector(0,0.8*V0,0)
aT_arrow = arrow(pos=mater.pos,axis=vec(0,0,0),shaftwidth=0.6*mater.radius ,color = color.black)
aN_arrow = arrow(pos=mater.pos,axis=vec(0,0,0),shaftwidth=0.6*mater.radius ,color = color.blue) 
v_arrow = arrow(pos=mater.pos,axis=vec(0,0,0),shaftwidth=0.4*mater.radius ,color = color.red)
a_arrow = arrow(pos=mater.pos,axis=vec(0,0,0),shaftwidth=0.4*mater.radius ,color = color.white)

"""
    3. 執行迴圈
"""

while True:  #執行迴圈
    rate(500)
   

    dist = ((mater.pos.x-earth.pos.x)**2+(mater.pos.y-earth.pos.y)**2+(mater.pos.z-earth.pos.z)**2)**0.5 #距離純量
    radiavector = (mater.pos-earth.pos)/dist #距離單位向量
    Fg_vector = Fg(dist)*radiavector # 萬有引力向量=萬有引力量值*單位向量
    
    v_arrow.pos = mater.pos
    v_arrow.axis = materv*2500
    a_arrow.pos = mater.pos
    a_arrow.axis = Fg_vector/m*5000000

    aT_arrow.pos = mater.pos
    aT_arrow.axis = dot(Fg_vector/m,materv)*(norm(materv)/mag(materv))*5000000
    aN_arrow.pos = mater.pos
    aN_arrow.axis = (mag(cross(Fg_vector/m,materv))/mag(materv))*cross(norm(materv),vector(0,0,-1))*5000000

    materv += Fg_vector/m*dt   #Δv = F/m *dt
    mater.pos = mater.pos + materv*dt  # S = S0 + v *dt

    t = t+dt



