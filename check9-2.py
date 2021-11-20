
from vpython import * 

G = 6.67 ; M = 6*10**1 ; Re = 10 ; t = 0 ; dt = 0.001

def ag(x):   
    return -G*M/(x**2)

scene = canvas(width=1000, height=800, center=vec(0,0,0),background=vec(0.6,0.8,0.8),range=6*Re)
earth = sphere(pos=vec(0,0,0), radius=Re, texture=textures.earth)

arrowlist = []  
for N1 in range(-5,6,1): 
  for N2 in range(-5,6,1):
      for N3 in range(-5,6,1):
            arrowlist.append(arrow(pos=vector(N1*Re,N2*Re,N3*Re),axis=vector(5,0,0),shaftwidth=1 , color=color.red))

for N in arrowlist:
  N_dist = mag(N.pos - earth.pos)  
  N_radiavector = norm(N.pos-earth.pos) 
  if N_dist > 1.2*Re and N_dist < 5*Re:
    N.axis = ag(N_dist) * N_radiavector * 10
  else: N.axis = vector(0,0,0)

while True:
    rate(1000)