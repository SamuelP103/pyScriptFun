def math(num):
    try:
        return 42 / num  
    except ZeroDivisionError:
        print('Cant divide by zero on my watch!')
print(math(8))
print(math(1))
print(math(0))
print(math(3))
        
    