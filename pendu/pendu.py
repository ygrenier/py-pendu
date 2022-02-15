from read_files import *
from UI         import *
import random

  # goal_is_completed:
  # return True if the user found the word
def goal_is_completed(user_word):
    for i in range(len(user_word)):
        if user_word[i] == '_':
            return False
    return True

  # reveal_char:
  # reveal all the [letter] of the word. ex.: all the A
def reveal_char(user_word, goal_word, letter, proposed_letters):
    letter_is_in_word = 0
    if letter in proposed_letters:
        return 2
    for i in range(len(goal_word)):
        if goal_word[i] == letter:
            user_word[i] = letter
            letter_is_in_word = 1
    return letter_is_in_word

  # game:
  # the main loop of the game
def game(dictionary):

      # set the words
    goal_word = dictionary[random.randint(0, len(dictionary) - 1)]
    user_word = ['_'] * len(goal_word)

    proposed_letters = []

    nb_try = 0
    while not goal_is_completed(user_word):
        print('This is your word:\n', " ".join(user_word))
        letter = UI.get_letter()
        return_code = reveal_char(user_word, goal_word, letter, proposed_letters)
        if return_code == 2:
            print('You already proposed this letter.')
        elif return_code == 1:
            print('This letter is well in the word.')
            proposed_letters.append(letter)
        else:
            print('No, this letter is not in the word.\n')
            proposed_letters.append(letter)
            nb_try += 1

      # the user won
    print('Well done!\nYou found the word (', "".join(goal_word), ') with', nb_try, 'mistakes !\n')

def main():
    UI.say_hello()  # explain the aim of the game
    dictionary = read_files.read_file('pendu/data/dictionary.txt').upper().split('\n')  # get the file content fully and formatted to a list of words

    while True:
        game(dictionary)
        answer = input('Do you want to play again?\nPlease answer y or n:\n>> ')
        while answer != 'y': # if answer == 'n', the return statement is executed.
            if answer == 'y':
                pass
            elif answer == 'n':
                return
            else:
                answer = input('please, enter y for yes or n for no.\nDo you want to play again?\n>> ')

main()