  # say_hello : print a welcoming message
def say_hello():
    print('Bienvenu dans le pendu !')

  # get_letter : get a letter entered by the use
def get_letter():
    letter = input('propose a letter:\n>> ')
    letter_is_valid = (len(letter) == 1) and (letter.isalpha())
    while not letter_is_valid:  # the entered letter is not valid
        if len(letter) != 1:
            letter = input('please, enter only one letter.\n>> ')
        elif not letter.isalpha():
            letter = input('please, enter a letter\n>> ')
    return letter