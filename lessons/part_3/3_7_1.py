n = int(input())
d = {}
for i in range(n):
    l = input().split(';')
    if l[0] not in d:
        d[l[0]] = [0, 0, 0, 0, 0]
    if l[2] not in d:
        d[l[2]] = [0, 0, 0, 0, 0]
    d[l[0]][0] += 1
    d[l[2]][0] += 1
    if int(l[1]) > int(l[3]):
        d[l[0]][1] += 1
        d[l[0]][4] += 3
        d[l[2]][3] += 1
    elif int(l[1]) < int(l[3]):
        d[l[0]][3] += 1
        d[l[2]][1] += 1
        d[l[2]][4] += 3
    else:
        d[l[0]][2] += 1
        d[l[0]][4] += 1
        d[l[2]][2] += 1
        d[l[2]][4] += 1

for k, v in d.items():
    print((k + ':'), *v, end='\n')

# for k,v in d.items():
#     print (k, end=':')
#     for i in range (len(v)):
#         print (v[i], end = ' ')
#     print()
