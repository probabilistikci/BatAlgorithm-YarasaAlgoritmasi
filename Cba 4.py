# Kaos eklenmiş yarasa algoritması
# r değeri logistic map ile güncellenmektedir.
import math
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')

def amacfonksiyonu(x1,x2):
    return x1**2+x2**2
YarasaSayisi=10;IterasyonSayisi=10000
Fmin=0;Fmax=2;AltLimit=-10;UstLimit=10
V=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
F=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
X1=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
X2=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
A=0.9
r=0.8
Y=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
eniyikonum=[0.0,0.0]
eniyiAFdegeri=0.0
for j in range(10):
    X1[j]=AltLimit+(UstLimit-AltLimit)*random.uniform(0,1)
    X2[j] = AltLimit + (UstLimit - AltLimit) * random.uniform(0, 1)
    Y[j]=amacfonksiyonu(X1[j],X2[j])
    if j==0:
        eniyikonum=[X1[j],X2[j]]
        eniyiAFdegeri=Y[j]
    elif j!=0 and Y[j]<eniyiAFdegeri :
        eniyikonum = [X1[j],X2[j]]
        eniyiAFdegeri=Y[j]
ax.plot(X1,X2,Y,"*" ,c='r',marker='o')
plt.title("Logistic Map \n Caotic Bat Algorithm IV")
plt.show()

t=0
while t<IterasyonSayisi:
    t=t+1
    rnd = random.uniform(0, 1)
    for i in range(YarasaSayisi):
        for z in range(3):
            F[i] = Fmin + (Fmax - Fmin) * random.uniform(0,1)
            if z==0:
                V[i] = V[i] + (X1[i] - eniyikonum[z]) * F[i]
                X1[i] = X1[i] + V[i]
            elif z==1:
                V[i] = V[i] + (X2[i] - eniyikonum[z]) * F[i]
                X2[i] = X2[i] + V[i]
            if X1[i] < (-10):
                X1[i] = -10
            elif X2[i] < (-10):
                X2[i] = -10
            elif X1[i] > 10:
                X1[i] = 10
            elif X2[i] > 10:
                X2[i] = 10


        if rnd>r:
            X1[i]=eniyikonum[0]+random.uniform(-1,1)*A
            X2[i] = eniyikonum[1] + random.uniform(-1, 1) * A


        Y[i]=amacfonksiyonu(X1[i],X2[i])
        if rnd<A and Y[i]<eniyiAFdegeri:
            eniyikonum =[X1[i],X2[i]]
            eniyiAFdegeri = Y[i]
            A = A * 0.9
            r = 4*r*(1-r)
xx=eniyikonum[0]
yy=eniyikonum[1]
zz=(eniyikonum[0]**2)+(eniyikonum[1]**2)
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.plot(X1,X2,Y ,"*",c='b',marker='o')
ax.scatter(xx,yy,zz, c='r')
plt.title("Logistic Map \n Caotic Bat Algorithm IV")
plt.show()

print("A =",A,"r =",r)
print("en iyi konum (x1,x2)=",eniyikonum,"\nen iyi AF değeri =",eniyiAFdegeri)