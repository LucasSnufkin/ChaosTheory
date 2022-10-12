import matplotlib.pyplot as plt
import random
import math
fig = plt.figure()
from mpl_toolkits.mplot3d import Axes3D
ax = fig.add_subplot(projection='3d')

#Constante du système
sigma=10
beta=8/3
ro=24

#Point fixe au centre des attracteurs
xat1=-math.sqrt(beta*(ro-1))
yat1=xat1
xat2=math.sqrt(beta*(ro-1))
yat2=xat2
zat=ro-1

dt=0.01
tmax=10

Lf=[]

#On crée la fonction qui permet de calculer les etats du systemes au differents instants par intégration :

def suivant(x,y,z,dt):
    dx=sigma*(y-x)
    dy=ro*x-y-x*z
    dz=x*y-beta*z
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

#On definit une fonction qui separe une liste de 3 listes en 3 listes distinctes
def separation(l):
    l1=[]
    l2=[]
    l3=[]
    for p in l:
        l1.append(p[0])
        l2.append(p[1])
        l3.append(p[2])
    return (l1,l2,l3)

#On definit deux fonctions qui permettent de calculer le temps pour lequel une trajectoire est plus d'un point fixe que de l'autre
def distance (x,y,z,x1,y1,z1):
    return math.sqrt((x-x1)**2+(y-y1)**2+(z-z1)**2)


def tempspasse(x,y,z):
    L=[0,0]
    for i in range (len(x)):
        at1=distance(xat1,yat1,zat,x[i],y[i],z[i])
        at2=distance(xat2,yat2,zat,x[i],y[i],z[i])
        if at1<at2:
            L[0]+=1
        else :
            L[1]+=1
    return L

#On crée une fonction permettant de lancer une simulation de n trajectoires dont les conditions initiales sont aléatoires

def alea(n):
    for k in range (n):
        x=random.uniform(-20, 20)
        y=random.uniform(-20, 20)
        z=random.uniform(-20, 20)
        xs,ys,zs=separation(resolution(x,y,z,dt,tmax))
        Lf.append(tempspasse(xs,ys,zs))
        ax.plot(xs, ys, zs)
alea(50)

#On calcule la moyenne du temps passé proche d'un point attracteur pour toutes trajectoires
def moyenne(L):
    s=0
    f=0
    for p in L:
        s+=p[0]
        f+=p[1]
    return (s/len(L),f/len(L))

def ecarttype (L):
    (m1,m2)=moyenne(L)
    s=0
    f=0
    n=len(L)
    for p in L :
        s+=(m1-p[0])**2
        f+=(m2-p[1])**2
    return (math.sqrt(s/n),math.sqrt(f/n))


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
(moy1,moy2)=moyenne(Lf)
(eca1,eca2)=ecarttype(Lf)
print("dt =",dt,"tmax=",tmax)
print("moyenne =",(moy1*dt,moy2*dt))
print("Ecart-type=",(eca1*dt,eca2*dt))
plt.show()