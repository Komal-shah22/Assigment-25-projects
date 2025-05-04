import random

def welcome_message():
    """
    This function displays a welcome message for the user.
    """
    print("\n\t\t\t======== WELCOME TO ROCK, PAPER, SCISSORS GAME! =======\n")
    print("You will play against the computer.")
    print("Enter 'rock', 'paper', or 'scissors' to make your move.")
    print("\n\t\t\t~~~~~~~~Let's see if you can beat the computer! ~~~~~~~~\n")

def get_winner(user_choice, computer_choice):
    """
    Determines the winner based on user and computer choices.
    """
    if user_choice == computer_choice:
        return "\t\t\t========= It's a tie! ========"
    
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "scissors" and computer_choice == "paper") or \
       (user_choice == "paper" and computer_choice == "rock"):
        return "\t\t\t========== You win! =========="
    
    return "\t\t\t========== Computer wins! Try again! =========="

def play_game():
    """
    Runs the main game loop.
    """
    choices = ["rock", "paper", "scissors"]

    while True:
        # User input
        user_choice = input("\nEnter your choice (rock, paper, scissors): ").strip().lower()

        if user_choice not in choices:
            print(" Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")
            continue

        # Computer choice
        computer_choice = random.choice(choices)
        print(f"\n Computer chose: {computer_choice.capitalize()}")
        
        # Determine the winner
        result = get_winner(user_choice, computer_choice)
        print(result)

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("\n\t\t\t========= Thank you for playing! Have a great day! ========")
            break

# Start the game with a welcome message
welcome_message()
play_game()
