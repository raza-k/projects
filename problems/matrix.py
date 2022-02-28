import random

m = [
    [11, 12, 54],
    [65, 78, 9],
    [99, 23, 38]
]

print(m)
smallest = m[0][0]
for j in range(len(m)):
    for i in range(len(m)):
        # print(f"{j},{i}:", m[j][i])
        if m[j][i] < smallest:
            smallest = m[j][i]

print(smallest)

