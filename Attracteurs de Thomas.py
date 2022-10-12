## Attracteurs de Thomas


import matplotlib.pyplot as plt
import random
import math
fig = plt.figure()
from mpl_toolkits.mplot3d import Axes3D
ax = fig.add_subplot(projection='3d')

#Constante du système
b=0.20

dt=0.01
tmax=50

def suivant(x,y,z,dt):
    dx=math.sin(y)-b*x
    dy=math.sin(z)-b*y
    dz=math.sin(x)-b*z
    nx=dx*dt+x
    ny=dy*dt+y
    nz=dz*dt+z
    return(nx,ny,nz)

def resolution(x0,y0,z0,dt,tmax):
    Reponse=[(x0,y0,z0)]
    t=0
    i=0
    while t<tmax:
        x,y,z=Reponse[i]
        nx,ny,nz=suivant(x,y,z,dt)
        Reponse.append((nx,ny,nz))
        t+=dt
        i+=1
    return (Reponse)

def separation(l):
    l1=[]
    l2=[]
    l3=[]
    for p in l:
        l1.append(p[0])
        l2.append(p[1])
        l3.append(p[2])
    return (l1,l2,l3)

def alea(n):
    for k in range (n):
        x=random.uniform(-2, 2)
        y=random.uniform(-2, 2)
        z=random.uniform(-2,2)
        xs,ys,zs=separation(resolution(x,y,z,dt,tmax))
        ax.plot(xs, ys, zs)
alea(20)


axes=plt.gca()
axes.set_xlim(-5,5)
axes.set_ylim(-5,5)
axes.set_zlim(-5,5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()