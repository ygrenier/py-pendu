    # read_file:
    # open a file and return its content
def read_file(name):

    try:  # trying to open the specified file
        file = open(name, 'r')
    except FileNotFoundError as error:
        print('[write_files.py :: write_file] ' + error)
        exit()

    content = file.read()
    file.close()
    return content
