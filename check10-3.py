"""
    建國中學 Vpython物理模擬
    作者: 物理科 賴奕帆老師
    特色課程 Lecture 10 
    10_2_3 mouse control Practice_Gravity force.py
"""
from vpython import *  #引用視覺畫套件Vpython

G = 6.67 ; M = 6*10**1 ; Re = 10 ; t =0 ; dt = 0.001

by = 1 # touch this close to tail or tip, 滑鼠按下後與尾與箭頭的判斷距離
drag = None # have not selected tail or tip of arrow, 判斷是否選擇了尾與箭頭
drag_pos = vector (0,0,0)
new_pos = vector (0,0,0)

def ag(x):
    return -G*M/(x**2)

scene = canvas(width=1000, height=800, center=vec(0,-5,0),
                background=vec(0.6,0.8,0.8),range=6*Re)
earth = sphere(pos=vec(0,0,0), radius=Re, texture=textures.earth)

arrowlist = []
for N1 in range(-5,6,1): #X軸
  for N2 in range(-5,6,1):#Y軸
    arrowlist.append(arrow(pos=vector(N1*Re,N2*Re,0),axis=vector(5,0,0),shaftwidth=1 , color=color.red))

arr = arrow(pos=vector(12.5,12.5,0),axis=vector(5,0,0),shaftwidth=1 , color=color.blue)

for N in arrowlist:
  N_dist = mag(N.pos - earth.pos)
  N_radiavector = norm(N.pos-earth.pos)
  if N_dist > 1.2*Re and N_dist < 5*Re:
    N.axis = ag(N_dist) * N_radiavector * 10
  else: N.axis = vector(0,0,0)

    
while True:
    rate(1000)
    arr_dist = mag(arr.pos - earth.pos)
    arr_radiavector = norm(arr.pos - earth.pos)
    if arr_dist > 1.0*Re :
      arr.axis = ag(arr_dist) * arr_radiavector * 10
    else: arr.axis = vector(0,0,0)

    m_ev = scene.waitfor('click mousedown mouseup mousemove')  #滑鼠event
    if m_ev.event == 'mousedown':  #如果滑鼠按下左鍵
        if mag(arr.pos-m_ev.pos) <= by: #若滑鼠位置與尾端的位置差小於by
            drag = 'tail' # near tail of arrow, 則判斷正在拖曳tail(尾)
        elif mag((arr.pos+arr.axis)-m_ev.pos) <= by: #若滑鼠位置與箭頭的位置差小於by
            drag = 'tip' # near tip of arrow, 則判斷正在拖曳tip(箭頭)
            drag_pos = m_ev.pos # save press location , 紀錄按下的位置於drag_pos(注意，此時滑鼠左鍵持續按著, 可拖曳)
    elif m_ev.event == 'mouseup': # released at end of drag, 若滑鼠左鍵放開
        drag = None # end dragging (None is False) , 則判斷停者拖曳  

    if drag: #如果滑鼠正在按下拖曳tail or tip)
        new_pos = m_ev.pos #把目前滑鼠的位置紀錄於new_pos
        if new_pos != drag_pos: # if mouse has moved, 如果滑鼠拖曳了, 導致目前滑鼠的位置與之前紀錄的位置不一樣
            displace = new_pos - drag_pos # how far , 則計算滑鼠移動了多少距離
            drag_pos = new_pos # update drag position, 並更新drag_pos於目前的滑鼠位置            
            if drag == 'tail': #如果判斷指令為tail(尾)
                arr.pos = m_ev.pos # displace the tail, 則更新尾巴的位置
            if drag == 'tip': #如果判斷指令為tip(箭頭)
                arr.axis += displace # displace the tip, 則更新向量的長度