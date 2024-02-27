Feature: Showing off behave behave Cucumber with python

  Scenario: Use Magnifying glass to start fire
    Given person is in dark forrest with magnifying glass
    When we start a fire
    Then it is less dark
    When we drop the firestarter
    And we pick up wooden sticks and eat some lasagne
    Then we still have the wooden sticks


  Scenario: Flash light
    Given person is in dark forrest with matches
    When we start a fire
    Then it is less dark
    And we still have the matches
#    And we drop the firestarter

  Scenario: Go to forrest with matches
    Given person is in dark forrest with lighter
    When we start a fire
    Then it is less dark
    And we still have the lighter
