from flask import jsonify, request, abort
from service.models import Product, Category
from service import app

######################################################################
# READ A PRODUCT
######################################################################
@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = Product.find(product_id)
    if not product:
        abort(404)
    return jsonify(product.serialize()), 200

######################################################################
# UPDATE A PRODUCT
######################################################################
@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    product = Product.find(product_id)
    if not product:
        abort(404)

    data = request.get_json()
    product.deserialize(data)
    product.id = product_id
    product.update()

    return jsonify(product.serialize()), 200

######################################################################
# DELETE A PRODUCT
######################################################################
@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    product = Product.find(product_id)
    if product:
        product.delete()
    return "", 204

######################################################################
# LIST ALL PRODUCTS
######################################################################
@app.route("/products", methods=["GET"])
def list_products():
    name = request.args.get("name")
    category = request.args.get("category")
    available = request.args.get("available")

    if name:
        products = Product.find_by_name(name)
    elif category:
        products = Product.find_by_category(Category[category.upper()])
    elif available:
        products = Product.find_by_availability(available.lower() == "true")
    else:
        products = Product.all()

    results = [p.serialize() for p in products]
    return jsonify(results), 200