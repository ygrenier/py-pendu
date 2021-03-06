from threading          import activeCount
from files_interactions import *
from UI                 import *
from datetime           import datetime
import random
from colors.color_declarations import bcolors
from settings import settings

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
        print('\n' + bcolors.LIGHT_PURPLE + 'You already proposed this letter.\n' + bcolors.RESET)
        return 2

    for i in range(len(goal_word)):
        if goal_word[i] == letter:
            user_word[i] = letter
            letter_is_in_word = 1

    if letter_is_in_word:
        print(bcolors.GREEN + bcolors.BOLD + '\nThe letter ' + letter + ' is well in the word.\n' + bcolors.RESET)
    else:
        print(bcolors.RED + bcolors.BOLD + '\nNo, the letter ' + letter + ' is not in the word.\n' + bcolors.RESET)

    return letter_is_in_word

  # game_turn:
  # one turn in the game
def game_turn(nb_try, proposed_letters, user_word, goal_word, is_battle: bool = False):
    if not is_battle:
        UI.draw_hangman(nb_try)
    if len(proposed_letters) > 0:
        print('You already proposed the letters ' + bcolors.LIGHT_BLUE +  ", ".join(proposed_letters) + bcolors.RESET + ".")
    if not is_battle:
        print(bcolors.YELLOW + 'You still can do ' + str(7 - nb_try) + ' mistakes.' + bcolors.RESET)
    print('This is your word:\n' + bcolors.CYAN + bcolors.BOLD + " ".join(user_word) + bcolors.RESET)

    letter = UI.get_letter()
    return_code = reveal_char(user_word, goal_word, letter, proposed_letters)
    if return_code != 2:
        proposed_letters.append(letter)
        if return_code == 0:
            return False
        return True

  # game:
  # the main loop of the game
def game(goal_word, nb_players, name: str = 'nameless user'):

    user_word = ['_'] * len(goal_word)
    proposed_letters = []
    nb_try = 0

    time_before = datetime.now()

    while not goal_is_completed(user_word):
        if not game_turn(nb_try, proposed_letters, user_word, goal_word):
            nb_try += 1
        if nb_try > settings.NB_TURNS_MAX:
            UI.draw_hangman(8)
            print('You did not found the word (' + bcolors.CYAN + "".join(goal_word) + bcolors.RESET + ') in less than 7 mistakes.\nYou lost!\n')
            return 0

      # the user won
    print('Well done!\nYou found the word (' + bcolors.CYAN + "".join(goal_word) + bcolors.RESET + ') with', nb_try, 'mistakes !\n')

    game_time = datetime.now() - time_before
    if nb_players == 1:
        points = calculate_points(goal_word, nb_try, time_before, game_time)
        if points != 0:
            write_files.write_file('pendu/data/' + name + '_points.txt', str(points) + "\n")
            print('You have now a total of', UI.avg_points(name), 'points.\n')
            return points
        return 0
    else:
        return get_points(game_time, goal_word, nb_try)

  # calculate_points:
  # print how many points the player earned
def calculate_points(goal_word, nb_try, time_before, game_time):
    if nb_try > settings.NB_TURNS_MAX:
        print('You did not found the word, so you won no points this time.')
        return 0

    if nb_try == 0:
        print('Incredible... You found it with no mistakes!')
    points = get_points(game_time, goal_word, nb_try)
    print('You earned a score of', points, 'points by finding this word.')
    return points

  # get_points:
  # return the number of points won with the specified settings
def get_points(game_time, goal_word, nb_try):
    average_time = game_time / len(goal_word)
    return round(average_time.total_seconds()) * 6 + nb_try * 5

  # battle:
  # a mode where two players are fighting
def battle(nb_players):
    UI.clear()
    name = []
    for i in range(nb_players):
        print('\nplayer', i + 1, ':')
        tmp_name = input('What is your name?\n>> ')
        while (not tmp_name.isalnum()) or (len(tmp_name) > 15):
            tmp_name = input('Please, enter fewer than 15 letters and digits:\n>> ')
        name.append(tmp_name)

    dictionary = read_files.read_file('pendu/data/dictionary.txt').upper().split('\n')  # get the file content formatted to a list of words

    points = [0] * nb_players

    print('\nYou will have the same word to search, one after another.')
    print('after 3 words, the player who won the most of points win!')
    points = [0] * nb_players
    for i in range(1, settings.NB_BATTLE_ROUNDS + 1):
        input('\npress <enter> to continue. ')
        goal_word = dictionary[random.randint(0, len(dictionary) - 1)]
        tmp_points = [0] * nb_players
        for j in range(nb_players):
            UI.clear()
            print (bcolors.LIGHT_WHITE + bcolors.BOLD + name[j] + ' search the word.\n')
            tmp_points[j] = game(goal_word, 0)
            if tmp_points[j] > 0:
                points[j] += tmp_points[j]
            else:
                points[j] += settings.WORD_NOT_FOUND_PENALITY
        print('\n' + name[tmp_points.index(min(tmp_points))] + ' won this round.')
        print(name[points.index(min(points))] + ' is winning the battle.\n')
        for j in range(nb_players):
            print(name[j], 'points: ', points[j])

    print(name[points.index(min(points))], 'won the battle!\n')

    for i in range(nb_players):
        print(name[i], 'points: ', points[i])
    input('\npress <enter> to leave the battle. ')
    UI.clear()

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

  # play1:
  # play with one player
def play1():
    has_played = False
    name = UI.get_name(has_played)
    dictionary = read_files.read_file('pendu/data/dictionary.txt').upper().split('\n')  # get the file content formatted to a list of words
    play = True
    while play:
        points = game(dictionary[random.randint(0, len(dictionary) - 1)], 1, name)
        if not has_played and points > 0:
            write_files.write_file('pendu/data/index.txt', name + "\n")
        play = UI.play_again()

  # play2:
  # play with two players
def play2():
    play = True
    while play:
        game(UI.get_user_word().upper(), 2)
        play = UI.play_again()

  # main:
  # start all others functions
def main():
    UI.clear()
    UI.say_hello()  # explain the aim of the game

    commands = ['play1', 'play2', 'top5', 'battle', 'exit', 'help']

    while True:
        cmd = start(commands)
        if cmd == 1: # entered command: play1
            play1()
        elif cmd == 2: # entered command: play2
            play2()
        elif cmd == 3: # entered command: top5
            UI.best_scores()
        elif cmd == 4: # entered command: battle
            battle(UI.get_nb_players())
        elif cmd == 5: # entered command: exit
            return
        elif cmd == 6: # entered command: help
            UI.command_list()

main()