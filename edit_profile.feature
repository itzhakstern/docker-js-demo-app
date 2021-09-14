# Created by itzhakshtern at 13/09/2021

Feature: Edit profile in js app
  In order to edit my profile
  As a user
  I want know that the db updated

  Scenario: Edit my profile
    Given I have profile with name "Anna Smith" ,email "anna.smith@example.com", interests "coding"
    When I want edit the profile with name "Itzhak Stern" ,email "sss@example.com", interests "AI"
    Then The data will be update in the data base