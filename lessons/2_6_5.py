n = int(input())
a = [[0 for j in range(n)] for i in range(n)]
lv = [0, 0]
pv = [0, n - 1]
ln = [n - 1, 0]
pn = [n - 1, n - 1]
k = 1
while k <= n * n:
    if lv[0] == 0 and lv[1] == 0:
        for j in range(lv[1], pv[1] + 1, 1):
            a[lv[0]][j] = k
            k += 1
        lv[0] += 1
    else:
        for j in range(lv[1] + 1, pv[1] + 1, 1):
            a[lv[0]][j] = k
            k += 1
        for t in range(2):
            lv[t] += 1

    for i in range(pv[0] + 1, pn[0] + 1, 1):
        a[i][pv[1]] = k
        k += 1
    pv[0] += 1
    pv[1] -= 1

    for j in range(pn[1] - 1, ln[1] - 1, -1):
        a[pn[0]][j] = k
        k += 1
    for t in range(2):
        pn[t] -= 1

    for i in range(ln[0] - 1, lv[0] - 1, -1):
        a[i][ln[1]] = k
        k += 1
    ln[0] -= 1
    ln[1] += 1


for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
