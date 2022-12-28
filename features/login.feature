@instagram
Feature: Validate the login Functionality of Instagram

    Background:
        Given app is launched

    @login
    Scenario: Verify the login Functionality of Instagram with valid credentials
        When user clicks login link
        And user attempts to login with valid credentials
