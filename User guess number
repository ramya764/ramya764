import random
from colorama import Fore

# generating magic number
magic_number = random.randint(1, 101)

user_guess = 0
# chances for number of guesses
chances = 5

while user_guess != magic_number and chances != 0:
    print(Fore.RED, f"you have {chances} left")
    # taking guesses from user
    user_guess = int(input("enter a guess between 1 to 100  "))

    if user_guess > magic_number:
        print(Fore.BLUE, "you are too high for magic number")

    elif user_guess < magic_number:
        print(Fore.BLUE, "you are too low for magic number")

    else:
        print(Fore.MAGENTA, f"congrats!!....you have guess the magic number {magic_number} correctly")
        break
    chances -= 1
if user_guess != magic_number:
    print(Fore.LIGHTRED_EX, "you lost the match")
