def gcd(a, b):
    if(b == 0):
        return a
    return gcd(b, a%b)
a, b = map(int, input().split())
c = gcd(a, b)
print(c)
print(a*b//c)