from importlib.resources import as_file
import random
from words import words
import string
# Choosing a word form words list
def get_valid_word(words):
    word = random.choice(words)
    # Exluding the words that contain " " or "-"
    while " " in word or "-" in word:
        word = random.choice(words)
    return word.upper()

# The game funciton 
def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word to keep of what's have been guessed in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed
    lives = 6 
    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print("You have ", lives, " lives left","You have used these letters: ", " ".join(used_letters))

        # what current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        user_letter = input("Guess a letter: ").upper()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1 # take away one life
                print('Letter is not a word.')

        elif user_letter in used_letters:
            print("You have already used that letter. Please try again.")

        else:
            print("Invalid character. Please try again.")
    if lives == 0:
        print('You died, sorry. The word was ', word)
    print('You guessed the word ', word, '.')


hangman()