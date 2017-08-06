Feature: Testing basic functionalities edx.org webpage

    @scenario_1
    Scenario: Check if webpage www.edx.org load correctly

      	Given I open "www.edx.org"
      	Then the "page title" is visible
      	And the "search field" is visible
      	And the "register button" is visible
        And the "sign in button" is visible

    @scenario_2
    Scenario Outline: Check if user can search the <course> course

        Given I open "www.edx.org"
        And the "search field" is visible
	    When I in the "search field" enter <course>
	    And I click on the "search"
	    Then the "results page" is loaded with searched <course> courses

		Examples:
		    | course  |
		    | Python  |
            |  Java   |
            | Haskell |
            |  Ruby   |

    @scenario_3
    Scenario: Check if selected course page is loaded correctly

	    Given I open "www.edx.org"
	    And the "view all courses" is visible
	    When I click on the "view all courses" button
        And I select "course page avatar"
        Then the "enroll button" is visible

    @scenario_4
    Scenario: Check if most related results of "search field" drop down menu are clickable and redirects
              to course web page.

	    Given I open "www.edx.org"
	    And the "search field" is visible
	    When I in the "search field" enter "Python"
        And The "drop down menu" is visible
	    And I click on the "first result" from the drop down list
	    Then the "enroll button" is visible
