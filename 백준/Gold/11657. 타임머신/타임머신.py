import sys

n, m = map(int, input().split())
INF = float("inf")
arr = []
for i in range (m):
    a, b, c = map(int, input().split())
    arr.append((a, b, c))

ans = [INF] * (n + 1)
ans[1] = 0

for k in range (1, n):
    for j in range (m):
        if (ans[arr[j][0]] == INF):
            continue
        if (ans[arr[j][1]] > arr[j][2] + ans[arr[j][0]]):
            ans[arr[j][1]] = arr[j][2] + ans[arr[j][0]]

for j in range (m):
    if (ans[arr[j][0]] == INF):
        continue
    if (ans[arr[j][1]] > arr[j][2] + ans[arr[j][0]]):
        print(-1)
        sys.exit()

for i in range (2, n+1):
    print("-1" if ans[i] == INF else ans[i])