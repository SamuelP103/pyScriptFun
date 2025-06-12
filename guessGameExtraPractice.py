import random

sec_number = random.randint(1,20)

print('choose a number between 1 and 20')
for guess_count in range(1,7):
    print('choose your number')
    guess = int(input('>'))
    
    if guess > sec_number:
        print('too high')
    elif guess < sec_number:
        print('too low')
    else:
        break
if guess == sec_number:
    print('great job you got it in ' + str(guess_count) + ' attempts')
    
else:
    print('Nope the random number was ' + str(sec_number) + ' better luck next time')
    