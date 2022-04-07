import sys
from itertools import permutations
input=sys.stdin.readline

n,m=map(int,input().split())
data=sorted(list(map(int,input().split())))
for com in list(permutations(data,m)):
    print(*list(com))