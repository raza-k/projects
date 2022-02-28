a = [4, 9, 17, 97, 23, 44, 66]
o = []
e = []

for x in range(len(a)):
    if a[x] % 2 == 1:
        o.append(a[x])
    else:
        e.append(a[x])

print(o)
print(e)
