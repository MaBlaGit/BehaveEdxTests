from behave import given, when, then
from common.common_functions import webcommon
from common.common_configs.url_config import URLCONFIG
from common.common_configs.locators_config import LOCATORS
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@given('I open "{url}"')
def open_the_webpage(context, url):
    url = URLCONFIG.get(url)
    context.driver.get(url)


@given('the "{element}" is visible')
@when('The "{element}" is visible')
@then('the "{element}" is visible')
def search_if_element_is_visible(context, element):
    # locators
    locator_info = LOCATORS.get(element)
    locator_type = locator_info['by']
    locator_text = locator_info['locator']
    # find element
    web_element = webcommon.find_element(context, locator_type, locator_text)
    webcommon.assert_element_is_displayed(web_element)


@when('I in the "{element}" enter {course}')
def locate_and_send_keys(context, element, course):
    # locators
    locator_info = LOCATORS.get(element)
    locator_type = locator_info['by']
    locator_text = locator_info['locator']
    # find element
    locate_element = webcommon.find_element(context, locator_type, locator_text)
    locate_element.send_keys(course)


@when('I click on the "{element}"')
def click_on_search(context, element):
    # locators
    locator_info = LOCATORS.get(element)
    locator_type = locator_info['by']
    locator_text = locator_info['locator']
    locate_element = webcommon.find_element(context, locator_type, locator_text)
    if context.driver.name == "firefox":
        locate_element.click()
    elif context.driver.name == "chrome":
        locate_element.click()
        locate_element.click()


@when('I click on the "{button}" button')
def click_on_button(context, button):
    # locators
    locator_info = LOCATORS.get(button)
    locator_type = locator_info['by']
    locator_text = locator_info['locator']
    context.driver.execute_script("window.scrollBy(0, 1000)")
    # find element
    find_button = webcommon.find_element(context, locator_type, locator_text)
    find_button.click()


@when('I select "{avatar}"')
def click_on_avatar(context, avatar):
    # locators
    locator_info = LOCATORS.get(avatar)
    locator_type = locator_info['by']
    locator_text = locator_info['locator']
    # find element
    locate_element = webcommon.find_element(context, locator_type, locator_text)
    locate_element.click()


@then('the "{element}" is loaded with searched {course} courses')
def results_page(context, element, course):
    # locators
    locator_info = LOCATORS.get(element)
    locator_type = locator_info['by']
    locator_text = locator_info['locator']
    # find element
    locate_element = webcommon.find_element(context, locator_type, locator_text)
    webcommon.assert_element_is_displayed(locate_element)


@when('I choose the "{element}" from the drop down list')
def click_on_the_first_element_from_drop_down(context, element):
    # locators
    locator_info = LOCATORS.get(element)
    locator_type = locator_info['by']
    locator_text = locator_info['locator']
    # find element
    webcommon.find_element(context, locator_type, locator_text)
    action = ActionChains(context.driver)
    action.key_down(Keys.ARROW_DOWN)
    action.key_down(Keys.ENTER)
    action.perform()
