import email
from user.models import UserInfo 
from django.test import TestCase
# Create your tests here.
class Nytest(TestCase):
    
    def test_case(self):
        UserInfo.objects.create(user_name="孙笑川",email="121@qq.com",pwd="123123",phone="1786733515",nickname="我是你哥哥")

        