from django.db import models

# Create your models here.
class UserInfo(models.Model):
    # CharField类型不能为空,最少要指定一个长度
    #DecimialField表示浮点型数，max_digits表示小数点前最大位数，decimal_places表示小数点后最多位数，并且必须指派一个默认值
    user_name = models.CharField(max_length=32,default='')
    email = models.EmailField(max_length=32)
    pwd = models.CharField(max_length=32,default='')
    phone = models.CharField(max_length=11,default='')
    nickname = models.CharField(max_length=20,default='')

    class Meta:
        db_table = 'userinfo'

    def __str__(self):
        return 'user_name is %s email is %s phone is %s'%(self.user_name,self.email,self.phone)