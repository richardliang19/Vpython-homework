from vpython import *  

G = 6.67 ; M = 6*10**1 ; Re = 10 ; t =0 ; dt = 0.001

by = 1 # touch this close to tail or tip
drag = None # have not selected tail or tip of arrow
drag_pos = vector (0,0,0)
new_pos = vector (0,0,0)

def ag(x):
    return -G*M/(x**2)

scene = canvas(width=1000, height=800, center=vec(0,-5,0),
                background=vec(0.6,0.8,0.8),range=6*Re)
earth = sphere(pos=vec(0,0,0), radius=Re, texture=textures.earth)

arrowlist = []
for N1 in range(-5,6,1): 
  for N2 in range(-5,6,1):
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

    m_ev = scene.waitfor('click mousedown mouseup mousemove')  
    if m_ev.event == 'mousedown': 
        if mag(arr.pos-m_ev.pos) <= by: 
            drag = 'tail' # near tail of arrow
        elif mag((arr.pos+arr.axis)-m_ev.pos) <= by: 
            drag = 'tip' # near tip of arrow
            drag_pos = m_ev.pos # save press location 
    elif m_ev.event == 'mouseup': # released at end of drag
        drag = None # end dragging (None is False) 

    if drag: 
        new_pos = m_ev.pos 
        if new_pos != drag_pos: # if mouse has moved
            displace = new_pos - drag_pos # how far 
            drag_pos = new_pos # update drag position           
            if drag == 'tail': 
                arr.pos = m_ev.pos # displace the tail
            if drag == 'tip': 
                arr.axis += displace # displace the tip