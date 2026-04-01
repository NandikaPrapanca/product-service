import factory
from faker import Faker

fake = Faker()

class ProductFactory(factory.Factory):
    """Creates fake products for testing"""

    class Meta:
        model = dict

    id = factory.Sequence(lambda n: n)
    name = factory.Faker("word")
    description = factory.Faker("sentence")
    price = factory.Faker("pyfloat", left_digits=2, right_digits=2, positive=True)
    category = factory.Iterator(["books", "clothes", "tools", "food"])
    available = factory.Faker("boolean")