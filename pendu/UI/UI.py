  # say_hello:
  # print a welcoming message
def say_hello():
    print('Welcome in the hangman game!')

  # get_letter:
  # get a letter entered by the use
def get_letter():
    letter = input('try a letter:\n>> ')
    letter_is_valid = (len(letter) == 1) and (letter.isalpha())

    while not letter_is_valid:  # the entered letter is not valid
        if len(letter) > 1:
            letter = input('please, enter only one letter.\n>> ')
        elif len(letter) < 1:
            letter = input('please, enter one letter.\n>> ')
        elif letter.isalpha():
            return letter.upper() # all letters are upped, to compare them easier
        else:
            letter = input('please, enter a letter\n>> ')

  # get_nb_players:
  # return the entered numbers of players (1 or 2)
def get_nb_players():
    nb_players = input('Are you 1 player or 2 players ? (1/2)\n>> ')
    number_is_valid = (nb_players == 1) or (nb_players == 2)

    while not number_is_valid:  # the entered number is not 1 or 2
        nb_players = input('please, enter 1 or 2\n>> ')
        number_is_valid = (nb_players == 1) or (nb_players == 2)

    return nb_players