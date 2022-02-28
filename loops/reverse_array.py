arry = [71, 42, 9, 23, 4, 55, 99]

# before
for i in range(len(arry)):
    print(arry[i], " ", end="")
print("")

for x in range(int(len(arry)/2)):
    temp = arry[x]
    arry[x] = arry[len(arry) - x - 1]
    arry[len(arry) - x - 1] = temp

# before
for i in range(len(arry)):
    print(arry[i], " ", end="")
print("")
