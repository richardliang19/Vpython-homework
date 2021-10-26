from vpython import *  #引用視覺畫套件Vpython
"""
    1. 參數設定，設定變數及定義萬有引力公式
"""
G = 6.67*10**(-11) ; M = 6*10**24 ; m = 1000  
Re = 6.4*10**6 ; H = 5*Re ; t = 0 ; dt = 1
def Fg(x):                                 #定義公式
    return -G*M*m/(x**2)


gd = graph(align='left',width=400,height=400,  #設定X-t繪圖視窗
              title='K+U=E', xtitle='t', ytitle='E(red),K(black),U(green)',
              foreground=color.black,background=color.white)
f1 = gcurve(color=color.red)  #定義曲線
f2 = gcurve(color=color.black)  #定義曲線
f3 = gcurve(color=color.green)  #定義曲線
Fe = G*M*m/Re**2 #定義地球表面重力強度



"""
    2. 畫面設定
"""
scene = canvas(align = 'left',title ='4_01_Gravity force',  width=800, height=300, center=vec(0,0,0), background=vec(0.6,0.8,0.8)) #設定視窗
earth = sphere(pos=vec(0,0,0), radius=Re, texture=textures.earth) #放置物件地球
mater = sphere(pos=vec(H,0,0), radius=0.1*Re,color=color.red, make_trail=True) #放置物件衛星
V0= (G*M/H)**0.5
materv=vector(0,0.7*V0,0)
"""
    3. 執行迴圈
"""
while True:  #執行迴圈
    rate(10000)
    dist = ((mater.pos.x-earth.pos.x)**2+(mater.pos.y-earth.pos.y)**2+(mater.pos.z-earth.pos.z)**2)**0.5 #距離純量
    radiavector = (mater.pos-earth.pos)/dist #距離單位向量
    Fg_vector = Fg(dist)*radiavector # 萬有引力向量=萬有引力量值*單位向量
    
    materv += Fg_vector/m*dt   #Δv = F/m *dt
    mater.pos = mater.pos + materv*dt  # S = S0 + v *dt
  
    t = t+dt
    K=0.5*m*(mag(materv))**2
    U=-G*M*m/dist
    f2.plot(pos=(t,K))  
    f3.plot(pos=(t,U))
    f1.plot(pos=(t,K+U))
