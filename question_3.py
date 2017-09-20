# Write a function in Python that takes a list of strings and returns a single
# string that is an HTML unordered list (<ul>...</ul>) of those strings.
# You should include a brief explanation of your code. Then, what would
# you have to consider if the original list was provided by user input?

from xml.dom.minidom import *
from sys import stdout

def get_html_list(alist):

    doc = Document();
    node = doc.createElement('ul')
    for i in range(0, len(alist)):
        list_item = doc.createElement('li')
        list_item.appendChild(doc.createTextNode(str(alist[i])))
        node.appendChild(list_item)
    doc.appendChild(node)
    return doc

if __name__ == '__main__':
    # test_list = ['a', 'b', 'c', 'd']
    test_list = [1, 2, 3, 4]
    get_html_list(test_list).writexml(stdout)

# node contents must be a string, otherwise it will raise error.
