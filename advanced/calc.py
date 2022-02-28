import sys


def clac(a, b, oper):
    if oper == '+':
        return a + b
    if oper == '-':
        return a - b
    if oper == '*' :
        return a * b
    if oper == '/':
        return a / b


x = int(sys.argv[1])

y = int(sys.argv[3])

z = sys.argv[2]

result = clac(x, y, z)
if result == None:
    print("invaild operator ")
else:
    print(result)
