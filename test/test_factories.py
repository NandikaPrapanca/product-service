import unittest
from tests.factories import ProductFactory

class TestFactories(unittest.TestCase):

    def test_product_factory(self):
        product = ProductFactory()

        self.assertIsNotNone(product)
        self.assertIn("name", product)
        self.assertIn("price", product)

if __name__ == "__main__":
    unittest.main()