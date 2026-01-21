import sys
sys.setrecursionlimit(10**6)

def func(f):
    global arr
    if f == 1:
        return 0
    a = b = c = float("inf")
    if (arr[f] > 0):
        return arr[f]
    if (f % 3 == 0):
        a = 1 + func(f//3)
    if (f % 2 == 0):
        b = 1 + func(f//2)
    c = 1 + func(f-1)

    arr[f] = min(a, b, c)
    return arr[f]

x = int(input())
arr = [-1] * (x+3)

print(func(x))