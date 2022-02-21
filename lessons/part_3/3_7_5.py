n = 11
l = [[0 for j in range(2)] for i in range(n)]
with open('input6.txt', encoding='utf-8') as inf:
    for s in inf:
        w = s.strip().split('\t')
        l[int(w[0]) - 1][0] += int(w[2])
        l[int(w[0]) - 1][1] += 1

for i in range(n):
    print(i + 1, end=' ')
    if l[i][1] == 0:
        print('-')
    else:
        print(l[i][0] / l[i][1])
