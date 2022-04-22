from collections import deque
import sys
input=sys.stdin.readline
answer=[]
limit=list(map(int,input().split())) # a,b,c 의 한계
visited=[
    [
        [-1 for _ in range(limit[2]+1)] for _ in range(limit[1]+1)
    ] for _ in range(limit[0]+1)
]
q=deque()
q.append((0,0,limit[2])) # 시작점 넣기
visited[0][0][limit[2]]=0
def move(arr,start,end):
    cur=[arr[0],arr[1],arr[2]]
    if arr[start]+arr[end]<=limit[end]:
        cur[end]=arr[start]+arr[end]
        cur[start]=0
    else:
        cur[end]=limit[end]
        cur[start]-=(limit[end]-arr[end])
    return cur
while q:
    a,b,c=q.popleft()
    if a==0:
        answer.append(c)
    for i in range(3):
        for j in range(3):
            if i==j:
                continue
            water=move([a,b,c],i,j)
            if visited[water[0]][water[1]][water[2]]!=-1:
                continue
            visited[water[0]][water[1]][water[2]]=0
            q.append((water[0],water[1],water[2]))
answer=sorted(answer)
print(*answer)
