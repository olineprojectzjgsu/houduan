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