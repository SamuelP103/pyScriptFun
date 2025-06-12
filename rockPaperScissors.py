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
    if player_choice == 'r':
        print('ROCK versus...')
    if player_choice == 'r':
        print('ROCK versus...')