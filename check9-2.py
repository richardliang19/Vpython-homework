"""
    建國中學 Vpython物理模擬
    作者: 物理科 賴奕帆老師
    日期: 107/08/25
    特色課程 Lecture 09 List的練習_重力場與電場
    9_01_Gravity force field.py
"""
from vpython import *  #引用視覺畫套件Vpython
"""
    1. 參數設定
"""
G = 6.67 ; M = 6*10**1 ; Re = 10 ; t = 0 ; dt = 0.001
"""
    2. 畫面設定
"""
def ag(x):   #定義重力場公式
    return -G*M/(x**2)

scene = canvas(width=1000, height=800, center=vec(0,0,0),background=vec(0.6,0.8,0.8),range=6*Re)
earth = sphere(pos=vec(0,0,0), radius=Re, texture=textures.earth)

arrowlist = []  #定義箭頭放置的List
for N1 in range(-5,6,1): #X軸
  for N2 in range(-5,6,1):#Y軸
      for N3 in range(-5,6,1):#Z軸
            arrowlist.append(arrow(pos=vector(N1*Re,N2*Re,N3*Re),axis=vector(5,0,0),shaftwidth=1 , color=color.red))

for N in arrowlist:
  N_dist = mag(N.pos - earth.pos)  #計算每個箭頭與地球間的距離純量
  N_radiavector = norm(N.pos-earth.pos) #計算每個箭頭與地球間的距離單位向量
  if N_dist > 1.2*Re and N_dist < 5*Re:
    N.axis = ag(N_dist) * N_radiavector * 10
  else: N.axis = vector(0,0,0)
"""
    3. 執行迴圈
"""
while True:
    rate(1000)