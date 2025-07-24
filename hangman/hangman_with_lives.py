import random
import string
from words import words  

def get_valid_word(words):
    word = random.choice(words) 
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  

    lives = 6 

    while len(word_letters) > 0 and lives > 0:

        print(f"\nYou have {lives} lives left.")
        print("Used letters: ", ', '.join(sorted(used_letters)))

    
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))


        user_letter = input("Enter a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("Good guess!")
            else:
                lives -= 1
                print("Wrong guess.")

        elif user_letter in used_letters:
            print("You’ve already used that letter. Try again.")

        else:
            print("Invalid character. Please enter a letter.")


    if lives == 0:
        print(f"\nYou lost! The word was: {word}")
    else:
        print(f"\nYou guessed the word {word} correctly! 🎉")


hangman()
