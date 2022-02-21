from requests import *

with open('input5.txt') as inf:
    url = inf.readline().strip()
r = get(url)
first = r.text.split(' ')[0]
while first != 'We':
    url_new = 'https://stepic.org/media/attachments/course67/3.6.3/' + r.text
    r = get(url_new)
    first = r.text.split(' ')[0]
    print(url_new)

with open('output5.txt', 'w') as outf:
    outf.write(r.text)
