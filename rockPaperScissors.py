import random, sys

print ('ROCK, PAPER, SCISSORS')

wins = 0
losses = 0
ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:
        print ('Enter your move player: (r)ock, (p)aper, (s)cissors or (q)uit')
        player_choice = input('>')
        if player_choice == 'q':
            sys.exit()
        if player_choice == 'r' or player_choice == 'p' or player_choice == 's':
            break
    if player_choice == 'r':
        print('ROCK versus...')
    if player_choice == 'p':
        print('PAPER versus...')
    if player_choice == 's':
        print('SCISSORS versus...')
    num_choice = random.randint(1, 3)
    
    if num_choice == 1:
        computer_choice = 'r'
        print('ROCK')
    elif num_choice == 2:
        computer_choice = 'p'
        print('PAPER')
    elif num_choice == 3:
        computer_choice = 's'
        print('SCISSORS')
    
    # counter
    
    if player_choice == computer_choice:
        print('Its a tie!')
        ties = ties + 1
    elif player_choice == 'r' and computer_choice == 'p':
        print('You lose, good luck next time!')
        losses = losses + 1 
    elif player_choice == 'p' and computer_choice == 's':
        print('You lose, good luck next time!')
        losses = losses + 1 
    elif player_choice == 's' and computer_choice == 'r':
        print('You lose, good luck next time!')
        losses = losses + 1 
    elif player_choice == 'r' and computer_choice == 's':
        print('You win! Rematch!')
        wins = wins + 1 
    elif player_choice == 'p' and computer_choice == 'r':
        print('You win! Rematch!')
        wins = wins + 1 
    elif player_choice == 's' and computer_choice == 'p':
        print('You win! Rematch!')
        wins = wins + 1 

