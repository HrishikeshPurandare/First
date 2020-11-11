Feature: Login Page

    Scenario: I can log in with correct credentials
        Given I want to log in to Hudl as Hudl Coach
        When I log in 
        When I click on Home Button
        Then I should be directed to my home page

    