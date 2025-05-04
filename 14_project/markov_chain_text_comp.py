import random

def welcome_message():
    print("\n\t\t\t~~~~~~ WELCOME TO THE MARKOV CHAIN TEXT COMPOSER! ~~~~~~\n")
    print("This tool generates random text based on input using Markov Chains.")
    print("Simply paste in some text (like song lyrics or a paragraph), and see the magic!\n")
    print("\t\t\t========== Let's begin! ==========\n")

def build_markov_chain(text):
    words = text.split()
    markov_chain = {}
    for i in range(len(words) - 1):
        word, next_word = words[i], words[i + 1]
        if word not in markov_chain:
            markov_chain[word] = []
        markov_chain[word].append(next_word)
    return markov_chain

def generate_text(chain, length=50):
    word = random.choice(list(chain.keys()))
    output = [word]
    for _ in range(length - 1):
        next_words = chain.get(word)
        if not next_words:
            word = random.choice(list(chain.keys()))
        else:
            word = random.choice(next_words)
        output.append(word)
    return ' '.join(output)

# Run in a loop
while True:
    welcome_message()
    user_input = input("Paste some text to train the Markov model: \n\n")
    chain = build_markov_chain(user_input)
    
    generated = generate_text(chain)
    print("\nHere's your generated text:\n")
    print(generated)

    again = input("\nDo you want to generate again with new input? (yes/no): ").strip().lower()
    if again != 'yes':
        print("\nThanks for using the Markov Chain Text Composer!")
        break
