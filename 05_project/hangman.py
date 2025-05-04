import random

def welcome_message():
    """
    This function displays a welcome message for the user.
    """
    print("\n\t\t\t========= WELCOME TO THE HANGMAN GAME! =========\n")
    print("Try to guess the word one letter at a time.")
    print("You have limited attempts, so choose wisely! \n")
    print("\n\t\t\t~~~~~~~ Let's begin! ~~~~~~~~\n")

def choose_word():
    """
    Randomly selects a word from a predefined list.
    """
    words = ["python", "developer", "hangman", "programming", "artificial", "machine", "learning"]
    return random.choice(words)

def display_word(word, guessed_letters):
    """
    Displays the word with guessed letters filled in and unguessed letters as underscores.
    """
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def play_game():
    """
    Main function to play the Hangman game.
    """
    word = choose_word()
    guessed_letters = set()
    attempts = 6  # Maximum wrong guesses allowed

    print(" The word to guess:", display_word(word, guessed_letters))

    while attempts > 0:
        guess = input("\nEnter a letter: ").strip().lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print(" Invalid input! Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(" You've already guessed this letter! Try a different one.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("\n Correct guess!")
        else:
            attempts -= 1
            print(f"\n Wrong guess! You have {attempts} attempts left.")

        # Display the word with guessed letters
        current_state = display_word(word, guessed_letters)
        print("\nWord:", current_state)

        # Check if the user has won
        if "_" not in current_state:
            print("\n\t\t======= Congratulations! You've guessed the word correctly! =======\n")
            break

    else:
        print(f"\n Game over! The correct word was: {word}\n")

# Start the game with a welcome message
welcome_message()

# Repeat the game if the user wants to play again
while True:
    play_game()
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("\n\t\t======== Thank you for playing! See you next time! =======")
        break
