import os
from xml.etree import ElementTree


def load_file_into_tree():
    '''Only the ElementTree class has a parse() method'''
    path = os.path.join(os.path.dirname(__file__), 'test.xml')
    tree = ElementTree.parse(path)
    print(type(tree)) # <class 'xml.etree.ElementTree.ElementTree'>


def load_string_into_tree():
    '''
    Only the ElementTree class has a fromstring() method
    - Same for getroot() method
    '''
    xml = '''<?xml version="1.0" encoding="utf-8"?>
    <SearchResults:searchresults xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SearchResults="http://www.zillow.com/static/xsd/SearchResults.xsd" xsi:schemaLocation="http://www.zillow.com/static/xsd/SearchResults.xsd https://www.zillowstatic.com/vstatic/80d5e73/static/xsd/SearchResults.xsd">
    <request>
    <address>279</address>
    <citystatezip>11211</citystatezip>
    </request>
    </SearchResults:searchresults>
    '''
    element = ElementTree.fromstring(xml)
    print(type(element)) # <class 'xml.etree.ElementTree.Element'>
    print(element) # <Element '{http://www.zillow.com/static/xsd/SearchResults.xsd}searchresults' at ...>
    #print(element.getroot()) # AttributeError


if __name__ == '__main__':
    #load_file_into_tree()
    load_string_into_tree()