
from random import randint

fruits=['frog','chipmuck','baba','chicken']

for x in range(0, 1):

	index = randint(0,3)

	if fruits[index] == 'baba':
		print("> wait what")
	elif fruits[index] == 'chicken':
		print("> puck puck")
	elif fruits[index] == "frog":
		print("> ribbit")
	else:
		print("> no comment")


 