#kaos eklenmemiş yarasa algoritması
#Amaç fonksiyonu olarak tek boyutlu rastrigin fonksiyonu kullanıldı.
import math
import RastriginFunction
import random
import matplotlib.pyplot as plt
def amacfonksiyonu(x):
    return 10+x**2-10*math.cos(2*math.pi*x)
YarasaSayisi=10;IterasyonSayisi=20000
Fmin=0;Fmax=2;AltLimit=-5.12;UstLimit=5.12
V=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
F=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
X=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
A=0.9
r=0.1
Y=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
eniyikonum=0.0
eniyiAFdegeri=0.0
for j in range(10):
    X[j]=AltLimit+(UstLimit-AltLimit)*random.uniform(0,1)
    Y[j]=amacfonksiyonu(X[j])
    if j==0:
        eniyikonum=X[j]
        eniyiAFdegeri=Y[j]
    elif j!=0 and Y[j]<eniyiAFdegeri :
        eniyikonum = X[j]
        eniyiAFdegeri=Y[j]
plt.plot(X,Y,"*")
plt.plot(RastriginFunction.x, RastriginFunction.y)
plt.show()
t=0
while t<IterasyonSayisi:
    t=t+1
    rnd = random.uniform(0, 1)
    for i in range(YarasaSayisi):
        F[i] = Fmin + (Fmax - Fmin) * random.uniform(0,1)
        V[i] = V[i] + (X[i] - eniyikonum) * F[i]
        Xi = X[i] + V[i]
        if rnd>r:
            Xi=eniyikonum+random.uniform(-1,1)*A
        if Xi<(-5.12):
            Xi=-5.12
        elif Xi>5.12:
            Xi=5.12
        X[i]=Xi
        Y[i]=amacfonksiyonu(X[i])
        if rnd<A and Y[i]<eniyiAFdegeri:
            eniyikonum = X[i]
            eniyiAFdegeri = Y[i]
            A = A * 0.9
            r =  0.9 * (math.exp(-0.3 * t))

plt.plot(X,Y,"*")
plt.plot(eniyikonum,eniyiAFdegeri,"+",color="red")
plt.plot(RastriginFunction.x, RastriginFunction.y)
plt.show()
print("en iyi konum (x)=",eniyikonum,"\nen iyi AF değeri =",eniyiAFdegeri)