def f1(arg):
    p = 13
    print(f"well p is {p}")
    return p


def f2():
    p = 300
    print(f"but p is {p}")
    return p


print("hello this is the main program running")
p1 = f2()
p2 = f1("hello")
print(f"p1 is actually {p1} and p2 is {p2}")


