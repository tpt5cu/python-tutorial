# https://stackoverflow.com/questions/1912434/how-do-i-parse-xml-in-python
# https://docs.python.org/2/library/xml.etree.elementtree.html
# https://stackoverflow.com/questions/1181888/what-does-xmlns-in-xml-mean

import os
import xml.etree.ElementTree as ET


"""
The ElementTree XML API in native Python is the easiest and most straightforward wasy to parse XML in Python, though not the fastest. There are two
basic types in the ElementTree interface: ElementTree and Element.
- ElementTree encapsulates operations on the entire XML tree
- Element encapsulates operations on a single Element in the tree

There's an expression language called XPath that uses expression to explore an XML tree. I'm not dealing with that right now.
"""

"""
- $ xmlns:<str>='<URI>' $: "xmlns" defines an XML namespace. <str> is the "namespace prefix" and <URI> is the "namespace URI".
"""

def get_xml_root():
    """The root of an xml document is treated as an Element like any other"""
    filepath = os.path.join(os.path.dirname(__file__), "test.xml")
    tree = ET.parse(filepath)
    root = tree.getroot()
    #print(type(root)) # <class 'xml.etree.ElementTree.Element>
    # <Element>.tag identifies what kind of data this Element represents
    #print(root.tag)
    #print(root.attrib)
    return root


def get_direct_children():
    """
    <Element>.find() will ONLY return the FIRST direct child of Element if it exists, else None. Iterating over an Element will iterate over its
    DIRECT children only.
    """
    root = get_xml_root()
    request = root.find("request")
    print(request.tag) # request
    address = root.find("address")
    # There is no DIRECT subelement of Element with the tag "address", so <Element>.find() returns None
    print(address) # None
    for direct_child in root:
        print(direct_child.tag) # request message response


def get_specific_elements():
    """
    It appears I have to manually parse for descendents that I'm interested in. There is no "find the first descendent at an arbitrary depth that
    matches some criteria" function.
    """
    root = get_xml_root()
    element = root.find("response").find("results").find("result").find("address")
    address = (element.find("street").text + ", " + element.find("city").text + ", " +
        element.find("state").text + " " + element.find("zipcode").text)
    print(address)


if __name__ == "__main__":
    #get_xml_root()
    #get_direct_child()
    get_specific_elements()