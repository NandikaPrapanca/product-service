import unittest
from service.models import Product, Category
from service import app
from service.models import db

class TestProductModel(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        db.init_app(app)

        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_product(self):
        product = Product(name="Hammer", description="Tool", price=10.0,
                          category=Category.TOOLS, available=True)
        product.create()

        self.assertIsNotNone(product.id)

    def test_read_product(self):
        product = Product(name="Hammer", description="Tool", price=10.0,
                          category=Category.TOOLS, available=True)
        product.create()

        found = Product.find(product.id)
        self.assertEqual(found.name, "Hammer")

    def test_update_product(self):
        product = Product(name="Hammer", description="Tool", price=10.0,
                          category=Category.TOOLS, available=True)
        product.create()

        product.price = 99.0
        product.update()

        updated = Product.find(product.id)
        self.assertEqual(updated.price, 99.0)

    def test_delete_product(self):
        product = Product(name="Hammer", description="Tool", price=10.0,
                          category=Category.TOOLS, available=True)
        product.create()
        product_id = product.id

        product.delete()

        result = Product.find(product_id)
        self.assertIsNone(result)

    def test_list_all_products(self):
        Product(name="Hammer", description="Tool", price=10.0,
                category=Category.TOOLS, available=True).create()

        products = Product.all()
        self.assertGreater(len(products), 0)

    def test_find_by_name(self):
        Product(name="Hammer", description="Tool", price=10.0,
                category=Category.TOOLS, available=True).create()

        products = Product.find_by_name("Hammer")
        self.assertEqual(len(products), 1)

    def test_find_by_category(self):
        Product(name="Hammer", description="Tool", price=10.0,
                category=Category.TOOLS, available=True).create()

        products = Product.find_by_category(Category.TOOLS)
        self.assertEqual(len(products), 1)

    def test_find_by_availability(self):
        Product(name="Hammer", description="Tool", price=10.0,
                category=Category.TOOLS, available=True).create()

        products = Product.find_by_availability(True)
        self.assertEqual(len(products), 1)