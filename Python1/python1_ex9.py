
file_to_delete_word = 'testFile.txt'


def read_from_file(file_name):
    file = open(file_name, 'r')
    text = file.read()
    file.close()
    return text


def delete_word(word, src_file_name,dst_file_name):
    src_file = open(src_file_name, 'r').readlines()
    dst_file = open(dst_file_name, 'w')
    for s in src_file:
        dst_file.write(s.replace(word, " "))
        dst_file.close()

def clear_text(file_name):
    words_to_delete = [" sie ", " i ", " oraz ", " nigdy ", " dlaczego "]

    for word in words_to_delete:
        delete_word(word, file_name,file_name)


print("before:", read_from_file(file_to_delete_word))
clear_text(file_to_delete_word)
print("after: ", read_from_file(file_to_delete_word))
