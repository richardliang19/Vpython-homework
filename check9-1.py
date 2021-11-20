"""
    建國中學 Vpython物理模擬
    作者: 物理科 賴奕帆老師
    日期: 107/08/25
    特色課程 Lecture 09 List的練習_萬有引力_球與圓環的SHM
    9_01_SHM_Circle and Ball_Fg.py
"""
from vpython import *  #引用視覺畫套件Vpython
"""
    1. 參數設定
"""
G=2000  #重力常數
M=1.0     #紅球質量(圓環質量為360*M)
m=1.0     #綠球質量
dt = 0.001          
t = 0
R = 10     #圓環半徑
"""
    2. 畫面設定
"""
scene = canvas(width=1000, height=600, background=vec(0.6,0.8,0.8),range = 0.9*R)
scene.center = vec(0,0,0)					#設定視窗中心點
ball = sphere(pos=vector(0,0,0), radius = 0.5, color=color.green, v = vec(0,0,0), make_trail = True)

#  利用List畫出360顆小球代表圓環
balllist = []  

for N in range(-3,4,1):
    for M in range(-3,4,1):
        for K in range(-3,4,1):
            balllist.append(sphere(pos=vector(N*0.1*R,M*0.1*R,K*0.1*R), radius = 0.1, color=color.red))
"""
    3. 執行迴圈
"""
while True:
    rate (1000)

    t = t+dt
    ball.pos = ball.pos