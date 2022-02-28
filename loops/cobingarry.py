a = [0, 1, 1, 1, 1, 1, 1]

for x in range(1, len(a)):
    a[x] = a[x] + a[x-1]

print(a)
