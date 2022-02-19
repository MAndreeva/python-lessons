with open('input1.txt') as inf:
    s = inf.readline().strip()
let = s[0]
k = ''
res = ''
for i in range(len(s) - 1):
    if s[i + 1].isnumeric():
        k += s[i + 1]
    else:
        res += let * int(k)
        # for j in range(int(k)):
        #     res += let
        let = s[i + 1]
        k = ''
if res != '':
    for j in range(int(k)):
        res += let
with open('output1.txt', 'w') as outf:
    outf.write(res)
