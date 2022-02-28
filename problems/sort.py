import random

a = []

for i in range(10):
    a.append(random.randint(1, 100))

print(a)

for j in range(len(a)-1):
    for i in range(len(a)-1):
        if a[i] < a[i+1]:
            a[i+1], a[i] = a[i], a[i+1]

print(a)
