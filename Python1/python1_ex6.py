from PIL import Image

path = "D:\Python_Exercise_final\Python1"
imageTitle = 'python'
path_jpg = path + '\\' + imageTitle + '.jpg'
path_png = path + '\\' + imageTitle + '.png'

Image\
    .open(path_jpg)\
    .save(path_png)
