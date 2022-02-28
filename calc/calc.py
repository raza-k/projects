a = int(input("give me number"))
b = int(input("give me another number"))
opr = input('give me the opration')

if opr == '+':
	result = a + b
	print("a + b equals:", result)
elif opr == '-':
	result = a - b
	print("a - b equals:", result)
elif opr =='*':
	result= a * b
	print("a*b equals :", result)  
else:
	print ("i dont understand ", opr)
