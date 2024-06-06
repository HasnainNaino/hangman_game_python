import random

def choose_word():
    words = ["hangman", "computer", "python", "program", "developer", "game", "keyboard"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print("Try to guess the word. You can make up to", max_incorrect_guesses, "incorrect guesses.")

    while incorrect_guesses < max_incorrect_guesses:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        else:
            guessed_letters.append(guess)
            if guess not in word:
                incorrect_guesses += 1
                print("Incorrect guess. You have", max_incorrect_guesses - incorrect_guesses, "incorrect guesses left.")
            
            if set(word) == set(guessed_letters):
                print("\nCongratulations! You guessed the word:", word)
                break

    if incorrect_guesses == max_incorrect_guesses:
        print("\nSorry, you ran out of guesses. The word was:", word)

hangman()
