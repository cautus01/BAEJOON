import sys
from itertools import combinations_with_replacement
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[i for i in range(1,n+1)]
for com in list(combinations_with_replacement(arr,m)):
    print(*sorted(list(com)))