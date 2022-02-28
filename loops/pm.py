x = int(input("how big?"))

for i in range(x):
    for j in range(x):
        if i % 2 == 0:
            print("+", end="")
        else:
            print("-", end="")
    print("")