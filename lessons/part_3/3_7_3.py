n = int(input())
s = set()
for i in range(n):
    s.add(input().lower())
n1 = int(input())
mist = set()
for i in range(n1):
    l = input().lower().split(' ')
    for j in range(len(l)):
        if l[j] not in s:
            mist.add(l[j])
for x in mist:
    print(x)
