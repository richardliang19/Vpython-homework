"""
    建國中學 Vpython物理模擬
    作者: 物理科 賴奕帆老師
    日期: 107/08/31
    特色課程 Lecture 10 
    10_1_3_keyboard_control Practice_Pjojectile motion and boom.py
"""
from vpython import *  #引用視覺畫套件Vpython
g=9.8    ;   size = 0.5  ; m1 =2 ; m2 =4 ; t = 0 ; dt = 0.001
v0 = 20   ;   theta_0 = 60*pi/180   ;   s0 = vector( -25.0, size, 0.0)
J_vector = norm(vector(1,0,0)) #爆炸衝量方向(1,0,0)為水平爆炸
J_mag = 20 #爆炸衝量強度
scene = canvas(title='拋體運動', width=1000, height=600, center=vec(0,10,0),background=vec(0.6,0.8,0.8))#設定畫面
floor = box(length=60, height=0.01, width=4, texture=textures.wood)                  #畫地板
ball1 = sphere(radius = size,  color=color.red, make_trail = True)          #畫球
ball2 = sphere(radius = size,  color=color.green, make_trail = True)          #畫球
ball3 = sphere(radius = 0.01*size,  color=color.black, make_trail = True)          #畫球
ball1.pos = s0    ;  ball1.v = vector(v0*cos(theta_0), v0*sin(theta_0) , 0.0)       #球初速
ball2.pos = s0    ;  ball2.v = vector(v0*cos(theta_0), v0*sin(theta_0) , 0.0)       #球初速
ball3.pos = s0    ;  ball3.v = vector(0, 0 , 0)       #球初速

#設定鍵盤按下a,使start > 0 , 開始拋射
start = 0
def keyinput(evt):       # 呼喚keyboard使用功能
    global start     # 定義鍵盤控制參數
    key_s = {'a' :1.0}
    s = evt.key    #控制鍵盤事件參數
    if s in key_s : start = start + key_s[s]
    ##設定鍵盤按下a,使start > 0 , 開始拋射
    if start > 0:
        ball1.pos += ball1.v*dt
        ball1.v += vector(0,- g*dt,0)
        ball2.pos += ball2.v*dt
        ball2.v += vector(0,- g*dt,0)
        if start > 1.9 and start <2.1:   # 注意，此處衝量J_vector只能施加一次爆炸衝擊。
            ball1.v += J_vector*J_mag/m1      #球1受到向右的衝量
            ball2.v += - J_vector*J_mag/m2    #球2受到向左的衝量
            start = start + 1                 #使衝量只會受到一次
scene.bind('keydown', keyinput)                    # 將鍵盤控制設定綁定於scene視窗  
while ball3.pos.y>=0:       #模擬直到球落地
    rate(500)                   #每一秒跑1000次
    t = t + dt

    ball3.pos = (m1*ball1.pos+m2*ball2.pos)/(m1+m2)  #兩球的質心
    
    ##設定鍵盤按下a,使start > 0 , 開始拋射
    if t >= 0:
        ball1.pos += ball1.v*dt
        ball1.v += vector(0,- g*dt,0)
        ball2.pos += ball2.v*dt
        ball2.v += vector(0,- g*dt,0)
        if ball1.v.y < 0  and start < 1:   # 注意，此處衝量J_vector只能施加一次爆炸衝擊。
            ball1.v += J_vector*J_mag/m1      #球1受到向右的衝量
            ball2.v += - J_vector*J_mag/m2     #球2受到向左的衝量
            start = start + 1                 #使衝量只會受到一次