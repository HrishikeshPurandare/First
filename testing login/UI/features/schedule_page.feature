Feature: Schedule Page

    Scenario: I can log in with correct credentials and access the schedule page of team
        Given I want to log in to Hudl as Hudl Coach 
        When I log in 
        When I click on Home Button
        When I click on team button
        When I click on Schedule Button 
        Then I should be directed to my schedule page

    