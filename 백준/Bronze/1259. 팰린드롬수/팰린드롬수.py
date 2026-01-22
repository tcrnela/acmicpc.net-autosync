import sys
input = sys.stdin.readline

while(1):
    a = input().strip()
    if a == "0": sys.exit()
    b = a[:len(a)//2]
    if (len(a)%2):
        n = len(a)//2+1
    else: n = len(a)//2
    c = a[n:]
    c = c[::-1]
    if(b == c):
        print("yes")
    else:
        print("no")