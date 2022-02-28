s = [5, 29, 53, 99, 32]
f = [0, 0, 0, 0, 0]

# before
for i in range(len(s)):
    print(s[i], " ", end="")
print("")

for x in range(len(s)):
    s[x] = f[len(s) - x - 1]

# before
for i in range(len(f)):
    print(f[i], " ", end="")
print("")
