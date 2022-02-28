name=input('what file:')
fp=open(name)
line=fp.readline()
count=0
while(line):
	count=count+1
	line=fp.readline()

print(count)