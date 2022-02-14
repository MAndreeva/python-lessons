# l = [int(i) for i in input().split()]
# s = ''
# l.sort()
# while (len(l) != 1):
#     if (l[0] == l[1]):
#         s += str(l[0]) + ' '
#         while (len(l) >= 2) and l[0] == l[1]:
#             del (l[1])
#     else:
#         del (l[0])
# print(s)

l = [int(i) for i in input().split()]
l.sort()
s = ''
p = l[0]
n = 0
for i in range(len(l) - 1):
    if p == l[i + 1]:
        n += 1
    else:
        if n != 0:
            s += str(p) + ' '
        n = 0
    p = l[i + 1]
if n != 0:
    s += str(l[-1])
print(s)
