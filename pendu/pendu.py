from threading          import activeCount
from files_interactions import *
from UI                 import *
from datetime           import datetime
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
def game(goal_word, nb_players: int = ...):

    print('[DEBUG]: the word is', goal_word)
    user_word = ['_'] * len(goal_word)
    proposed_letters = []
    nb_try = 0

    time_before = datetime.now()

    while not goal_is_completed(user_word):
        if len(proposed_letters) > 0:
            print('You already proposed the letters:', ", ".join(proposed_letters), ".")
        print('You still can do', 7 - nb_try, 'mistakes.')
        print('This is your word:\n', " ".join(user_word))

        letter = UI.get_letter()
        return_code = reveal_char(user_word, goal_word, letter, proposed_letters)
        if return_code == 2:
            print('You already proposed this letter.\n')
        elif return_code == 1:
            print('This letter is well in the word.\n')
            proposed_letters.append(letter)
        else:
            print('No, this letter is not in the word.\n')
            proposed_letters.append(letter)
            nb_try += 1

        if nb_try > 7:
            print('You did not found the word (', "".join(goal_word), ') in less than 7 mistakes.\nYou lost!')
            return nb_try

      # the user won
    print('Well done!\nYou found the word (', "".join(goal_word), ') with', nb_try, 'mistakes !\n')

    game_time = datetime.now() - time_before
    if nb_players == 1:
        points = calculate_points(goal_word, nb_try, time_before, game_time)
        if points != 0:
            write_files.write_file('pendu/data/points.txt', str(points) + "\n")

    return nb_try

  # calculate_points:
  # print how many points the player earned
def calculate_points(goal_word, nb_try, time_before, game_time):
    if nb_try > 7:
        print('You did not found the word, so you won no points this time.')
        return 0

    average_time = 0
    if nb_try == 0:  # risk of division by 0
        print('Incredible... You found it with no mistakes!')
        average_time = game_time / len(goal_word)
    else:
        average_time = game_time / len(goal_word)
    print('[DEBUG] average time:', round(average_time.total_seconds()))
    print('[DEBUG] nb_try:', nb_try)
    points = round(average_time.total_seconds()) * 6 + nb_try * 5
    print('You earned a score of', points, 'points by finding this word.')
    return points

def main():
    UI.say_hello()  # explain the aim of the game
    nb_players = UI.get_nb_players()

    if nb_players == 1:
        dictionary = read_files.read_file('pendu/data/dictionary.txt').upper().split('\n')  # get the file content fully and formatted to a list of words

        while True:
            game(dictionary[random.randint(0, len(dictionary) - 1)])
            answer = input('Do you want to play again?\nPlease answer y or n:\n>> ')
            while answer != 'y': # if answer == 'n', the return statement is executed.
                if answer == 'y':
                    pass
                elif answer == 'n':
                    return
                else:
                    answer = input('please, enter y for yes or n for no.\nDo you want to play again?\n>> ')
    else:
        while True:
            game(UI.get_user_word().upper())
            answer = input('Do you want to play again?\nPlease answer y or n:\n>> ')
            while answer != 'y': # if answer == 'n', the return statement is executed.
                if answer == 'y':
                    pass
                elif answer == 'n':
                    return
                else:
                    answer = input('please, enter y for yes or n for no.\nDo you want to play again?\n>> ')


main()