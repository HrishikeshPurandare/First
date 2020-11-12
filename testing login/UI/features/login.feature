Feature: Login Page

    Scenario: I can log in with correct credentials
        Given I want to log in to Hudl as Hudl Coach
        When I log in 
        When I click on Home Button
        Then I should be directed to my home page



    Scenario: I can log in with incorrect credentials
        Given I want to log in to Hudl as Hudl Coach
        When  I log in with wrong credentials 
        Then  I should get error message for wrong credentials


    Scenario: I can reset my password if I am valid user
        Given I want to reset my Hudl Login Password
        When I click on need help button
        When I enter my mail ID
        Then I should get confirmation of sent mail on screen



    # Scenario: I Can create new account on Hudl
    #     Given I want to create new account on hudl as hudl coach
    #     When I click on sign up button
    #     Then I should be directed to my sign up page

    Scenario: I Can login with organisation
        Given I want to login with organisation credentials
        When I enter mail id 
        Then Mail id need to be valid 
        And  I should enter password on next screen

    
    Scenario: I can login with valid credentials
        Given I want to login with valid credentials
        When  I log in
        Then  I should directed to dashboard of analyst 
         

        




         
          

            

    