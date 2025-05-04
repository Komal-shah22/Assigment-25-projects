import time

def welcome_message():
    """
    Displays a welcome message.
    """
    print("\n\t\t\t~~~~~~~~~~~~ WELCOME TO THE COUNTDOWN TIMER! ~~~~~~~~~~~\n")
    print("Enter the time in seconds, and the timer will count down.")
    print("\n\t\t\t======== Let's begin! ========\n")

def countdown_timer(seconds):
    """
    Runs a countdown from the given number of seconds.
    """
    while seconds:
        minutes, secs = divmod(seconds, 60)
        timer_display = f"{minutes:02d}:{secs:02d}"
        print(f"\r Time Remaining: {timer_display}", end="")  # Updates the same line
        time.sleep(1)
        seconds -= 1

    print("\n\t\t\t========= Time's up! =========\n")

# Start the timer with a welcome message
welcome_message()

while True:
    try:
        user_time = int(input("Enter the countdown time in seconds: "))
        if user_time <= 0:
            print(" Please enter a positive number!")
            continue
        countdown_timer(user_time)
    except ValueError:
        print(" Invalid input! Please enter a number.")

    play_again = input("\nDo you want to set another timer? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("\n\t\t\t========= Thank you for using the Countdown Timer! ========")
        break
