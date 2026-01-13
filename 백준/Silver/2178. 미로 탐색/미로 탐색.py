import sys
from collections import deque

def func(x, y):
    que = deque()
    que.append((y, x, 1))
    while(que):
        y, x, t = que.popleft()
        if (x == m and y == n):
            print(t)
            sys.exit()
        
        if (maze[y][x-1] and visited[y][x-1] == False):
            visited[y][x-1] = True
            que.append((y, x-1, t+1))
        if (maze[y][x+1] and visited[y][x+1] == False):
            visited[y][x+1] = True
            que.append((y, x+1, t+1))
        if (maze[y-1][x] and visited[y-1][x] == False):
            visited[y-1][x] = True
            que.append((y-1, x, t+1))
        if (maze[y+1][x] and visited[y+1][x] == False):
            visited[y+1][x] = True
            que.append((y+1, x, t+1))

n, m = map(int, input().split())
maze = [[0] * (m+2) for _ in range (n+2)]
visited = [[False] * (m+2) for _ in range (n+2)]

maze = [[0] * (m + 2)]
for _ in range(n):
    line = [0] + list(map(int, input().strip())) + [0]
    maze.append(line)
maze.append([0] * (m + 2))

func(1, 1)