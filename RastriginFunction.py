import math
x=[];y=[]
k=-5.12
while k<=5.12:
    x.append(k)
    sonuc=10+k**2-10*math.cos(2*math.pi*k)
    y.append(sonuc)
    k+=0.01