
LOCATORS = {
    'page title': {'by': 'xpath',
                   'locator':
                       '//title[contains(text(), "edX | Free online courses from the world\'s best universities")]'},
    'search field': {'by': 'xpath',
                     'locator': '(//input[@class="js-search-bar edit-search-query form-text tt-input"])[2]'},
    'search': {'by': 'xpath',
               'locator': '(//button[@type="submit"])[2]'},
    'results page': {'by': 'xpath',
                     'locator': '//button[@class="facet-option js-clear"]'},
    'register button': {'by': 'xpath',
                        'locator': '//a[@class="btn btn-blue"]'},
    'sign in button': {'by': 'xpath',
                       'locator': '//a[@class="btn "]'},
    'view all courses': {'by': 'xpath',
                         'locator': '(//a[@class="btn btn-blue js-view-all"])[2]'},

    'course page avatar': {'by': 'xpath',
                           'locator': '(//div[@class="discovery-card-inner-wrapper"])[1]'},
    'enroll button': {'by': 'xpath',
                      'locator': '(//a[@class="btn btn-cta txt-center js-enroll-btn "])[1]'},

    'drop down menu': {'by': 'xpath',
                       'locator': '//h3[@class="league-name"]'},

    'first result': {'by': 'xpath',
                     'locator': '//div[@class="tt-dataset-course"]'}
    }
