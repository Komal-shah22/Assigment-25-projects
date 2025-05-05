import random

def welcome_message():
    """
    This function displays a welcome message for the user.
    """
    print("\n\t\t\t========== WELCOME TO THE GUESS THE NUMBER GAME! ==========\n")
    print("Think of a number between 1 and 10.")
    print("The computer will try to guess your number!")
    print("You need to give hints: 'Too High', 'Too Low', or 'Correct'.\n")
    print("\t\t\t~~~~~~~~~~ Let's begin! ~~~~~~~~~~\n")

def computer_guesses():
    """
    The computer tries to guess the user's number.
    """
    low, high = 1, 10
    attempts = 0

    while True:
        if low > high:
            print("\n Oops! Something went wrong. Did you give the correct hints? Let's try again!\n")
            break

        # Computer makes a guess
        guess = random.randint(low, high)
        attempts += 1

        # Ask the user for feedback
        feedback = input(f"Is your number {guess}? (too high / too low / correct): ").strip().lower()

        if feedback == "correct":
            print(f"\n\t\t~~~~~~~~~ Yay! The computer guessed your number in {attempts} attempts! \n~~~~~~~~")
            break
        elif feedback == "too high":
            high = guess - 1
        elif feedback == "too low":
            low = guess + 1
        else:
            print(" Invalid input! Please type 'too high', 'too low', or 'correct'.")

# Start the game with a welcome message
welcome_message()

# Repeat the game if the user wants to play again
while True:
    computer_guesses()
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("\n\t\t\t============ Thank you for playing! ============")
        break
