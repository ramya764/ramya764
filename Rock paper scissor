import random

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_choice = input("Enter your choice: ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def display_as_emoji(choice):
    if choice == "rock":
        return "🪨"
    elif choice == "paper":
        return "📄"
    elif choice == "scissors":
        return "✂️"

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Rock, Paper, Scissors")

    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    user_choice_emoji = display_as_emoji(user_choice)
    computer_choice_emoji = display_as_emoji(computer_choice)

    print(f"You chose: {user_choice_emoji}")
    print(f"Computer chose: {computer_choice_emoji}")

    result = determine_winner(user_choice, computer_choice)
    print(result)


play_game()
