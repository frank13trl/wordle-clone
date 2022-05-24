from colorama import Fore, Style

MAX_LEN = 5

def validate_guess(current_guess, word_list):
    if len(current_guess) == MAX_LEN:
        if current_guess.isalpha():
            if current_guess in word_list:
                return True
            else:
                print(Fore.LIGHTRED_EX + "Word not in word list !" + Fore.RESET)
        else:
            print(Fore.LIGHTRED_EX + "Word should only contain alphabets !" + Fore.RESET)
    else:
        print(Fore.LIGHTRED_EX + "Word should be of five letters !" + Fore.RESET)

def word_equal(listed_word, guessed_word):
    if listed_word == guessed_word:
        return True

def word_unequal(hidden_list, open_list, guessed_includes, guessd_right):
    temp_word = []
    right_letters = []
    for idx in range(MAX_LEN):

        letter = open_list[idx]

        if letter in guessd_right and letter == hidden_list[idx]:
            temp_word.append(Fore.GREEN + letter + Fore.RESET)
            guessd_right.remove(letter)
            if letter in guessed_includes: guessed_includes.remove(letter)
            right_letters.append(letter)

        elif letter in guessed_includes:
            temp_word.append(Fore.YELLOW + letter + Fore.RESET)
            guessed_includes.remove(letter)
            if letter in guessd_right: guessd_right.remove(letter)

        else: temp_word.append(letter)

    return temp_word, right_letters