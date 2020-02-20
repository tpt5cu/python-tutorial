

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


def get_headless_browser():
    opts = Options()
    opts.set_headless()
    assert opts.headless 
    return Firefox(options=opts)


def test_safari():
    '''
    A selenium driver exists for Safari, but it's not headless as far as I can tell
    '''
    from selenium.webdriver import Safari
    print(dir(Safari), '\n')
    from selenium.webdriver import safari
    print(dir(safari))
    browser = Safari()
    browser.get('https://duckduckgo.com')


def test_firefox():
    '''
    - Need to install a driver first: https://github.com/mozilla/geckodriver/releases
        - $ wget -P /Users/austinchang/tutorials/python/libraries/selenium/python_369 https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-macos.tar.gz
    - browser object
        - Useful browser attributes:
            - page_source: the actual html received
            - title: the title of the web page
            - current_url: the url of the page that is currently loaded into the session
        - There is no post() method, only get()
        - 
    '''
    from selenium.webdriver import Firefox
    from selenium.webdriver.firefox.options import Options
    opts = Options()
    opts.set_headless()
    assert opts.headless  # Operating in headless mode
    browser = Firefox(options=opts)
    browser.get('http://localhost:5000')
    #browser.get('https://www.duckduckgo.com') # Works
    print(browser.page_source)


if __name__ == '__main__':
    #test_safari()
    test_firefox()

# - distNetViz.py isn't sufficient because it renders distNetViz.html in a static context
# 1) Start a real web server or a test web server?
#   - Real web server. The web server process never returns, so how would I know when it was ready? I could start a web server in the test and then
#     poll it until I got something. Actually, starting the web server takes forever. Starting a new web server with every test run will take a long
#     time, so I should just use a real web server since it will probably be running already
# 2) Log in as test
#   2a) View feeder owned by test
#   2b) View feeder owned by public
# 3) Log in as admin
#   3a) View feeder owned by admin
#   3b) View feeder owned by public
#   3c) View feeder owned by test
