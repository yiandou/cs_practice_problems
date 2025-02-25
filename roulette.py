import random
import time

# Generate a wheel
def generate_wheel():
    spaces = []
    for i in range(18):
        spaces.append("red")
        spaces.append("black")
    for i in range(2):
        spaces.append("green")
    
    return spaces

# Generate a random space that gets landed on.
def spin_wheel(spaces): return random.choice(spaces)

def play_game():
    money = 2048
    spaces = generate_wheel()

    print(f"You have ${2048}.")

    while True:
        landed = spin_wheel(spaces)
        bet = int(input("How much do you wish to bet?\n"))
        color = input("Pick a color to bet on.\n")

        for i in range(random.randint(0, 128)):
            print("Spinning" + "."*i)
            time.sleep(0.25)

        print(f"It landed on {landed}")

        if landed == color:
            money = money + bet
            print(f"You won! You now have ${money}.")
        else:
            money = money - bet
            print(f"You lost. You now have ${money}.")
            if money == 0:
                print("You\'re broke...")
                break

        if input("Do you want to play again?[y/n]") == "n":
            break


play_game()
