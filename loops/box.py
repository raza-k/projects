x = int(input("how big?:"))
while x > 0:
    i = 0
    while i < x:
        i = i + 1

        j = 0
        while j < x:
            j = j + 1
            print("*", end="")

        print("")
    x = int(input("how big?:"))