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
def reveal_char(user_word, goal_word, letter):
    letter_is_in_word = False
    for i in range(len(goal_word)):
        if goal_word[i] == letter:
            user_word[i] = letter
            letter_is_in_word = True
    return letter_is_in_word

  # game:
  # the main loop of the game
def game(goal_word):

      # set the words
    user_word = ['_'] * len(goal_word)

    nb_try = 0
    while not goal_is_completed(user_word):
        print('This is your word:\n', " ".join(user_word))
        letter = UI.get_letter()
        if reveal_char(user_word, goal_word, letter):
            print('This letter is well in the word.\n')
        else:
            print('No, this letter is not in the word.\n')
            nb_try += 1

      # the user won
    print('Well done!\nYou found the word (', "".join(goal_word), ') with', nb_try, 'mistakes !\n')

def main():
    UI.say_hello()  # explain the aim of the game

#    if UI.get_nb_players() == 1:
    dictionary = read_files.read_file('pendu/data/dictionary.txt').upper().split('\n')  # get the file content fully and formatted to a list of words

    while True:
        goal_word = dictionary[random.randint(0, len(dictionary) - 1)]
        game(goal_word)
        answer = input('Do you want to play again?\nPlease answer y or n:\n>> ')
        while answer != 'y': # if answer == 'n', the return statement is executed.
            if answer == 'y':
                pass
            elif answer == 'n':
                return
            else:
                answer = input('please, enter y for yes or n for no.\nDo you want to play again?\n>> ')

#    else:
#          # getting the word from the first player
#       goal_word = input('The first player enter the word:\n>> ')
#        while not goal_word.isalpha():
#            goal_worl = input('please enter a word.')
""" 
          # the second player has to find it
        while True:
            game(goal_word)
            answer = input('Do you want to play again?\nPlease answer y or n:\n>> ')
            while answer != 'y': # if answer == 'n', the return statement is executed.
                if answer == 'y':
                    pass
                elif answer == 'n':
                    return
                else:
                    answer = input('please, enter y for yes or n for no.\nDo you want to play again?\n>> ')
 """        

main()