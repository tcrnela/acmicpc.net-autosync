import sys
import heapq
input = sys.stdin.readline

def djk(k):
    global ans
    que = []
    heapq.heappush(que, (ans[k], k))
    while(que):
        t = heapq.heappop(que)
        k = t[1]
        for node in grp[k]:
            if (ans[node[0]] > node[1] + ans[k]):
                ans[node[0]] = node[1] + ans[k]
                heapq.heappush(que, (node[1]+ans[k], node[0]))

v, e = map(int, input().split())
INF = float("inf")
grp = [[] for _ in range (v+1)]
ans = [INF] * (v+1)
k = int(input())
ans[k] = 0

for _ in range(e):
    a, b, c = map(int, input().split())
    grp[a].append([b, c])

djk(k)
for i in range (1, v+1):
    print("INF" if ans[i] == INF else ans[i])