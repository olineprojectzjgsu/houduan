import email
from user.models import UserInfo 
from django.test import TestCase
# Create your tests here.
class Nytest(TestCase):
    
    def test_case(self):
        UserInfo.objects.create(user_name="sunxiaochuan",email="1210797561@qq.com",pwd="123123",phone="1786733515",nickname="haohaho",user_photo="dadadasd")
        p = UserInfo.objects.get(user_name="sunxiaochuan")
        print(p.user_name)
        print(p.email)
        print(p.pwd)
        print(p.user_photo)
        