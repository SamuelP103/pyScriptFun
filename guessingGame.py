import random

secret_number = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

for guesses_taken in range (1,7):
    print('Take a guess.')
    guess = int(input('>'))
    
    if guess < secret_number:
        print('To low!')
    elif guess > secret_number:
        print('Too high!')
    else:
        break
if guess == secret_number:
    print('Great job! You got it in ' + str(guesses_taken) + ' guesses!')
else:
    print('Nope the secret number was ' + str(secret_number) + ' better luck next time!')
    