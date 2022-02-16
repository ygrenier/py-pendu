from os                 import system
from sys                import platform
from statistics         import mean
from files_interactions import *

  # say_hello:
  # print a welcoming message
def say_hello():
    print('Welcome in the hangman game!')
    print('You will have to find a word.')
    print('according to your time and your number of mistakes, you will earn some points. Note that in 2 players mode, you will not earn points.')
    print('if you want, your final goal will be to have the fewer point that you can!\n')
    point_average = mean(int(x) for x in read_files.read_file('pendu/data/points.txt').splitlines())
    print('actually, you have an average of', point_average, 'points.')
    if point_average < 10:
        print('You are an excellent player!\n')
    elif point_average < 20:
        print('You are a realy good player!')
    elif point_average < 30:
        print('You are a good player.\n')
    elif point_average < 40:
        print('You may do better!\n')
    elif point_average < 50:
        print('You are not realy good at this game...\nEverybody has strong points and weak points.\n')
    else:
        print('You are maybe not French?\n')

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
            letter = getChar()
            letter_is_valid = (len(letter) == 1) and (letter.isalpha())
        elif len(letter) < 1:
            print('please, enter one letter.\n>> ', end='')
            letter = getChar()
            letter_is_valid = (len(letter) == 1) and (letter.isalpha())
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
    word = input('The first player enter the word to search:\n>> ')
    while not word.isalpha():
        word = input('Please, enter only letters.\n>> ')

    if 'win' in platform: # if it's running on windows
        system('cls')
    elif 'linux' in platform: # if it's running on linux
        system('clear')
    else:
        for i in range(100):
            print()
        print('Your OS is not taken care by this program, so it only printed 100 empty lines.')
    print('The first player entered a word. You have to find it!\n')

    return word
