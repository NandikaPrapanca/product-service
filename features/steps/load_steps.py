from behave import given
import requests

@given('the following products')
def step_given_products(context):
    """Load products from feature file into the service"""
    context.base_url = "http://localhost:8080"

    for row in context.table:
        payload = {
            "name": row["name"],
            "description": row["description"],
            "price": float(row["price"]),
            "category": row["category"],
            "available": row["available"].lower() == "true"
        }

        response = requests.post(f"{context.base_url}/products", json=payload)
        assert response.status_code == 201