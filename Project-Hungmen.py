import random

def hangman():
    # List of words to guess
    words = ["human", "Bear", "tiger", "superman", "thor", 
             "pokemon", "avengers", "savewater", "earth", "annable"]
    word = random.choice(words).lower()  # Randomly select a word
    valid_letters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessed_letters = set()

    print("Welcome to Hangman!")
    print("You have 10 chances to guess the word correctly.")
    print("-" * 30)

    while True:
        # Build the display word based on guessed letters
        display_word = ''.join([letter if letter in guessed_letters else ' _ ' for letter in word])
        print(f"Word: {display_word}")

        # Check if turns are exhausted
        if turns == 0:
            print("\nGame Over! The correct word was:", word)
            print("Better luck next time!")
            print_hangman(turns)  # Final stage
            break

        # Check if the user has guessed the entire word
        if display_word.replace(' ', '') == word:  # Remove spaces added in ' _ '
            print("\nCongratulations! You guessed the word:", word)
            break

        guess = input("\nGuess a letter: ").lower()

        # Validate the input
        if len(guess) != 1 or guess not in valid_letters:
            print("Invalid input. Please enter a single valid letter.")
            continue

        # Process the guess
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
        else:
            guessed_letters.add(guess)
            if guess not in word:
                turns -= 1
                print(f"Wrong guess! You have {turns} turns left.")
                print_hangman(turns)

def print_hangman(turns):
    """
    Display hangman progress based on remaining turns.
    """
    stages = [
        """
           --------
               O_|
              /|\\
              / \\
        """,
        """
           --------
               O_|/
              /|\\
              / \\
        """,
        """
           --------
              \\O_/|
               |
              / \\
        """,
        """
           --------
              \\O_/
               |
              / \\
        """,
        """
           --------
              \\O 
               |
              / \\
        """,
        """
           --------
               O
               |
              / \\
        """,
        """
           --------
               O
               |
              / 
        """,
        """
           --------
               O
               |
        """,
        """
           --------
               O
        """,
        """
           --------
        """
    ]

    if turns >= 0:  # Ensure valid index
        print(stages[9 - turns])

if __name__ == "__main__":
    name = input("Enter your name: ").strip()
    print(f"Welcome, {name}!")
    print("Try to guess the word in less than 10 attempts!")
    hangman()
