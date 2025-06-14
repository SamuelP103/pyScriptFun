import random

def random_number(chosen_number):
    if chosen_number == 1:
        return 'It is certain'
    if chosen_number == 2:
        return 'It is decidedly so'
    if chosen_number == 3:
        return 'Yes'
    if chosen_number == 4:
        return 'Reply hazy, try again'
    if chosen_number == 5:
        return 'Ask again later'
    if chosen_number == 6:
        return 'Concentrate and ask again'
    if chosen_number == 7:
        return 'No'
    if chosen_number == 8:
        return 'Outlook does not look good'
    if chosen_number == 9:
        return 'Very doubtful'
    
print('Ask a yes or no question')
input('>')
r = random.randint(1,9)
fortune = random_number(r)
print(fortune)
    
