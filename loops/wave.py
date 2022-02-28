x = int(input('How big? '))

for i in range(x):
    for j in range(i + 1):
        print("*", end="")
    print("")

for i in range(x):
    for j in range(x - i):
        print("*", end="")
    print("")
