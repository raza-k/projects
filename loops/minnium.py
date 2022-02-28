a = [15, 3, 72, 83, 3, 21]
b = []

for i in range(len(a)):

    min_index = 0
    min_value = a[0]

    for x in range(len(a)):
        if a[x] < min_value:
            min_value = a[x]
            min_index = x

    b.append(min_value)
    a.pop(min_index)

print(a)
print(b)
