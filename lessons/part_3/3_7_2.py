l1 = list(input())
l2 = list(input())
l_toCode = list(input())
l_toEncode = list(input())
d_code = {}
d_encode = {}
for i in range(len(l1)):
    d_code[l1[i]] = l2[i]
    d_encode[l2[i]] = l1[i]
res1 = ''
res2 = ''
for i in range(len(l_toCode)):
    res1 += d_code[l_toCode[i]]
for i in range(len(l_toEncode)):
    res2 += d_encode[l_toEncode[i]]

print(res1)
print(res2)
