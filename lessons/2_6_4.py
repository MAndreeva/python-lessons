a = []
inp = input()
while inp != 'end':
    a.append([int(j) for j in inp.split()])
    inp = input()
n = len(a)
m = len(a[0])
res = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        if i == n - 1:
            res[i][j] += a[0][j]
        else:
            res[i][j] += a[i + 1][j]
        if j == m - 1:
            res[i][j] += a[i][0]
        else:
            res[i][j] += a[i][j + 1]
        res[i][j] += a[i-1][j] + a[i][j-1]
for i in range(n):
    for j in range(m):
        print (res[i][j], end=' ')
    print()