import sys

while True:
    print ('Info: type Exit to exit')
    print ('Enter your name pretty please')
    Name = input('>')
    if Name == ('Exit'):
        sys.exit()
    if Name == ('your name'):
        break
print('Thank you smartie pants')