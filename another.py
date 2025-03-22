import random

n = random.randrange(1,101)
guess = int(input('Enter the number(1 to 100): '))

while n != guess:
    if guess < n:
        print('Too low!')
        guess = int(input('Enter the number(1 to 100): '))
    elif guess > n:
        print('Too high!')
        guess = int(input('Enter the number(1 to 100): '))
    break
print('You Got it!')        