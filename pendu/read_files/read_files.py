    # read_file:
    # open a file and return its content
def read_file(name):

    try:  # trying to open the specified file
        file = open(name, 'r')
    except FileNotFoundError:
        print('cannot find the file', name)
        exit()

    content = file.read()
    file.close()
    return content
