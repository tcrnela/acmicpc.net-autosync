n, m = map(int, input().split())
a = []
b = []
ans = 0

for _ in range (m):
    q, w = map(int, input().split())
    a.append(q)
    b.append(w)
a.sort()
b.sort()

while(n > 0):
    if (n >= 6):
        t = b[0]*6
        ans += min(a[0], b[0]*6)
        n -= 6
    else:
        ans += min(a[0], b[0]*n)
        n = 0
print(ans)