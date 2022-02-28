ages=[93, 326, 12, 3, 9, 10, 123]

min = ages[0]

for e in range (0, len(ages)):
	v = ages[e]
	if v < min:
		min = v

print(min)


