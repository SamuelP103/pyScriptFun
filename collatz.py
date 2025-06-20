while True:
    def collatz(number):
        if number % 2 == 0:
            print(number // 2)
        else:
            print(number * 3 + 1)
    try:        
        usr_input = int(input('Enter a number:'))
        collatz(usr_input)
    except ValueError:
        print('Enter a proper number')
