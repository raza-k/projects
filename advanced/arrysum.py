def arrysum(a):
    t = 0
    for x in a:
        t = t + x
    return t


data = [1, 3, 5]
total = arrysum(data)
print(total)