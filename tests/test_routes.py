import unittest
from service import app
from service.models import db, Product, Category

class TestProductRoutes(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        self.client = app.test_client()

        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def create_product(self):
        product = Product(
            name="Hammer",
            description="Tool",
            price=10.0,
            category=Category.TOOLS,
            available=True
        )
        product.create()
        return product

    def test_read_product(self):
        product = self.create_product()
        resp = self.client.get(f"/products/{product.id}")
        self.assertEqual(resp.status_code, 200)

    def test_update_product(self):
        product = self.create_product()
        resp = self.client.put(
            f"/products/{product.id}",
            json={"price": 99.0}
        )
        self.assertEqual(resp.status_code, 200)

    def test_delete_product(self):
        product = self.create_product()
        resp = self.client.delete(f"/products/{product.id}")
        self.assertEqual(resp.status_code, 204)

    def test_list_all_products(self):
        self.create_product()
        resp = self.client.get("/products")
        self.assertEqual(resp.status_code, 200)

    def test_list_by_name(self):
        self.create_product()
        resp = self.client.get("/products?name=Hammer")
        self.assertEqual(resp.status_code, 200)

    def test_list_by_category(self):
        self.create_product()
        resp = self.client.get("/products?category=TOOLS")
        self.assertEqual(resp.status_code, 200)

    def test_list_by_availability(self):
        self.create_product()
        resp = self.client.get("/products?available=true")
        self.assertEqual(resp.status_code, 200)