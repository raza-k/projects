search=[2,5,7,9,12,4,6,8]

a=int(input('tell me the number you want me to search'))

found = False

for x in range(0,len(search)):
	print(".", end='')
	if search[x] == a:
		found=True
		break

print('')
if found == True:
	print('found it')
else:
	print ('did not find it')