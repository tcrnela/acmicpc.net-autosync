import sys

n = int(input())
c5 = c2 = 0
t = n

c5 = t // 5
t %= 5

while (t % 2 != 0):
    t += 5
    c5 -= 1
    if (t > n):
        print(-1)
        sys.exit()
c2 = t // 2

print(c5+c2)