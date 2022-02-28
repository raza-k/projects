name = input('what file?')
fp = open(name)
line = fp.readline()
num=1
while(line):
	print(num,":", line)
	line = fp.readline()
	num=num+1
