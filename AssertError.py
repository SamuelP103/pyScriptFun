spam = 9
print("Choose a flavor of spam by typing the letter corresponding")
print("BBQ - a\n"
"Mayo - b \n"
"Cheese - c\n"
"Lemon - d ")


choice = input().lower() 

if choice == 'a':
    flavor = 1
elif choice == 'b':
    flavor = 2
elif choice == 'c':
    flavor = 3
elif choice == 'd':
    flavor = 4
else:
    flavor = 0
    
hasflavor = flavor + spam

assert hasflavor >= 10, f"Don't forget a flavor! score = {hasflavor}"