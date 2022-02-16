n = int(input())
d={}
for i in range (n):
    s = int(input())
    if s not in d:
        d[s]=f(s)
        print (d[s])
    else:
        print(d[s])