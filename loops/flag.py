x = int(input("how big:"))

for i in range(x):
    for j in range(x):
        if i % 2 == 0:
            if j % 2 == 0:
                print("*", end="")
            else:
                print(" ", end="")
        else:
            if j % 2 == 0:
                print(" ", end="")
            else:
                print("*", end="")
    print("")