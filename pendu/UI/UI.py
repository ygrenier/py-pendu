from os                 import system
from sys                import platform
from statistics         import mean
from files_interactions import *

  # clear:
  # clear the consol
def clear():
    if 'win' in platform: # if it's running on windows
        system('cls')
    elif 'linux' in platform: # if it's running on linux
        system('clear')
    else:
        for i in range(100):
            print()
        print('Your OS is not taken care by this program, so it only printed 100 empty lines. Please don\'t cheat!')


  # say_hello:
  # print a welcoming message
def say_hello():
    print('Welcome in the hangman game!')
    print('You will have to find a word.')
    print('according to your time and your number of mistakes, you will earn some points. Note that in 2 players mode, you will not earn points.')
    print('if you want, your final goal will be to have the fewer point that you can!\n')

  # getChar:
  # code from https://stackoverflow.com/questions/510357/how-to-read-a-single-character-from-the-user
  # read only one char (don't wait for a '\n')
def getChar():
    try:
        # for Windows-based systems
        import msvcrt # If successful, we are on Windows
        return str(msvcrt.getch())[2]

    except ImportError:
        # for POSIX-based systems (with termios & tty support)
        import tty, sys, termios  # raises ImportError if unsupported

        fd = sys.stdin.fileno()
        oldSettings = termios.tcgetattr(fd)

        try:
            tty.setcbreak(fd)
            answer = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, oldSettings)

        return answer

  # get_letter:
  # get a letter entered by the use
def get_letter():
    print('try a letter:\n>> ', end='')
    letter = getChar()
    letter_is_valid = (len(letter) == 1) and (letter.isalpha())

    while not letter_is_valid:  # the entered letter is not valid
        if len(letter) > 1:
            print('please, enter only one letter.\n>> ', end='')
        elif len(letter) < 1:
            print('please, enter one letter.\n>> ', end='')
        elif letter.isalpha():
            return letter.upper() # all letters are upped, to compare them easier
        else:
            print('please, enter a letter\n>> ', end='')
        letter = getChar()
        letter_is_valid = (len(letter) == 1) and (letter.isalpha())

    return letter.upper()

  # get_nb_players:
  # ask the players how many there are (1 ou 2)
def get_nb_players():
    answer = input('Do you play with one player or two players?\n>> ')
    while (not answer.isdigit()) or ((int(answer) != 1) and (int(answer) != 2)) :
        answer = input('Please enter 1 or 2.\n>> ')
    return int(answer)

  # get_user_word:
  # ask the first player to enter the word
def get_user_word():
    clear()
    word = input('The first player enter the word to search:\n>> ')
    while not word.isalpha():
        word = input('Please, enter only letters.\n>> ')
    clear()
    print('The first player entered a word. You have to find it!\n')

    return word

def draw_hangman(n):
    hangman =\
    [
        """
        _|_
        """,
        """
         |
         |
         |
        _|_
        """,
        """
          _____
         |
         |
         |
        _|_
        """,
        """
          _____
         |    |
         |
         |
        _|_
        """,
        """
          _____
         |    |
         |    O
         |
        _|_
        """,
        """
          _____
         |    |
         |    O
         |    |
        _|_
        """,
        """
          _____
         |    |
         |    O
         |   '|'
        _|_
        """,
        """
          _____
         |    |
         |    O
         |   '|'
        _|_  ' '
        """,
        """
         _______
        | X   X |
        |   °   |
        |  ---  |
         ^^^^^^^
        """
    ]
    print(hangman[n], "\n")

  # play_again:
  # get if the player want to play again (or not)
def play_again():
    answer = input('Do you want to play again?\nPlease answer y or n:\n>> ')
    while True:
        if answer == 'y' or answer == 'y':
            clear()
            return True
        elif answer == 'n' or answer == 'N':
            clear()
            return False
        else:
            answer = input('please, enter y for yes or n for no.\nDo you want to play again?\n>> ')

  # get_name:
  # get the name of the user
def get_name(has_played):
    name = input('What is your name?\n>> ')
    while (not name.isalnum()) or (len(name) > 15):
        name = input('Please, enter fewer than 15 letters and digits:\n>> ')
    points_average = avg_points(name)
    if points_average == 0:
        print('you have not collected points so far.')
        has_played = False
    else:
        print('You have actually an average of', points_average, 'points.')
        has_played = True
    input('\nPress enter to begin...')
    clear()
    return name

  # avg_points:
  # return the average of points of the user [name]
def avg_points(name):
    try:
        avg_points = mean(int(x) for x in read_files.read_file('pendu/data/' + name + '_points.txt').splitlines())
        return avg_points
    except:
        return 0

  # best_scores:
  # show the score board
def best_scores():
    scores = {}
      # create a dictionary with all usernames and scores
    for username in read_files.read_file('pendu/data/index.txt').splitlines():
        scores[username] = avg_points(username)
      # sort it
    sorted_scores = dict(sorted(scores.items(), key= lambda x:x[1]))
      # print the betters
    print('\nbest players:')
    i = 1
    for name, score in sorted_scores.items():
        print(i, '. ', name, ' : ', score)
        if i >= 5:
            break
        i += 1
    print()

def command_list():
    print('A short command list:')
    print(
'''
top5   : print the 5 better players
play1  : play in 1 player mode
play2  : play in 2 player mode
battle : play in battle mode
exit   : leave the game
help   : print this command list
''')