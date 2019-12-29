# https://stackoverflow.com/questions/31043997/whats-difference-between-findall-and-iterfind-of-xml-etree-elementtree


import os
from xml.etree import ElementTree as ET


'''
If an XPath expression starts with "/", it always represents an absolute path to an element
'''


def _get_tree_root():
    path = os.path.join(os.path.dirname(__file__), 'test.xml')
    root = ET.parse(path).getroot()
    return root


def element_truthiness():
    '''
    Caution: elements with no subelements will test as False. This behavior will change in future versions. Use specific len(elem) or elem is None
    test instead.
    - This is tricky because a nonexistant element is None, which is also False
    - Therfore, detecting a False Element does not tell me if it 1) doesn't exist or 2) exists, but doesn't have children
    '''
    root = _get_tree_root()
    request_address = list(root.iterfind('request/address'))[0]
    # This element exists, but has no children
    print(type(request_address)) # <class 'xml.etree.ElementTree.Element'>
    print(len(request_address)) # 0
    print(bool(request_address)) # False


def iterfind_():
    '''
    <Element>.iterfind() returns a generator, so it's faster than findall() when I simply want to iterate over all elements in the tree because it
    doesn't create a list
    - iterfind() only searches direct children by tag name. That's why an XPath expression is more useful
    - The children of an element can be easily looked-up by iterating over the element itself (or using the list constructor)
    '''
    root = _get_tree_root()
    # This doesn't work because the root element doesn't have any direct children with the tag "address"
    #matching_elements = root.iterfind('address') 
    matching_elements = root.find('response').find('results').find('result').iterfind('address')
    for e in matching_elements:
        print([sub.text for sub in e])
    # .// (XPath syntax): "." select current node, "//" select nodes in the document anywhere in the tree from the current node that match the selection
    #matching_elements = root.iterfind('//address') # SyntaxError: cannot use absolute path on element
    matching_elements = root.iterfind('.//address')
    print(type(matching_elements)) # <type 'generator'>
    for e in matching_elements:
        print([sub.text for sub in e])


def iter_():
    '''
    <Element>.iter() implicitly searches the entire tree for elements with the matching tag.
    - iter() does not appear to accept XPath expressions
    - iter() is more blunt than iterfind()
    '''
    root = _get_tree_root()
    # This includes the <request> contents, which I don't want
    #for e in root.iter('address'): 
    # This doesn't work at all
    #for e in root.iter('response//address'):
    # This works perfectly, but doesn't use iter()!
    for e in root.iterfind('response//address'):
        print([sub.text for sub in e])


def get_results_count():
    '''
    The children of an element are directly subscriptable
    '''
    root = _get_tree_root()
    # Generators don't have __len__
    #print(len(root.iterfind('response/results/result')))
    # The address subtrees of all results
    addresses = list(root.iterfind('response/results/result//address'))
    print(len(addresses)) # 16
    # The text of the first child of the first element in the list of addresses
    print(addresses[0][0].text) # 279 Hewes St


def handle_falsy_element():
    '''
    Ternary assignment is not unique to Elements. However, what is nice is that the first expression is never evaluated unless the conditional is
    True. Therefore, I won't get NoneType AttributeErrors so long as I detect that the element exists first
    '''
    root = _get_tree_root()
    first_address = list(root.iterfind('response/results/result//address'))[0]
    street = first_address.find('meat').text if first_address.find('meat') is not None else ''
    print(street) # ""
    street = first_address.find('street').text if first_address.find('street') is not None else ''
    print(street) # 279 Hewes St


if __name__ == '__main__':
    #element_truthiness()
    #iterfind_()
    #iter_()
    #get_results_count()
    handle_falsy_element()