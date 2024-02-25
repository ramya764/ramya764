import random

def choose_word():
    words = ["javascript", "python", "programming", "developer", "coding", "pacewisdom", "swapnodaya"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def display_hangman(incorrect_attempts):
    hangman_art = [
        """
         -----
         |   |
             |
             |
             |
             |
        -----
        """,
        """
         -----
         |   |
         O   |
             |
             |
             |
        -----
        """,
        """
         -----
         |   |
         O   |
         |   |
             |
             |
        -----
        """,
        """
         -----
         |   |
         O   |
        /|   |
             |
             |
        -----
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
             |
             |
        -----
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        /    |
             |
        -----
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        -----
        """
    ]

    return hangman_art[incorrect_attempts]

def hangman():
    print("Welcome to Hangman!")
    word_to_guess = choose_word()
    guessed_letters = []
    incorrect_attempts = 0
    max_attempts = 15

    while True:
        current_display = display_word(word_to_guess, guessed_letters)
        print(f"\n{display_hangman(incorrect_attempts)}")
        print(f"Current word: {current_display}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")

        if current_display == word_to_guess:
            print("Congratulations! You've guessed the word.")
            break

        if incorrect_attempts >= max_attempts:
            print(f"Sorry, you've run out of attempts. The word was: {word_to_guess}")
            break

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            incorrect_attempts += 1
            print(f"Incorrect guess! You have {max_attempts - incorrect_attempts} attempts left.")


hangman()
