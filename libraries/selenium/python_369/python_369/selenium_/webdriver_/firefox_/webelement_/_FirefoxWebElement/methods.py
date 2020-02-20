# https://stackoverflow.com/questions/51865300/python-selenium-keep-browser-open


from python_369 import introduction
from selenium.webdriver.common.keys import Keys


def get_attribute_value():
    browser = introduction.get_headless_firefox()
    browser.get('https://www.duckduckgo.com')
    elements = browser.find_elements_by_id('search_form_input_homepage')
    val = elements[0].get_attribute('value')
    print(type(val)) # <class 'str'>
    print(val) # ''


def type_and_enter_input():
    '''
    There doesn't appear to be a way to get a Firefox browser to stay open after the function completes. It looks possible with Chrome
    '''
    browser = introduction.get_visible_firefox()
    browser.get('https://www.duckduckgo.com')
    elements = browser.find_elements_by_id('search_form_input_homepage')
    input_ = elements[0]
    input_.send_keys(['Cats'])
    input_.send_keys(Keys.RETURN) # simulate pressing enter inside of the search box
    #while True:
    #    pass


def find_elements_by_link_text():
    '''
    This method appears to search elements by their text node content, not their <a href=...> content
    '''
    pass


if __name__ == '__main__':
    #get_attribute_value()
    type_and_enter_input()
