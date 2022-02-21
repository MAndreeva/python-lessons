n=int(input())
loc = [0,0]
for i in range (n):
    l = input().split()
    if l[0]== 'север':
        loc[1] += int(l[1])
    if l[0]== 'юг':
        loc[1] -= int(l[1])
    if l[0]== 'восток':
        loc[0] += int(l[1])
    if l[0]== 'запад':
        loc[0] -= int(l[1])
for i in loc:
    print (i, end=' ')