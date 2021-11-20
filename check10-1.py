"""
    建國中學 Vpython物理模擬
    作者: 物理科 賴奕帆老師
    日期: 107/08/31
    特色課程 Lecture 10 
    10_1_2_keyboard_control Practice_Circle_Motion with velocity and acceleration.py
"""
from vpython import *  #引用視覺畫套件Vpython


R = 20                #圓周半徑
B_r = 0.1*R           #球的半徑
theta = 0*pi/180      #轉動初始角度
w = 1                 #轉動角速度
t=0
dt = 0.001            #時間間隔 0.001 秒

scene = canvas(width=1000, height=800, center = vec(0,0,0), background=vec(0.3,0.4,0.4), forward=vec(0,0,-1),range=60) #設定畫面

ball = sphere(radius = B_r , color=color.yellow, make_trail= True, interval=100) #畫球
ball.pos = vector( R*cos(theta), R*sin(theta), 0) #球初始位置
ball.v = vector( 0, 0, 0) #球初速 

v_arrow = arrow(pos=ball.pos,axis=vec(0,0,0),shaftwidth=0.2*B_r ,color = color.red)  #速度箭頭
a_arrow = arrow(pos=ball.pos,axis=vec(0,0,0),shaftwidth=0.2*B_r ,color = color.white)  #加速度箭頭

def keyinput(evt):                                                           # keyboard interrupt callback function
    global R, w     # define the global variables that you want to change by this function
    length = {'q' :0.2, 'w' : -0.2}
    angle_v = {'a' : 0.1, 's': -0.1}
    
    s = evt.key
    if s in length : R = R + length[s]
    if s in angle_v: w = w + angle_v[s]
scene.bind('keydown', keyinput)  

while True :             
    rate(1000)     #每一秒跑 1000 次
    
    theta = theta + w * dt          
    ball.pos = vector (R*cos(theta), R*sin(theta), 0 )

    v_arrow.pos = ball.pos
    v_arrow.axis = cross(vector(0,0,1),ball.pos).norm() * R * w
    a_arrow.pos = ball.pos
    a_arrow.axis = - ball.pos.norm() * R * w * w

    t = t + dt