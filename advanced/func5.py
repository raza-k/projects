def match(a,b):
    if a == b:
        return True
    else:
        return False


x = input("enter a string")
y = input("enter another string")
Check = match(x,y)
if Check == True:
    print("match")
else:
    print("no match")

