import random

def hangman():
    # Step 1: Predefined list of words
    words = ["python", "java", "kotlin", "swift", "hangman"]
    word = random.choice(words)  # Pick a random word
    
    guessed_word = ["_"] * len(word)  # Display underscores for unguessed letters
    guessed_letters = []  # Track guessed letters
    attempts = 6  # Limit of incorrect guesses

    print("Welcome to Hangman!")
    
    # Step 2: Game loop
    while attempts > 0 and "_" in guessed_word:
        print("\nWord: ", " ".join(guessed_word))
        print("Guessed letters: ", " ".join(guessed_letters))
        print(f"Attempts left: {attempts}")
        
        guess = input("Guess a letter: ").lower()
        
        # Validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Step 3: Check if guess is correct
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
            print("Good guess!")
        else:
            attempts -= 1
            print("Wrong guess!")
    
    # Step 4: End game
    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame Over! The word was:", word)

# Run the game
hangman()

