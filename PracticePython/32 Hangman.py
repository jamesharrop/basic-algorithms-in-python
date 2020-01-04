'''
>>> Welcome to Hangman!
_ _ _ _ _ _ _ _ _
>>> Guess your letter: S
Incorrect!
>>> Guess your letter: E
E _ _ _ _ _ _ _ E

'''
'''
Psuedocode approach with assignment to objects:

Welcome message [Player]
Choose a random word [Board]
Display the word with _ symbols where no letters are known [Board]
Display how many guesses the player has left [Player]
Ask for a guess [Player]
Check whether the player has guessed that already - if so they get another go [Player]
Check whether that guess is in the word [Board]
Loop until word is guessed or guesses are all used up [Main]
'''

import random

class Player:
    def __init__(self):
        print("Welcome to this game.")
        self.guesses = []
    
    def print_how_many_guesses_left(self):
        print(f"You have {6-len(self.guesses)} guesses left.")

    def ask_for_guess(self) -> str:
        guess = input("Guess a letter: ")
        # Input validation goes here
        return guess

    def letter_is_already_guessed(self, guess) -> bool:
        return (guess in self.guesses)
    
    def display_whether_guess_correct(self, correct: bool):
        if correct:
            print("Correct")
        else:
            print("That's not in the word")
    
class Board:
    def __init__(self):
        self.word = ""
        self.guessed = [] # A list of Bools corresponding to which letters in word have been guessed

    def choose_random_word(self):
        with open("sowpods.txt", "r") as f:
            word_list = f.readlines()
            self.word = random.choice(word_list).strip()
            self.guessed = [False] * len(self.word)

    def display_word(self):
        for index, letter in enumerate(self.word):
            if self.guessed[index]:
                print(letter, end="")
            else:
                print("_", end="")
            print(" ", end="")
        print("\n")
    
    def check_if_guess_in_word(self, guess):
        is_in_word = False
        for index, letter in enumerate(self.word):
            if letter == guess:
                self.guessed[index] = True
                is_in_word = True
        return(is_in_word)

    def all_letters_have_been_guessed(self):
        return (not any(letter == False for letter in self.guessed))

    def debug_print_out_variables(self):
        print("word:", self.word)
        print("guessed:", self.guessed)

if __name__ == "__main__":    
    p = Player()
    b = Board()
    b.choose_random_word()
    b.display_word()
    while True:
        b.debug_print_out_variables()
        while True:
            p.print_how_many_guesses_left()
            guess = p.ask_for_guess()
            if p.letter_is_already_guessed(guess):
                print("You already guessed that letter - have another go")
            else:
                break
        correct = b.check_if_guess_in_word(guess)
        p.display_whether_guess_correct(correct)
        if b.all_letters_have_been_guessed():
            print("All guessed")
            break
