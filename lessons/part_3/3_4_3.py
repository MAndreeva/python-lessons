w = []
n = 0
sum_1 = 0
sum_2 = 0
sum_3 = 0
res = []
with open('input3.txt', encoding='utf-8') as inf:
    for s in inf:
        w = s.strip().split(';')
        n += 1
        sum_1 += int(w[1])
        sum_2 += int(w[2])
        sum_3 += int(w[3])
        res.append((int(w[1]) + int(w[2]) + int(w[3])) / 3)
res.append(str(sum_1 / n) + ' ' + str(sum_2 / n) + ' ' + str(sum_3 / n))
with open('output3.txt', 'w') as outf:
    for i in range(len(res)):
        outf.write(str(res[i]) + '\n')

        # s = s.strip()
        # w = s.split()
        # print(w)

# iterExample = iter(inf)
# iterExample = inf.__iter__()

# nextElement = next(iterExample)
# nextElement = iterExample.__next__()
