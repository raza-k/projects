x = int(input("how big?:"))

for i in range(x):
    for j in range(i+1):
        if j == 0 or j == i or i == x - 1:
            print("*", end="")
        else:
            print(" ", end="")

    print("")
