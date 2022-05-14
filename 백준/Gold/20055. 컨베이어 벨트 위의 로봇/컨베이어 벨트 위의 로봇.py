import sys
from collections import deque
input=sys.stdin.readline

n,k=map(int,input().split())
arr=list(map(int,input().split()))
arr=deque(arr)
robot=[0]*(2*n)
robot=deque(robot)
answer=1 # 단계

while True:
    arr.rotate(1)
    robot.rotate(1)
    if robot[n-1]==1: # 로봇을 내린다.
        robot[n-1]=0
    for i in range(n-2,-1,-1):
        if robot[i]==1 and robot[i+1]==0 and arr[i+1]>0:
        # 로봇이 있고 그 다음 칸에 로봇이 없으며 칸의 내구도가 0보다 크다면
            robot[i],robot[i+1]=0,1
            arr[i+1]-=1
    if robot[n - 1] == 1:  # 로봇을 내린다.
        robot[n - 1] = 0
    if arr[0]!=0:
        robot[0]=1
        arr[0]-=1
    count=0
    for i in range(len(arr)):
        if arr[i]==0:
            count+=1
    if count>=k:
        break
    answer+=1
print(answer)