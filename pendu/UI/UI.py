  # say_hello:
  # print a welcoming message
from statistics import mean
from files_interactions import *
def say_hello():
    print('Welcome in the hangman game!')
    print('You will have to find a word.')
    print('according to your time and your number of mistakes, you will earn some points.')
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


 # get_letter:
  # get a letter entered by the use
def get_letter():
    letter = input('try a letter:\n>> ')
    letter_is_valid = (len(letter) == 1) and (letter.isalpha())

    while not letter_is_valid:  # the entered letter is not valid
        if len(letter) > 1:
            letter = input('please, enter only one letter.\n>> ')
            letter_is_valid = (len(letter) == 1) and (letter.isalpha())
        elif len(letter) < 1:
            letter = input('please, enter one letter.\n>> ')
            letter_is_valid = (len(letter) == 1) and (letter.isalpha())
        elif letter.isalpha():
            return letter.upper() # all letters are upped, to compare them easier
        else:
            letter = input('please, enter a letter\n>> ')
            letter_is_valid = (len(letter) == 1) and (letter.isalpha())

    return letter.upper()