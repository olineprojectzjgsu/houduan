from django.test import TestCase
from django.test import TestCase
from shopping.models import  UserAddressInfo, Book_Info
# Create your tests here.
class Mytest(TestCase):
    def test_case(self):
        UserAddressInfo.objects.create(province="zhejiang",city="jinhua",address="yongkang")
        p = UserAddressInfo.objects.get(address="yongkang")
        print(p.province)
        print(p.city)
        print(p.date)
        Book_Info.objects.create(remark="very bad",sale="10.32",address="yongkang")
        p = Book_Info.objects.get(id="1")
        print(p.remark)
        print(p.sale)
        print(p.address)
