from xmlrpc.client import Boolean
from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField("产品名",max_length=50,default='',unique=True);
    price = models.DecimalField("定价",max_digits=7,decimal_places=2,default=0.0)
    market_price = models.DecimalField("零售价",max_digits=7,decimal_places=2,default=0.0)
    is_active = models.BooleanField("是否在售",default=True)
    saler_id = models.IntegerField("商家ID",default=1)
    sort = models.CharField("产品分类",max_length=50,default="")
    describation = models.TextField("描述",max_length = 288,default='')
    class Meta:
        db_table = 'product'
    def __str__(self):
        return 'name is %s price is %s market_price is %s'%(self.product_name,self.price,self.market_price)
            