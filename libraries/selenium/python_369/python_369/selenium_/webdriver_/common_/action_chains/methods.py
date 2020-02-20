# https://stackoverflow.com/questions/20316864/how-to-perform-right-click-using-selenium-chromedriver - perform right click
# https://stackoverflow.com/questions/11428026/select-an-option-from-the-right-click-menu-in-selenium-webdriver-java - select right-click option
# https://sqa.stackexchange.com/questions/22954/how-to-right-click-and-select-option-in-webdriverjs - apprently I can't select an item from the
# BROWSER's own right click menu?. Perhaps selenium is sending the click events beneath the browser right click menu?


import time
# Don't use this
#from selenium.webdriver.common.actions import pointer_actions
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from python_369 import introduction


def right_click():
    '''
    Use the action_chains module, not the actions package (which contains pointer_actions)
    - I don't know if the actions package is what I want or not, but I couldn't get it to work
    - I can't select an option from the right-click menu by simply chaining actions on the ActionChains object. Instead, use move_by_offset() or
      related functions. It's hacky, but it works
    '''
    browser = introduction.get_visible_firefox()
    browser.get('https://www.duckduckgo.com')
    element = browser.find_element_by_id('logo_homepage_link')
    # Don't do this
    #pa = pointer_actions.PointerActions()
    #pa.context_click(element)
    ac = action_chains.ActionChains(browser)
    # This didn't work
    #ac.context_click(element).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN)
    # This also isn't working
    #ac.context_click(element).move_by_offset(-50, -50).context_click()
    ac.perform()
    while True:
        pass


if __name__ == '__main__':
    right_click()
