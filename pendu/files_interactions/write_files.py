  # write_file:
  # write [text] at the end of the file [name]
def write_file(name, text):
    try:  # trying to open the specified file
        file = open(name, 'a')
    except FileNotFoundError as error:
        print('[write_files.py :: write_file] ' + error)
        exit()
    file.write(str(text))