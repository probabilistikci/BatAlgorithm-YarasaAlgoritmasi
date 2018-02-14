import math
import random
def amacfonksiyonu(x):
    return (x[0])**2+(x[1])**2+(x[2])**2+(x[3])**2+(x[4])**2
YarasaSayisi=10;IterasyonSayisi=25000;Fmin=0;Fmax=2
AltLimit=-10;UstLimit=10
V=[];F=[]
X=[[],[],[],[],[],[],[],[],[],[]]
A=0.9
r=0.8;EnIyiCozum=0.0
for j in range(YarasaSayisi):
    for b in range(5):#Boyut Sayısı
        X[j].append(AltLimit+(UstLimit-AltLimit)*random.uniform(0,1))
    F.append(Fmin + (Fmax - Fmin) * random.uniform(0, 1))
    V.append(0.0)#ilk hızlar sıfır alındı
    MevcutCozum=amacfonksiyonu(X[j])
    if j==0:
        EnIyiCozum=MevcutCozum
        EnIyiKonum=X[j]
    elif j!=0 and amacfonksiyonu(X[j])<MevcutCozum:
        EnIyiCozum=MevcutCozum
        EnIyiKonum=X[j]
t=0;  kaos=0.85
while t<IterasyonSayisi:
    t=t+1
    for i in range(YarasaSayisi):
        F[i] = Fmin + (Fmax - Fmin) * random.uniform(0, 1)*kaos
        kaos = math.sin((random.uniform(0, 1) * math.pi) / kaos)
        for b in range(5):
            V[i] = V[i] + (X[i][b] - EnIyiKonum[b]) * F[i]
            X[i][b] = X[i][b] + V[i]
        rnd=random.uniform(0,1)
        if rnd>r:
            for b in range(5):
                X[i][b] =  min(EnIyiKonum) + random.uniform(-1, 1) * A
        for b in range(5):
            if  X[i][b]<-10:
                X[i][b] =-10
            elif  X[i][b]>10:
                X[i][b]=10
        MevcutCozum=amacfonksiyonu(X[i])
        if rnd<A and MevcutCozum<EnIyiCozum:
            EnIyiKonum =X[i]
            EnIyiCozum = MevcutCozum
            A = A * 0.9
            r = 0.9 * (math.exp(-0.3 * t))
            print("t =",t,"yarasa =",i,"\n","en iyi konum =", EnIyiKonum, "\nen iyi Çözüm =", EnIyiCozum,"\n")