import random  # Importing random number generator to create target number


def correct_number(guess):  # Function definition for checking if the guessed number is correct
	return guess == targetNumber


def higher_or_lower(guess):  # Function definition for telling the user if they're too high or low
	if guess > targetNumber:
		print('Nope, too high!')
	else:
		print('Nope, too low!')


playerName = 'Bella'  # Initialized with the name in the story for greeting
print('Welcome to the higher/lower game, {}!'.format(playerName))

boundsCorrect = False
while not boundsCorrect:  # Checks to see if the upper bound is greater than the lower bound
	lowerBound = int(input('Please enter the lower bound:'))
	upperBound = int(input('Please enter the upper bound:'))
	if upperBound > lowerBound:  # If this is true, it will exit, if not it will ask again
		boundsCorrect = True
	else:
		print('The higher bound must be greater than the lower bound!')

targetNumber = random.randint(lowerBound, upperBound)  # Generates our random number

guessCount = 0  # Using this to keep track of the user's guesses

keepGuessing = True
while keepGuessing:  # Asks for the users guess and passes it to our two functions
	print('')
	userGuess = int(input('Guess a number between {} and {}:'.format(lowerBound, upperBound)))
	if lowerBound <= userGuess <= upperBound:
		guessCount += 1
		if correct_number(userGuess):  # If the user guesses correctly, exit the loop
			keepGuessing = False
		else:  # If the user guesses incorrectly, call the function that prints higher or lower and restart loop
			higher_or_lower(userGuess)
	else:
		print('Please stay within the numbers given!')


def statement_ending(count):  # Checks the number of guesses to see if it should say guess or guesses
	if count == 1:
		return '{} guess'.format(count)
	else:
		return '{} guesses'.format(count)


# When guessed correctly, we let the user know
print('You got it! The number was {}! You got it in {}!'.format(targetNumber, statement_ending(guessCount)))
