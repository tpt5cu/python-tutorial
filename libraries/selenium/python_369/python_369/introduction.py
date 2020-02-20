# https://pypi.org/project/selenium/
# https://realpython.com/modern-web-automation-with-python-and-selenium/
# https://duo.com/decipher/driving-headless-chrome-with-python


from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


def get_headless_firefox():
    opts = Options()
    opts.set_headless()
    assert opts.headless 
    return Firefox(options=opts)


def get_visible_firefox():
    return Firefox()