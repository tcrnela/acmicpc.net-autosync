import sys
sys.setrecursionlimit(10**6)

def func(n):
    if(dp[n] == -1):
        dp[n] = max(a[n] + func(n-3) + a[n-1], a[n] + func(n-2))
    return dp[n] 

n = int(input())
dp = [-1] * (n+2)
a = [0] * (n+2)
for i in range (1, n+1):
    a[i] = int(input())

dp[0] = 0
dp[1] = a[1]
dp[2] = a[1] + a[2]
print(func(n))