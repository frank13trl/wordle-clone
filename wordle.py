# WORDLE clone by Frank Therattil (21MCA0184), VIT University, Vellore

import random
import string
from art import *
from colorama import Fore, Style

from wordle_check import *

def letter_history():
    print("Letter History :", end=' ')
    for alphabet in ALPHABETS:
        if alphabet in right_guesses: print(Fore.GREEN + alphabet, end=' ' + Fore.RESET)
        elif alphabet in word_has: print(Fore.YELLOW + alphabet, end=' ' + Fore.RESET)
        elif alphabet in used_letters: print(Fore.LIGHTBLACK_EX + alphabet, end=' ' + Fore.RESET)
        else: print(alphabet, end=' ')

tprint("WORDLE", font="small")
print(Style.BRIGHT + " HOW TO PLAY ".center(25, "="))
print("""Each guess must be a valid five-letter word. Hit the enter button to submit.
After each guess, the color of the letters will change to show how close your guess was to the word.\n""")

print(Fore.GREEN + "GREEN - The letter is in the word and in the correct spot." + Fore.RESET)
print(Fore.YELLOW + "YELLOW - The letter is in the word but in the wrong spot." + Fore.RESET)
print(Fore.LIGHTBLACK_EX + "GREY - The letter is not in the word in any spot.\n" + Fore.RESET)

word_list = open('word-list.txt', 'r').read().splitlines()
word = random.choice(word_list)
word = word.upper()
word = "POPPY"

tries_left = 6
success = False

ALPHABETS = list(string.ascii_uppercase)
used_letters = []
word_has = []
right_guesses = []
guess_history = []

while(tries_left > 0 and success == False):

    valid_guess = False
    while(not valid_guess):
        guess_word = input(Fore.LIGHTMAGENTA_EX + "Guess the word : " + Fore.RESET).strip()
        valid_guess = validate_guess(guess_word.lower(), word_list)
        
    guess = guess_word.upper()

    letter_list, guess_list = list(word), list(guess)

    for letter in guess_list:
        if letter not in used_letters: used_letters.append(letter)
        
    guessed_has = [i for i in letter_list if i in guess_list]
    for letter in guessed_has:
        if letter not in word_has: word_has.append(letter)
        
    guessed_correct = [k for k,v in zip(guess_list, letter_list) if k==v]

    new_word, right = word_unequal(letter_list, guess_list, guessed_has, guessed_correct)

    guess_history.append(new_word)
        
    for each_letter in right:
        if each_letter not in right_guesses: right_guesses.append(each_letter)
        
    for each in guess_history:
        print(" ".join(each))

    letter_history()
    if word_equal(guess, word):  success = True

    _try_ = "tries"
    if tries_left == 2: _try_ = "try"
    if tries_left != 1 and success == False:
        print(Fore.BLUE + "\nYou have {0} more {1} left\n".format(tries_left-1, _try_) + Fore.RESET)

    tries_left -= 1

if success == True:
    print(Fore.GREEN + "\nCongratulations! You guessed the word correctly\n" + Fore.RESET + Style.RESET_ALL)
else:
    print(Fore.LIGHTRED_EX + "\nYou ran out of chances! The word was :", word, "\n" + Fore.RESET + Style.RESET_ALL)