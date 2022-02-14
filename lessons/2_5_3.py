l = [int(i) for i in input().split()]
s = ''
if (len(l) == 1):
    print(str(l[0]))
else:
    for i in range(len(l)):
        if (i == 0):
            s += str(l[-1]  + l[i + 1]) + ' '
        elif (i == (len(l)-1)):
            s += str(l[i-1]  + l[0])
        else:
            s+= str(l[i-1] + l[i + 1]) + ' '

print(s)
