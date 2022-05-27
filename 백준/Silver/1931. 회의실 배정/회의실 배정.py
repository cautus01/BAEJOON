import sys
input=sys.stdin.readline

n=int(input())
schedule=[]
answer=0
for _ in range(n):
    a,b=map(int,input().split())
    schedule.append((a,b))
schedule=sorted(schedule,key=lambda x:(x[1],x[0]))
# print(schedule)
start,end=0,0
for x, y in schedule:
    if end<=x:
        start=x
        end=y
        answer+=1
    else:
        continue
print(answer)