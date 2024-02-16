# file:features/tutorial01_basics.feature
Feature: Showing off behave (tutorial01)

  Scenario: Run a simple test
    Given person is in dark forrest with "matches"
    When we start a fire
    And we drop the firestarter
    Then it is less dark
    And we still have the "matches"

  Scenario: Go to forrest with matches
    Given person is in dark forrest with "lighter"
    When we start a fire
    Then it is less dark
    And we still have the "matches"
#
#  Scenario: Run a simple test 2
#    Given we have behave installed
#    When we implement a test
#    Then behave will test it for us!