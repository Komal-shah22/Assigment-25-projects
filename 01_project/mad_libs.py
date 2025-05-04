import random

def welcome_message():
    """
    This function displays a welcome message for the user.
    """
    print("\n\t\t\t~~~~~~ WELCOME TO THE MAD LIBS GAME! ~~~~~~ \n")
    print("This is a fun game where YOU create a unique and funny story!")
    print("Just answer a few simple questions, and we will make a story for you. \n")
    print("\t\t\t========== Let's get started! ========\n")

def create_story():
    """
    This function asks the user for some words and then makes a fun story.
    """

    # List of different stories
    story_templates = [
        "{name} went to {place}. The place was very {adjective}. Suddenly, a {animal} appeared and started {verb}. {name} was surprised and watched carefully. Later, they ate {food} and enjoyed {activity}.",
        "One day, {name} visited {place}. There, they saw a {adjective} {animal} that was {verb}. It was very funny! After that, {name} had some {food} and spent time doing {activity}.",
        "{name} and their friend went on a {adjective} journey to {place}. While walking, they saw a {animal} that was {verb}. They laughed a lot! In the evening, they ate {food} and enjoyed {activity} together."
    ]

    # Ask the user for words
    print("\n Answer the following questions to create your story: \n")
    name = input("Enter a name (Example: Ali, Sara): ")
    place = input("Enter a place (Example: park, beach, school): ")
    adjective = input("Enter a describing word (Example: beautiful, funny, scary): ")
    animal = input("Enter an animal (Example: cat, elephant, lion): ")
    verb = input("Enter an action word (Example: running, jumping, singing): ")
    food = input("Enter a food (Example: pizza, burger, ice cream): ")
    activity = input("Enter an activity (Example: dancing, playing football, reading): ")

    # Pick a random story
    story = random.choice(story_templates)

    # Put the user’s words into the story
    final_story = story.format(
        name=name, place=place, adjective=adjective,
        animal=animal, verb=verb, food=food, activity=activity
    )

    # Show the story
    print("\n Here is your story! \n")
    print(final_story)
    print("\nHope you liked it! ")

# Start the game with a welcome message
welcome_message()

# Repeat the game if the user wants to play again
while True:
    create_story()
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("\n Thank you for playing!")
        break
