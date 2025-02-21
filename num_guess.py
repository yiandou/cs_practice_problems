import random

random_num = random.randint(0,100)
guess_c = 0

while True:
    guess_c = guess_c + 1
    guess = int(input("Guess a number from 0-100\n"))
    if guess < random_num:
        print("The number is higher.\n")
    elif guess > random_num:
        print("The number is lower.\n")
    else:
        print("You guessed the number.\n")
        print(f"You took {guess_c} guesses")
        break
