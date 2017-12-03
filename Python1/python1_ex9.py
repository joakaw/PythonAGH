
file_to_delete_word = 'testFile.txt'


def delete_word(word, file, dest_file):
    for s in file:
        dest_file.write(s.replace(word, ""))
        dest_file.close()


def read_from_file(file_name):
    file = open(file_name, 'r')
    text = file.read()
    file.close()
    return text


print("before:", read_from_file(file_to_delete_word))

source_file = open(file_to_delete_word, 'r').readlines()
destination_file = open(file_to_delete_word, 'w')

delete_word("slowo ", source_file,destination_file)
print("after: ", read_from_file(file_to_delete_word))
