import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    visited = [False] * (n+1)
    visited[1] = True
    que = deque()
    que.append(1)
    ans = [0] * (n+1)

    while(que):
        t = que.popleft()
        for j in grp[t]:
            if (visited[j] == False):
                ans[j] = t
                visited[j] = True
                que.append(j)
    for i in range (2, n+1):
        print(ans[i])    

n = int(input())
grp = [[] for _ in range (n+1)]

for _ in range (n-1):
    a, b = map(int, input().split())
    grp[a].append(b)
    grp[b].append(a)

bfs()