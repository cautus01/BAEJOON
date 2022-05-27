import sys
input=sys.stdin.readline

n=int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
max_value=0
for i in range(n):
    if max_value<arr[i]*(i+1):
        max_value=arr[i]*(i+1)
print(max_value)