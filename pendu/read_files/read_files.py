    # read_file :
    # open a file and ret its content
def read_file(name):

    try:
        file = open(name, 'r')
    except FileNotFoundError:
        print('cannot find the file', name)
        exit()

    content = file.read()
    file.close()
    return content
