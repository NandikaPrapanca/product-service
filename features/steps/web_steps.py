from behave import when, then
import requests

@when('I request all products')
def step_list_all(context):
    context.response = requests.get(f"{context.base_url}/products")

@then('I should see a list of products')
def step_see_list(context):
    assert context.response.status_code == 200


@when('I search products by name')
def step_search_name(context):
    name = "Hammer"
    context.response = requests.get(f"{context.base_url}/products?name={name}")

@then('I should see matching products')
def step_match_products(context):
    assert context.response.status_code == 200


@when('I search products by category')
def step_search_category(context):
    category = "tools"
    context.response = requests.get(f"{context.base_url}/products?category={category}")

@when('I search products by availability')
def step_search_available(context):
    context.response = requests.get(f"{context.base_url}/products?available=true")


@when('I search for a product by name')
def step_read_product(context):
    name = "Hammer"
    context.response = requests.get(f"{context.base_url}/products?name={name}")

@then('I should see the product details')
def step_see_details(context):
    assert context.response.status_code == 200


@when('I update a product')
def step_update_product(context):
    update_data = {"price": 99.9}
    context.response = requests.put(f"{context.base_url}/products/1", json=update_data)

@when('I delete a product')
def step_delete_product(context):
    context.response = requests.delete(f"{context.base_url}/products/1")