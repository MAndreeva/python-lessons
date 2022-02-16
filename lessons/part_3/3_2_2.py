s=input().lower()
l=[i for i in s.split()]
d={}
for i in range(len(l)):
    if l[i] in d:
        d[l[i]] += 1
    else:
        d[l[i]] = 1

for key, value in d.items():
    print (key, value)