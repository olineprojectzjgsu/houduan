from email.policy import default
from django.db import models

# Create your models here.
class UserAddressInfo(models.Model):
    province = models.CharField("省份",max_length=50,default="浙江")
    city = models.CharField("城市",max_length=50,default="杭州")
    address = models.CharField("地址",max_length=100,default="浙江工商大学")
    date = models.DateField(auto_now_add = True)
    longtitude = models.CharField(max_length=20,default='10.11')
    latitiude = models.CharField(max_length=20,default='10.11')
    district = models.CharField(max_length=10,default="钱塘区")
    street = models.CharField(max_length=20,default="白杨街道")
    detail_addr = models.CharField(max_length=100,default='浙江工商大学下沙校区')
    default_addr = models.SmallIntegerField(default=1)
    status = models.SmallIntegerField(default=1)
    add_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

class Book_Info(models.Model):
    remark = models.CharField("评论",max_length=100)
    sale = models.DecimalField("售价",max_digits=11,decimal_places=2,default='')
    address = models.CharField("地址",max_length=50)
    is_active = models.BooleanField(default=True)

class Shopping_cart(models.Model):
    product_name = models.CharField("外卖名字",max_length=50,default='')
    delivery_info = models.BooleanField("是否到达",default=False)
    is_active = models.BooleanField(default=True)


class Info_deliver(models.Model):
    advertise = models.TextField("推荐广告",max_length=200,default='')
    is_active = models.BooleanField(default=True)



class GetAddress(models.Model):
    address = models.CharField("地址",max_length=50,default='')
    phone_number = models.CharField("买家电话号码",max_length=11,default='')
    name = models.CharField("买家名字",max_length=20,default='') 
    is_active = models.BooleanField(default=True)
