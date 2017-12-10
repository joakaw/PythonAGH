dictionary = {' i ': ' oraz ', ' oraz ': ' i ', ' nigdy ': ' prawie nigdy ', ' dlaczego ': ' czemu '}


def read_from_file(file_name):
    file = open(file_name, 'r')
    text = file.read()
    file.close()
    return text


def change_word(word, src_file_name,dst_file_name):
    src_file = open(src_file_name, 'r').readlines()
    dst_file = open(dst_file_name, 'w')
    for s in src_file:
        dst_file.write(s.replace(word, dictionary.get(word)))
        dst_file.close()


def change_text(file_name):
    words_to_delete = dictionary.keys()

    for word in words_to_delete:
        change_word(word, file_name,file_name)


file_to_change_word = 'testFile2.txt'

print("before:", read_from_file(file_to_change_word))
change_text(file_to_change_word)
print("after: ", read_from_file(file_to_change_word))