
LOCATORS = {
    'page title': {'by': 'xpath',
                   'locator':
                       '//title[contains(text(), "edX | Free online courses from the world\'s best universities")]'},
    'search field': {'by': 'xpath',
                     'locator': '(//input[@class="js-search-bar edit-search-query form-text tt-input"])[2]'},
    'search button': {'by': 'xpath',
                      'locator': '(//button[@type="submit"])[2]'},
    'results page': {'by': 'xpath',
                     'locator': '//button[@class="facet-option js-clear"]'},
    'register button': {'by': 'xpath',
                        'locator': '//a[@class="btn btn-blue"]'},
    'sign in button': {'by': 'xpath',
                       'locator': '//a[@class="btn "]'}
    }
