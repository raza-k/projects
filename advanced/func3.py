def max_three(a, b, c):
    big = None

    if a > b:
        big = a
    else:
        big = b

    if big < c:
        big = c

    return big


ret = max_three(7, 7, 7)
print(f"the biggest number is {ret}")
