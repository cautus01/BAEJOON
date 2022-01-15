n=int(input())
t=[]
p=[]
dp=[0]*(n+1)
max_value=0
for _ in range(n):
    a,b=map(int,input().split())
    t.append(a)
    p.append(b)
for i in range(n-1,-1,-1):
    if i+t[i]>n:
        dp[i]=max_value
        continue
    dp[i]=max(p[i]+dp[i+t[i]],max_value)
    max_value=dp[i]
print(max(dp))