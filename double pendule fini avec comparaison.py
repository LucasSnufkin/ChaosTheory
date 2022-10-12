##Double pendule Euler/Runge-Kutta

from numpy import sin, cos, pi
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

#Constantes du système

G = 9.81
L1 = 0.2
L2 = 0.1
M1 = 0.1592
M2= 0.0778

#Pas et tableau des instants
dt = 0.01
tmax=4.07
t = np.arange(0,tmax, dt)

#Positions initiales
th1 = 0.9818616604
w1 = 1.898311325
th2 = -0.7221496875
w2 = 17.85135868

state =np.array([th1, w1, th2, w2])

#On crée la fonction qui permet de calculer les etats du systemes au differents instants par intégration :

def derivs(state,dt):

    dydx = np.zeros_like(state)
    dydx[0] = state[1]

    delta = state[2] - state[0]
    den1 = (M1+M2) * L1 - M2 * L1 * cos(delta) * cos(delta)
    dydx[1] = ((M2 * L1 * state[1] * state[1] * sin(delta) * cos(delta)
                + M2 * G * sin(state[2]) * cos(delta)
                + M2 * L2 * state[3] * state[3] * sin(delta)
                - (M1+M2) * G * sin(state[0]))
               / den1)

    dydx[2] = state[3]

    den2 = (L2/L1) * den1
    dydx[3] = ((- M2 * L2 * state[3] * state[3] * sin(delta) * cos(delta)
                + (M1+M2) * G * sin(state[0]) * cos(delta)
                - (M1+M2) * L1 * state[1] * state[1] * sin(delta)
                - (M1+M2) * G * sin(state[2]))
               / den2)

    return dydx

#Méthode d'Euler :

def suivant(state,dt):
    newState=mult(derivs(state,dt),dt)+state
    return newState

def mult (tab,x):
    for k in range (np.size(tab)):
        tab[k]*=x
    return tab

def calculEuler(state,dt,tmax):
    tab=[state]
    t=0
    for k in range (int(tmax//dt)-1):
        tab.append((suivant(tab[k],dt)))
    return tab



Euler=np.array(calculEuler(state,dt,tmax))

teta1=Euler[:, 0]
teta2=Euler[:, 2]
dteta1=Euler[:, 1]
dteta2=Euler[:, 3]


x1 = L1*sin(teta1)
y1 = -L1*cos(teta1)
x2 = L2*sin(teta2) + x1
y2 = -L2*cos(teta2) + y1

#On trace les trajectoires du premier pendule pour la méthode d'Euler :

plt.subplot(211)
plt.plot(t,x1,label='x')
plt.plot(t,-y1,label='y')
plt.title("Comparaison méthode d'Euler/méthode de Runge-Kutta")
plt.ylabel("x(t),y(t) Euler")
plt.legend()


#On utilise la méthode de Runge Kutta d'ordre 4 implémentée dans Scipy :

RK=integrate.odeint(derivs,state,t)

rk_teta1=RK[:, 0]
rk_teta2=RK[:, 2]
rk_dteta1=RK[:, 1]
rk_dteta2=RK[:, 3]

rk_x1 = L1*sin(rk_teta1)
rk_y1 = -L1*cos(rk_teta1)
rk_x2 = L2*sin(rk_teta2) + rk_x1
rk_y2 = -L2*cos(rk_teta2) + rk_y1

#On trace les trajectoires du premier pendule pour la méthode de Runge-Kutta :
plt.subplot(212)
plt.plot(t,rk_x1,label='x')
plt.plot(t,-rk_y1,label='y')
plt.xlabel("temps")
plt.ylabel("x(t),y(t) Runge-Kutta")
plt.legend()
plt.show()


##Comparaison deux pendules proches

th1 = -0.198
w1 = 5.6912
th2 = 0.8992
w2 = -6.111

th1p = -0.198
w1p = 5.6912
th2p = 0.87
w2p = -6.111



state =np.array([th1, w1, th2, w2])
statep =np.array([th1p,w1p,th2p,w2p])

#Euler
Euler=np.array(calculEuler(state,dt,tmax))

teta1=Euler[:, 0]
teta2=Euler[:, 2]
dteta1=Euler[:, 1]
dteta2=Euler[:, 3]

Eulerp=np.array(calculEuler(statep,dt,tmax))

teta1p = Eulerp[:, 0]
teta2p = Eulerp[:, 2]
dteta1p = Eulerp[:, 1]
dteta2p = Eulerp[:, 3]

#Runge Kutta
RK = integrate.odeint(derivs,state,t)

rk_teta1 = RK[:, 0]
rk_teta2 = RK[:, 2]
rk_dteta1 = RK[:, 1]
rk_dteta2 = RK[:, 3]

RKp = integrate.odeint(derivs,statep,t)

rk_teta1p = RKp[:, 0]
rk_teta2p = RKp[:, 2]
rk_dteta1p = RKp[:, 1]
rk_dteta2p = RKp[:, 3]

#Plot d'Euler
plt.subplot(211)
plt.plot(t,teta1,label='theta1')
plt.plot(t,teta2,label='theta2')
plt.title("Comparaison deux etats proches à l'aide d'Euler")
plt.ylabel("theta1(t),theta2(t)")
plt.legend()

plt.subplot(212)
plt.plot(t,teta1p,label='theta1')
plt.plot(t,teta2p,label='theta2')
plt.ylabel("theta1(t),theta2(t)")
plt.legend()
plt.show()

#Plot de Runge Kutta
plt.subplot(211)
plt.plot(t,rk_teta1,label='theta1')
plt.plot(t,rk_teta2,label='theta2')
plt.title("Comparaison deux etats proches à l'aide de RK")
plt.ylabel("theta1(t),theta2(t)")
plt.legend()

plt.subplot(212)
plt.plot(t,rk_teta1p,label='theta1')
plt.plot(t,rk_teta2p,label='theta2')
plt.ylabel("theta1(t),theta2(t)")
plt.legend()
plt.show()