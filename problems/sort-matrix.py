m = [
    [91, 12, 54],
    [65, 78, 9],
    [99, 23, 38]
]

print(m)

# sort loop can sort an array called "a"
for x in range(len(m)):
    a = m[x]
    for j in range(len(a)-1):
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                a[i+1], a[i] = a[i], a[i+1]

print(m)
