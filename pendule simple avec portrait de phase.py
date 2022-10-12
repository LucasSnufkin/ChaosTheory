import math
import matplotlib.pyplot as plt

g=9.81

#Résolution de manière analytique, on reconnaît un oscillateur harmonique :
def teta(t,tetai,dtetai,longueur):
    return (tetai*math.cos(math.sqrt(g/longueur)*t)+dtetai*math.sqrt(longueur/g)*math.sin(math.sqrt(g/longueur)*t))

def dteta(t,tetai,dtetai,longueur):
    return (-tetai*math.sqrt(g/longueur)*math.sin(math.sqrt(g/longueur)*t)+dtetai*math.cos(math.sqrt(g/longueur)*t))

#On partitionne [0;tempsfinal] en prenant un point tout les dt :
def pendulesimple(tetai,dtetai,dt,tempsfinal,longueur):
    Reponse=[(tetai,dtetai)]
    t=0
    while t < tempsfinal:
        Reponse.append((teta(t,tetai,dtetai,longueur),dteta(t,tetai,dtetai,longueur)))
        t+= dt
    return Reponse

#On récupère séparément la liste des angles au cours du temps et de leur dérivé
def separation(l):
    lon= len(l)
    L1=[]
    L2=[]
    for i in range (lon):
        L1.append(l[i][0])
        L2.append(l[i][1])
    return (L1,L2)

longueur=5
pendule=pendulesimple(0.8,0,0.1,20,longueur)
(teta,dteta)=separation(pendule)

#On passe en coordonnées :
def transformation (Liste,l=longueur):
    ReponseX=[]
    ReponseY=[]
    for i in range (len(Liste)):
        Teta=Liste[i][0]
        ReponseX.append(l*math.sin(Teta))
        ReponseY.append(-l*math.cos(Teta))
    return ReponseX,ReponseY

Xliste,Yliste=transformation(pendule)
plt.plot(Xliste,Yliste)
axes=plt.gca()
axes.set_xlim(-4,4)
axes.set_ylim(-8,0)
plt.show()

plt.plot(teta,dteta)
axes=plt.gca()
axes.set_xlim(-1.2,1.2)
axes.set_ylim(-1.2,1.2)
plt.show()


