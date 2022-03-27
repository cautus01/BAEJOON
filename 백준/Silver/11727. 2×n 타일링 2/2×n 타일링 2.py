d=[0]*1005

d[1]=1
d[2]=3
n=int(input())
for i in range(3,n+1):
    d[i]=(d[i-1]+2*d[i-2])%10007
print(d[n])