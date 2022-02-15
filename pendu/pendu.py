from read_files import *
from UI         import *
import random

  # return True if the user found the word
def goal_is_completed(user_word):
    for i in range(len(user_word)):
        if user_word[i] == '_':
            return False
    return True

  # reveal all the [letter] of the word
def reveal_char(user_word, goal_word, letter):
    letter_is_in_word = False
    for i in range(len(goal_word)):
        if goal_word[i] == letter:
            user_word[i] = letter
            letter_is_in_word = True
    return letter_is_in_word

  # TODO
def game(dictionary):
    goal_word = dictionary[random.randint(0, len(dictionary) - 1)]
    user_word = ['_'] * len(dictionary)
    nb_try = 0
    while not goal_is_completed(user_word):
        print('voici votre mot :\n', user_word, '\n')
        letter = UI.get_letter()
        if reveal_char(user_word, goal_word, letter):
            print('cette lettre est bien dans le mot.')
        else:
            print('Non, cette lettre n\'est pas dans le mot.')
            nb_try += 1
    print('Bravo !\nVous avez trouvé le mot en', nb_try, 'essais !')

def main():
    UI.say_hello()  # explain the aim of the game
    dictionary = read_files.read_file('pendu/data/dictionary.txt').upper().split()  # get the file content fully uppered in a list of words
    game(dictionary)

main()