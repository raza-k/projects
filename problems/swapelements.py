import random

a = []

for i in range(10):
    a.append(random.randint(1, 100))
print(a)

a[0],a[1] = a[1],a[0]
print(a)


