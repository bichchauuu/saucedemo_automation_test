  Scenario: Complete order flow
    Given the user opens the saucedemo website
    When the user logs in with username "standard_user" and password "secret_sauce"
    Then the user adds the first product to the cart
    And the button changes from 'Add to cart' to 'Remove'
    And the cart icon badge count updates to 1
    When the user navigates to the Cart screen
    Then the product name, description, and price displayed are correct
    When the user clicks the Checkout button
    And fills in the required unique information and clicks continue
    Then the product name, description, and price on the Overview screen are correct
    When the user clicks the Finish button
    Then the Checkout: Complete! page is displayed