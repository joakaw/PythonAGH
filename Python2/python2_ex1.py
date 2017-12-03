

def write_to_file(file_name, text):
    file = open(file_name, 'w')
    file.write(text)
    file.close()

def read_from_file(file_name):
    file = open(file_name, 'r')
    return file.read()


file_name = 'testFile.txt'
write_to_file(file_name, "Zadania z programowania w jezyku skryptowym Python")
print(read_from_file(file_name))
