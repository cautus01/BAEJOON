import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[]
def func(start):
    if len(arr)==m:
        print(*arr)
    else:
        for i in range(start,n+1):
            if i==0:
                continue
            arr.append(i)
            func(i)
            arr.pop()
func(1)