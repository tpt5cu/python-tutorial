from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


def get_headless_browser():
    opts = Options()
    opts.set_headless()
    assert opts.headless 
    browser = Firefox(options=opts)
    return browser


def common_attributes():
    '''
    - get_attribute(<name>): returns the value of the attribute
    - text: the text of the elme
    '''
    global browser
    prepare_browser()
    browser.get('https://www.duckduckgo.com') # Works
    elements = browser.find_elements_by_id('search_form_input_homepage')
    print(type(elements[0])) # <class 'selenium.webdriver.firefox.webelement.FirefoxWebElement'>
    print(elements[0]) # <selenium.webdriver.firefox.webelement.FirefoxWebElement (session="ed68e84b-c02b-294a-a5d9-1eff9c6497ad", element="51986b81-8f13-0144-a968-d9d72c04c9c1")>


if __name__ == '__main__':
    do()
