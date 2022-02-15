    # read_file :
    # open a file and ret its content
def read_file(name):
    file = open(name, 'r')
    content = file.read()
    file.close()
    return content
