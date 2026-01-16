a = input()
ca = cb = 0
k = "0"
for i in range (len(a)):
    if(a[i] != k):
        ca += 1
        k = "1" if k == "0" else "0"
k = "1"
for i in range (len(a)):
    if(a[i] != k):
        cb += 1
        k = "1" if k == "0" else "0"
ca = ca % 2 + ca // 2
cb = cb % 2 + cb // 2

print(ca if ca <= cb else cb)