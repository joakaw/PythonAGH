#!/usr/bin/python

from xml.dom.minidom import parse
import xml.dom.minidom


def printing_collection(collection):
    books = collection.getElementsByTagName("book")
    for book in books:
        print("--Book--")
        if book.hasAttribute("id"):
            print("ID: " + book.getAttribute("id"))
            author = book.getElementsByTagName('author')[0]
            print("Type: " + author.childNodes[0].data)
            title = book.getElementsByTagName('title')[0]
            print("Title: " + title.childNodes[0].data)
            genre = book.getElementsByTagName('genre')[0]
            print("Genre: " + genre.childNodes[0].data)
            price = book.getElementsByTagName('price')[0]
            print("Price: " + price.childNodes[0].data)
            publish_date = book.getElementsByTagName('publish_date')[0]
            print("Publish_date: " + publish_date.childNodes[0].data)
            description = book.getElementsByTagName('description')[0]
            print("Description:  " + description.childNodes[0].data)


def replace_text(collection, node, node_value, new_text):
    books = collection.getElementsByTagName("book")
    for book in books:
        if book.hasAttribute("id"):
            node_data = book.getElementsByTagName(node)[0].childNodes[0].data
            title = book.getElementsByTagName('title')[0].childNodes[0].data
            if node_data == node_value:
                print("Changing ",title,": ", node, "from ", node_data, "to ", new_text)
                book.getElementsByTagName(node)[0].childNodes[0].replaceWholeText(new_text)


DOMTree = xml.dom.minidom.parse("testXmlFile.xml")
book_collection = DOMTree.documentElement

printing_collection(book_collection)
replace_text(book_collection, 'price', '5.95', '5.0')
new_file = open("testXmlFile2.xml", "w")
book_collection.writexml(new_file)
new_file.close()