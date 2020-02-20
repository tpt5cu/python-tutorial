# https://stackoverflow.com/questions/48188978/how-to-get-browser-console-error-messages-using-selenium-webdriver-python
# https://stackoverflow.com/questions/59026421/python-selenium-unable-to-get-browser-console-logs
# https://stackoverflow.com/questions/17385779/how-do-i-load-a-javascript-file-into-the-dom-using-selenium/17387127 - load <script> into page
# https://stackoverflow.com/questions/12729265/switch-tabs-using-selenium-webdriver-with-java - switch tabs


'''Need to use Chrome instead of Firefox to access browser console logs'''


from python_369 import introduction


def get_webpage():
    browser = introduction.get_headless_firefox()
    browser.get('https://www.duckduckgo.com')
    print(browser.page_source)


def find_elements_by_id():
    browser = introduction.get_headless_firefox()
    browser.get('https://www.duckduckgo.com')
    elements = browser.find_elements_by_id('search_form_input_homepage')
    print(type(elements[0])) # <class 'selenium.webdriver.firefox.webelement.FirefoxWebElement'>
    print(elements[0]) # <selenium.webdriver.firefox.webelement.FirefoxWebElement (session="5187cd64-fde7-6246-b84a-2b4ad5473bcf", element="48281252-b0f8-3a4a-b31d-71b63b6cbdda")>
    

def perform_right_click_action():
    '''See action_chains'''
    pass


def switch_to_new_tab():
    '''
    1) browser.window_handles returns a list
    2) browser.switch_to.window(<item from the list>)
    '''
    pass


def execute_synchronous_script():
    browser = introduction.get_visible_firefox()
    browser.get('https://www.duckduckgo.com')
    browser.execute_script('alert("Hello from selenium");')
    while True:
        pass


def execute_asynchronous_script():
    browser = introduction.get_visible_firefox()
    browser.get('https://www.duckduckgo.com')
    browser.execute_script('window.setTimeout(function() { alert("Hello from setTimeout selenium") }, 3000);')
    while True:
        pass


def load_external_script_into_document():
    browser = introduction.get_visible_firefox()
    browser.get('https://developer.mozilla.org/en-US/docs/Web')
    browser.execute_script('\
    s = document.createElement("script"); \
    s.setAttribute("src", "./my_script.js"); \
    s.setAttribute("type", "text/javascript"); \
    document.head.append(s); \
    ')
    while True:
        pass

if __name__ == '__main__':
    #get_webpage()
    #find_elements_by_id()
    #execute_synchronous_script()
    #execute_asynchronous_script()
    load_external_script_into_document()
