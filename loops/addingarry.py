a = [55, 29, 43, 0, 91]
b = [23, 0, 86, 37, 3]
s = [0, 0, 0, 0, 0,0]

for x in range(len(a)):
    if b[x] != 0 and a[x] != 0:
        s[x] = a[x] / b[x]

print(s)
