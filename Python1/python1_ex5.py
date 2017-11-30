import os

path = 'D:/Python_Exercise_final'

def displayFolder(folder):
    print(folder)
    list_of_files = os.listdir(folder)

    for i in list_of_files:
        path2 = os.path.join(folder, i)

        if os.path.isdir(path2):
            displayFolder(path2)
        else:
            print(path2)


displayFolder(path)