a, b = map(int, input().split())
cnt = 1

while (b > a):
    cnt += 1
    if(int(str(b)[-1]) == 1):
        b //= 10
    elif(b % 2 == 0):
        b //= 2
    else:
        break

if (b != a):
    print(-1)
else:
    print(cnt)