count=int(input('tell me the number of stars you want '))
for x in range (0,count):
	for y in range (0, x+1):
		print('*',end='')	
	print('')