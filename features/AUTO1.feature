Feature: Search
  @search_page
  Scenario: search_page
    Given a user is in the search page
    When the user filters the car model and the user sorts the price higher to lower
    Then verify the filtered and sorted data