from django.test import TestCase
from django.test import TestCase
from shopping.models import  GetAddress, Info_deliver, Shopping_cart, UserAddressInfo, Book_Info
# Create your tests here.
class Mytest(TestCase):

    def test_case(self):
        UserAddressInfo.objects.create(province="zhejiang",city="jinhua",address="yongkang")
        p = UserAddressInfo.objects.get(address="yongkang")
        print(p.province)
        print(p.city)
        print(p.date)
        Book_Info.objects.create(remark="very bad",sale="10.32",address="yongkang")
        p1 = Book_Info.objects.get(id="1")
        print(p1.remark)
        print(p1.sale)
        print(p1.address)
        Shopping_cart.objects.create(product_name="huangmenjia",delivery_info=True)  
        p2 = Shopping_cart.objects.get(product_name="huangmenjia")
        print(p2.delivery_info)
        Info_deliver.objects.create(advertise="huangmenjia")  
        p3 = Info_deliver.objects.get(advertise="huangmenjia")
        print(p3.advertise)
        GetAddress.objects.create(address="jinhua",phone_number="12345678901",name="jiliu")
        p4 = GetAddress.objects.get(name="jiliu")
        print(p4.address)
        print(p4.phone_number)