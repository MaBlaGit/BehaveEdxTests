Feature: Testing basic functionalities edx.org webpage

    @scenario
    Scenario: Check if webpage www.edx.org load correctly

      	Given I open "www.edx.org"
      	Then the "page title" is visible
      	And the "search field" is visible
      	And the "register button" is visible
        And the "sign in button" is visible

    @scenario @outline
    Scenario Outline: Check if user can search the <course> course

        Given I open "www.edx.org"
        And the "search field" is visible
		When I in the "search field" enter <course>
		And I click on the "search button"
		Then the "results page" is loaded with searched <course> courses

		Examples:
		    | course  |
		    | Python  |
            |  Java   |
            | Haskell |
            |  Ruby   |

    @scenario
    Scenario: Check if selected course page is loaded correctly

		Given I open "www.edx.org"
		And "view_all_courses" button is visible
		When I click on "view_all_courses" button
        And I select "course page" avatar
        Then the "course page" page is visible
