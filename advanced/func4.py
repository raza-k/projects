def check_name(name):
    if name == "raza":
        return True
    else:
        return False


x = input(" enter a name")
check = check_name(x)
if check == True:
    print(" That is my name")
else:
    print("that is not my name")






