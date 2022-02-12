s = input()
res = ''
p = s[0]
n = 0
for i in range(len(s) - 1):
    if p == s[i + 1]:
        n += 1
    else:
        res += p + str((n + 1))
        n = 0
    p = s[i + 1]
res += s[-1] + str(n + 1)
print(res)
