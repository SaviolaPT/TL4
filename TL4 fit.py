import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
def readtabela(tabela):
    """_summary_

    Args:
        file (_type_): _description_
    """
    file1=open(tabela, "r")
    texto=file1.readlines()
    Tempos=[]
    Velocidades=[]
    for i in texto:
        Tempos.append(float(i.split(" ")[0]))
        Velocidades.append(float(i.split(" ")[1]))
    return Tempos, Velocidades
def v(t,v0,l,a):
    """_summary_

    Args:
        t (_type_): _description_
        v0 (_type_): _description_
        l (_type_): _description_
        a (_type_): _description_
    """
    return v0*np.exp(-t*l)-a*t

tabela="I010A.txt"
t,vel=readtabela(tabela)
v0,l,a=curve_fit(v,t,vel,bounds=[0,[0.9,0.02,0.08]])[0][0],curve_fit(v,t,vel,bounds=[0,[0.9,0.02,0.08]])[0][1],curve_fit(v,t,vel,bounds=[0,[0.9,0.02,0.08]])[0][2]


x=np.linspace(t[0],t[-1],1000)
y=[]
for i in x:
    y.append(v(i,v0,l,a))
fig1= plt.figure(1)
plt.scatter(t,vel,color="green",marker="x")
plt.plot(x,y,color="orange",marker=" ")
plt.title("Ajuste aos dados para I=0,10A")
plt.xlabel("Tempo(s)")
plt.ylabel("Velocidade máxima (m/s)")
plt.grid()
fig1.show()
fig1.savefig("python I010A.pdf")

tabela="I025A.txt"
t,vel=readtabela(tabela)
v0,l,a=curve_fit(v,t,vel,bounds=[0,[0.9,0.09,0.09]])[0][0],curve_fit(v,t,vel,bounds=[0,[0.9,0.09,0.09]])[0][1],curve_fit(v,t,vel,bounds=[0,[0.9,0.09,0.09]])[0][2]
x=np.linspace(t[0],t[-1],1000)
y=[]
for i in x:
    y.append(v(i,v0,l,a))   
fig2= plt.figure(2)
plt.scatter(t,vel,color="green",marker="x")
plt.plot(x,y,color="orange",marker=" ")
plt.title("Ajuste aos dados para I=0,25A")
plt.xlabel("Tempo(s)")
plt.ylabel("Velocidade máxima (m/s)")
plt.grid()
fig2.show()
fig2.savefig("python I025A.pdf")

tabela="I035A.txt"
t,vel=readtabela(tabela)
v0,l,a=curve_fit(v,t,vel,bounds=[0,[0.9,0.3,0.09]])[0][0],curve_fit(v,t,vel,bounds=[0,[0.9,0.3,0.09]])[0][1],curve_fit(v,t,vel,bounds=[0,[0.9,0.3,0.09]])[0][2]
x=np.linspace(t[0],t[-1],1000)
y=[]
for i in x:
    y.append(v(i,v0,l,a))
fig3= plt.figure(3)
plt.scatter(t,vel,color="green",marker="x")
plt.plot(x,y,color="orange",marker=" ")
plt.title("Ajuste aos dados para I=0,35A")
plt.xlabel("Tempo(s)")
plt.ylabel("Velocidade máxima (m/s)")
plt.grid()
fig3.show()
fig3.savefig("python I035A.pdf")

tabela="I050A.txt"
t,vel=readtabela(tabela)
v0,l,a=curve_fit(v,t,vel,bounds=[0,[0.9,0.33,0.09]])[0][0],curve_fit(v,t,vel,bounds=[0,[0.9,0.33,0.09]])[0][1],curve_fit(v,t,vel,bounds=[0,[0.9,0.33,0.09]])[0][2]
x=np.linspace(t[0],t[-1],1000)
y=[]
for i in x:
    y.append(v(i,v0,l,a))
fig4= plt.figure(4)
plt.scatter(t,vel,color="green",marker="x")
plt.plot(x,y,color="orange",marker=" ")
plt.title("Ajuste aos dados para I=0,50A")
plt.xlabel("Tempo(s)")
plt.ylabel("Velocidade máxima (m/s)")
plt.grid()
fig4.show()
fig4.savefig("python I050A.pdf")
