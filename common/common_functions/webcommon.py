from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
"""Common steps used in tests."""


def find_element(context, by, locator):

    by_list = ["id", "name", "xpath", "css selector",
               "tag name", "link text", "partial link text",
               "class name"]

    if by not in by_list:
        raise Exception("Locator not supported!!!",
                        "Supported locators: {0}".format(by_list))
    try:
        wait = WebDriverWait(context.driver, 10)
        element = wait.until(ec.presence_of_element_located((by, locator)))
        return element
    except:
        raise Exception("Couldn't find element!!!!")


def find_elements(context, by, locator):

    by_list = ["id", "name", "xpath", "css selector",
               "tag name", "link text", "partial link text",
               "class name"]
    if by not in by_list:
        raise Exception("Locator not supported!!!",
                        "Supported locators: {0}".format(by_list))
    try:
        element = context.driver.find_elements(by, locator)
        return element
    except:
        raise Exception("Couldn't find elements")


def assert_element_is_displayed(element):
    if not element.is_displayed():
        AssertionError("Element is not displayed")
