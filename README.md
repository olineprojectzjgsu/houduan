# 后端代码介绍 
开发日志:5.5,现在把main和master两块合并
接下来开发github action
## 然后这里是单元测试的模块
首先是对usr类进行了单元测试
在userapp的test.py中设置测试类
```
class Nytest(TestCase):
    
    def test_case(self):
        UserInfo.objects.create(user_name="孙笑川",email="121@qq.com",pwd="123123",phone="1786733515",nickname="我是你哥哥")
```
这次测试失败了
## 经过测试后发现是中文的原因
进行修改
```
class Nytest(TestCase):
    
    def test_case(self):
        UserInfo.objects.create(user_name="sunxiaochuan",email="1210797561@qq.com",pwd="123123",phone="1786733515",nickname="haohaho")
```
## 完成shopping和product部分的测试
```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
lizhi
12.10
31.21
32
fruit
very good
.zhejiang
jinhua
2022-05-12
very bad
10.32
yongkang
True
huangmenjia
jinhua
12345678901
.sunxiaochuan
1210797561@qq.com
123123
##以上为测试用例
```
## 目前端口已全部测试完毕，均已调通
详情请见apifox
5.13
## 目前已自动化测试成功
总结:
一方面是因为之前的依赖过多，导致一些原本不需要的依赖装上去了
另一方面的话mysql的模拟只需要在github action里面模拟出来行了
