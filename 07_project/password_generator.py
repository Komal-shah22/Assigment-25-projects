import random
import string

def welcome_message():
    """
    Displays a welcome message.
    """
    print("\n\t\t\t~~~~~~~~ WELCOME TO THE RANDOM PASSWORD GENERATOR! ~~~~~~~\n")
    print("Create strong and secure passwords in seconds.")
    print("Customize the length and number of passwords you need.")
    print("\t\t\t========= Let's begin! ========\n")

def generate_password(length):
    """
    Generates a random secure password of the given length.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))

def password_generator():
    """
    Asks the user for input and generates multiple passwords based on their preferences.
    """
    try:
        num_passwords = int(input("Enter the number of passwords to generate: "))
        if num_passwords <= 0:
            print(" Please enter a positive number!")
            return

        length = int(input("Enter the desired password length (minimum 6): "))
        if length < 6:
            print(" Password length should be at least 6 for security!")
            return

        print("\n Here are your secure passwords:\n")
        for i in range(num_passwords):
            print(f"{i + 1}. {generate_password(length)}")

    except ValueError:
        print(" Invalid input! Please enter a number.")

# Start the program with a welcome message
welcome_message()

while True:
    password_generator()
    play_again = input("\nDo you want to generate more passwords? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("\n\t\t========= Thank you for using the Password Generator! Stay secure! =========")
        break
