l = [int(i) for i in input().split()]
a = int(input())
b = False
for i in range(len(l)):
    if l[i] == a:
        print (i, end=' ')
        b = True
if b == False:
    print('Отсутствует')