from collections import deque
n, k = map(int, input().split())
q = deque(range(1, n+1))
a = []
while(len(q) > 0):
    q.rotate(-(k-1))
    a.append(q.popleft())
print("<", end="")
print(*a, sep=", ", end="")
print(">")