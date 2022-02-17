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
        print('You already proposed this letter.\n')
        return 2

    for i in range(len(goal_word)):
        if goal_word[i] == letter:
            user_word[i] = letter
            letter_is_in_word = 1

    if letter_is_in_word:
        print('This letter is well in the word.\n')
    else:
        print('No, this letter is not in the word.\n')

    return letter_is_in_word

  # game:
  # the main loop of the game
def game(goal_word, nb_players, name: str = 'nameless user'):

    user_word = ['_'] * len(goal_word)
    proposed_letters = []
    nb_try = 0

    time_before = datetime.now()

    while not goal_is_completed(user_word):
        UI.draw_hangman(nb_try)
        if len(proposed_letters) > 0:
            print('You already proposed the letters:', ", ".join(proposed_letters), ".")
        print('You still can do', 7 - nb_try, 'mistakes.')
        print('This is your word:\n', " ".join(user_word))

        letter = UI.get_letter()
        return_code = reveal_char(user_word, goal_word, letter, proposed_letters)
        if return_code != 2:
            proposed_letters.append(letter)
            if return_code == 0:
                nb_try += 1

        if nb_try > 7:
            UI.draw_hangman(8)
            print('You did not found the word (', "".join(goal_word), ') in less than 7 mistakes.\nYou lost!')
            return nb_try

      # the user won
    print('Well done!\nYou found the word (', "".join(goal_word), ') with', nb_try, 'mistakes !\n')

    game_time = datetime.now() - time_before
    if nb_players == 1:
        points = calculate_points(goal_word, nb_try, time_before, game_time)
        if points != 0:
            write_files.write_file('pendu/data/' + name + '_points.txt', str(points) + "\n")
            point_average = UI.avg_points(name)
            print('You have now a total of', point_average, 'points.')

    return nb_try

  # calculate_points:
  # print how many points the player earned
def calculate_points(goal_word, nb_try, time_before, game_time):
    if nb_try > 7:
        print('You did not found the word, so you won no points this time.')
        return 0

    if nb_try == 0:
        print('Incredible... You found it with no mistakes!')
    average_time = game_time / len(goal_word)
    points = round(average_time.total_seconds()) * 6 + nb_try * 5
    print('You earned a score of', points, 'points by finding this word.')
    return points

  # start:
  # get the entered command
def start(commands):
    print('enter a command:')
    print('(type <help> for a command list)')
    cmd = input('>> ')
    while True:
        if cmd in commands:
            return commands.index(cmd) + 1
        else:
            cmd = input('Please, enter a valid command (<help> for a list)\n>> ')

    return 1

  # main:
  # start all others functions
def main():
    UI.clear()
    UI.say_hello()  # explain the aim of the game

    commands = ['play1', 'play2', 'top5', 'battle', 'exit', 'help']

    while True:
        cmd = start(commands)
        if cmd == 1: # entered command: play1
            name = UI.get_name()
            dictionary = read_files.read_file('pendu/data/dictionary.txt').upper().split('\n')  # get the file content formatted to a list of words
            play = True
            while play:
                game(dictionary[random.randint(0, len(dictionary) - 1)], 1, name)
                if not UI.play_again():
                    play = False
        elif cmd == 2: # entered command: play2
            play = True
            while play:
                game(UI.get_user_word().upper(), 2)
                if not UI.play_again():
                    play = False
        elif cmd == 3: # entered command: top5
            UI.best_scores()
        elif cmd == 4: # entered command: battle
            pass
        elif cmd == 5: # entered command: exit
            return
        elif cmd == 6: # entered command: help
            UI.command_list()

main()