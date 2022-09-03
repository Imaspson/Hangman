import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)

    while '-' in word or ' ' in word:
        word = random.choice(word)

    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    #getting user input
    while len(word_letters) > 0:
        print("You have guessed the letters: ", " ".join(used_letters))

        word_list = [letter if  letter in used_letters else '_' for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = str(input("Guess a letter: "))
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print("You have already used character.")

        else:
            print("Invalid character. Please insert another valid one.")

user_input = input("Type something: ")