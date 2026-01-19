n = input()
a = sorted(n, reverse=True)
n = "".join(a)

if (int(n) % 30 == 0):
    print(n)
else:
    print(-1)