Feature: Product Service

Scenario: Read a Product
    Given the following products
    When I search for a product by name
    Then I should see the product details

Scenario: List all Products
    Given the following products
    When I request all products
    Then I should see a list of products

Scenario: Search by Name
    Given the following products
    When I search products by name
    Then I should see matching products

Scenario: Search by Category
    Given the following products
    When I search products by category
    Then I should see matching products

Scenario: Search by Availability
    Given the following products
    When I search products by availability
    Then I should see matching products