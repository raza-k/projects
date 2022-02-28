min = 7
max = 29
guess = 0
while guess <= max:
	answer = input(f'did u guess {guess}: ')
	if answer == 'y' or answer == 'yes':
		break
	guess = guess + 1
