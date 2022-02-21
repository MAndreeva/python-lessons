w = []
d = {}
with open('input2.txt') as inf:
    for s in inf:
        s = s.strip()
        w = s.lower().split()
        for i in range(len(w)):
            if w[i] not in d:
                d[w[i]] = 1
            else:
                d[w[i]] += 1
max = 0
max_w = ''
for k in d.keys():
    if d[k] > max or d[k] == max and k < max_w:
        max = d[k]
        max_w = k

print(max_w, max)
