import random
from colorama import Fore

# generating magic number
magic_number = 35
chances = 5

while chances > 0:
    computer_guess = random.randint(1,100)

    print(Fore.RED, f"Computer's guess: {computer_guess}")

    if computer_guess > magic_number:
        print(Fore.BLUE, "The computer's guess is too high.")
    elif computer_guess < magic_number:
        print(Fore.BLUE, "The computer's guess is too low.")
    else:
        print(Fore.MAGENTA, f"The computer guessed the magic number {magic_number} correctly. Congratulations!")
        break

    chances -= 1

    print(Fore.RED, f"You have {chances} guesses left.\n")
if computer_guess != magic_number:
    print(Fore.LIGHTRED_EX, "The computer couldn't guess the magic number. You won!")
