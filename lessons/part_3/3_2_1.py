def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    elif key*2 in d:
        d[key*2].append(value)
    else:
        d[key*2] = [value]

d = {}
update_dictionary(d, 1, -1)
print(d)
update_dictionary(d, 2, -2)
print(d)
update_dictionary(d, 1, -3)
print(d)