

def change_word(file, dest_file):
    dictionary = {' i ': ' oraz ', ' oraz ': ' i ', ' nigdy ': ' prawie nigdy ', ' dlaczego ': ' czemu '}
    for s in file:
        for i in dictionary.keys():
            dest_file.write(s.replace(i, dictionary.get(i)))
            print("looking for: ",i )
        print("looking for: ", s)

    dest_file.close()


def read_from_file(file_name):
    file = open(file_name, 'r')
    text = file.read()
    file.close()
    return text


file_to_change_word = 'testFile2.txt'
print("before:", read_from_file(file_to_change_word))

source_file = open(file_to_change_word, 'r').readlines()
destination_file = open(file_to_change_word, 'w')

change_word(source_file, destination_file)
print("after: ", read_from_file(file_to_change_word))