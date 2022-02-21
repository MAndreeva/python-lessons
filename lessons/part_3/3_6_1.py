from requests import *

with open('input4.txt') as inf:
    url = inf.readline().strip()
k = 0
r = get(url)
for line in r.text.splitlines():
    k += 1
print(k)
