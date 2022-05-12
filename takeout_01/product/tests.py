from itertools import product
from pickletools import markobject
from django.test import TestCase
from product.models import Product
# Create your tests here.
class Mytest(TestCase):
    def test_case(self):
        Product.objects.create(product_name="lizhi",price="12.10",market_price="31.21",saler_id=32,sort="fruit",describation="very good");
        p = Product.objects.get(product_name="lizhi")
        print(p.product_name)
        print(p.price)
        print(p.market_price)
        print(p.saler_id)
        print(p.sort)
        print(p.describation)