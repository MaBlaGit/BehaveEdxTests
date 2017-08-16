from selenium import webdriver

"""Fixtures which set up and tear down environment before each scenario."""


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


def after_scenario(context, scenario):
    context.driver.quit()
