a = [4, 23, 71, 45, 0]
b = [93, -1, 72, 45, 22]
m = []

for x in range(5):
    if a[x] > b[x]:
        m.append(a[x])
    else:
        m.append(b[x])

print(m)
