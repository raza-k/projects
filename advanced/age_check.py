def checkage(age):
    if age > 15:
        return True
    else:
        return False


answer = int(input(f"what is your age"))
E = checkage(answer)
if E == True:
    print("You are older than me ")
else:
    print("You are not older than me  ")

