s = input()
n=len(s)
m = int(input())
score_dict = {}
for _ in range(m):
    a, b = input().split()
    score_dict[a] = int(b)
dp = [0] * (n + 1)

for i in range(n-1,-1,-1):
    dp[i]=dp[i+1]+1
    for j in range(i+1,n+1):
        if s[i:j] in score_dict:
            dp[i]=max(dp[i],score_dict[s[i:j]]+dp[j])
print(max(dp))
