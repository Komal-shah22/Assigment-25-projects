import random

def welcome_message():
    """
    This function displays a welcome message for the user.
    """
    print("\n\t\t\t========= WELCOME TO THE GUESS THE NUMBER GAME! ========\n")
    print("The computer has picked a random number between 1 and 100.")
    print("Your task is to guess the correct number!")
    print("After each guess, you will get a hint: 'Too High' or 'Too Low'.\n")
    print("\t\t\t~~~~~~~~~~~~~Let's begin! ~~~~~~~~~~~~\n")

def play_game():
    """
    This function contains the main logic of the game.
    """

    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)
    attempts = 0

    while True:
        try:
            # Ask the user for their guess
            guess = int(input("Enter your guess (1-10): "))
            attempts += 1

            # Check if the guess is correct
            if guess == secret_number:
                print(f"\n\t~~~~ Congratulations! You guessed the number in {attempts} attempts. ~~~~")
                break
            elif guess < secret_number:
                print(" Too Low! Try again.")
            else:
                print(" Too High! Try again.")
        
        except ValueError:
            print(" Invalid input! Please enter a number between 1 and 10.")

# Start the game with a welcome message
welcome_message()

# Repeat the game if the user wants to play again
while True:
    play_game()
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("\n\t\t~~~~~~ Thank you for playing! Have a wonderful day! ~~~~~~ ")
        break
