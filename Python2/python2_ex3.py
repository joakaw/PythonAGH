#!/usr/bin/python

from xml.dom.minidom import parse
import xml.dom.minidom


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

replace_text(book_collection, 'price', '5.95', '5.0')
new_file = open("testXmlFile2.xml", "w")
book_collection.writexml(new_file)
new_file.close()