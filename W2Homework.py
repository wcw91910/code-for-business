amount=int(input())
a0=1000-amount
a=a0//500
b0=a0%500
b=b0//100
c0=b0%100
c=c0//50
d0=c0%50
d=d0//10
e0=d0%10
e=e0//5
f0=e0%5
f=f0//1
print(a,b,c,d,e,f,sep=" ")