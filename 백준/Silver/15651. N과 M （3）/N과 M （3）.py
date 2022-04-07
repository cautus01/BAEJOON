from itertools import product

n,m=map(int,input().split())
arr=[i for i in range(1,n+1)]
data=list(product(arr,repeat=m))
for a in data:
    print(*a)