import random

print('Welcome to the number guessing game!\nYou got 7 chances.')
print('lets start the game.')
num = random.randrange(100)

chances = 7
guess_counter = 0

while guess_counter < chances:
    guess_counter += 1
    guess = int(input('Enter the number(1 to 100.): '))
    if guess == num:
        print(f'You got it right in {guess_counter} attempt, The number is {num}.')
        break
    elif guess_counter >= chances and guess != num:
        print(f'Oops sorry! You got it wrong, The number is {num}')
    elif guess > num:
        print('Too High!')
    elif guess < num:
        print('Too Low!')        