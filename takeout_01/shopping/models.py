from email.policy import default
from django.db import models

# Create your models here.
class UserAddressInfo(models.Model):
    province = models.CharField("省份",max_length=50,default="浙江")
    name = models.CharField("名字",max_length=20,default="胡路涯")
    city = models.CharField("城市",max_length=50,default="杭州")
    phone = models.CharField("手机号",max_length=20,default="17816733515")
    address = models.CharField("地址",max_length=100,default="浙江工商大学")
    date = models.DateField(auto_now_add = True)
    district = models.CharField(max_length=10,default="钱塘区")
    street = models.CharField(max_length=20,default="白杨街道")
    detail_addr = models.CharField(max_length=100,default='浙江工商大学下沙校区')
    add_time = models.DateTimeField(auto_now_add=True)
    sex = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

class Book_Info(models.Model):
    _iphone = models.CharField("电话",max_length=100,default="17816733515")
    shopname = models.CharField("店铺",max_length=100,default='蛋糕店')
    money = models.CharField("订单发价",max_length=50,default="441")
    date = models.DateField("发货时间",auto_now=True)
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
class Shop_List(models.Model):
    shopName = models.CharField("店铺名",max_length=30)
    saleNum = models.IntegerField("销量",default=0)
    offerPrice = models.IntegerField("提供的价格",default=0)
    distributionCost = models.IntegerField("分配费用",default=0)
    welfare = models.CharField("福利",max_length=50)
    time = models.CharField("配送时间",max_length=30)
    shopPic = models.CharField("图片地址",max_length=100)
    shopNotice = models.CharField("公告",max_length=100)

class Food_List(models.Model):
    shopId = models.IntegerField("商家Id",default=0)
    foodId = models.CharField("食物Id",max_length=30,default='')
    FoodName = models.CharField("食物名称",max_length=30,default='')
    taste = models.CharField("口味选择",max_length=50,default='')
    saleNum = models.CharField("销量",max_length=20,default='')
    price = models.IntegerField("价格",default=0)
    count = models.IntegerField("计数",default=0)
    foodPic = models.CharField("图片地址",max_length=100)
    


