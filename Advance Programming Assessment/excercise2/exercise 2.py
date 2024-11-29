import random
import os

def load_jokes(filename):
    try:
        print(f"Looking for the file in: {os.getcwd()}")
        with open(filename, 'r') as file:
            jokes = file.readlines()
        return [joke.strip() for joke in jokes if '?' in joke]
    except FileNotFoundError:
        print(f"Error: Joke file '{filename}' not found.")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []

def tell_joke(jokes):
    if not jokes:
        print("No jokes available to display.")
        return
    joke = random.choice(jokes)
    if '?' in joke:
        setup, punchline = joke.split('?', 1)
        print(f"Setup: {setup.strip()}?")
        input("Press Enter to see the punchline...")
        print(f"Punchline: {punchline.strip()}")
    else:
        print("Invalid joke format: No '?' found in joke.")

def main():
    # Full path to the jokes file
    jokes_file = r"C:/Users/Dell/Documents/Advance Programming Assessment/excercise2/randomJokes.txt"
    
    jokes = load_jokes(jokes_file)

    if not jokes:
        return

    while True:
        user_input = input("Alexa, tell me a Joke (or type 'quit' to exit): ").lower()

        if user_input == 'quit':
            print("Goodbye!")
            break
        elif 'tell me a joke' in user_input:
            tell_joke(jokes)
        else:
            print("Please ask 'Alexa, tell me a Joke' or type 'quit' to exit.")

if __name__ == "__main__":
    main()
