from behave import given, when, then
from common.common_functions import webcommon
from common.common_configs.url_config import URLCONFIG
from common.common_configs.locators_config import LOCATORS
import time


@given('I open "{url}"')
def open_the_webpage(context, url):
    url = URLCONFIG.get(url)
    context.driver.get(url)


@given('the "{element}" is visible')
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
    locate_element = webcommon.find_element(context, locator_type, locator_text)
    locate_element.send_keys(course)


@when('I click on the "{element}"')
def click_on_search_button(context, element):
    # locators
    locator_info = LOCATORS.get(element)
    locator_type = locator_info['by']
    locator_text = locator_info['locator']
    locate_element = webcommon.find_element(context, locator_type, locator_text)
    locate_element.click()
    locate_element.click()


@then('the "{element}" is loaded with searched {course} courses')
def results_page(context, element, course):
    locator_info = LOCATORS.get(element)
    locator_type = locator_info['by']
    locator_text = locator_info['locator']
    locate_element = webcommon.find_element(context, locator_type, locator_text)
    webcommon.assert_element_is_displayed(locate_element)

