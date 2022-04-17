import email
from django.shortcuts import render
from .models import UserInfo
from django.http import JsonResponse
import json
# Create your views here.

def update_userinfo(request):
    if request.method == 'PUT':
        request.params = json.loads(request.body)
        newdata = request.params['newdata']
        try:
            select_user = UserInfo.objects.get(id=newdata['id'])
        except UserInfo.DoesNotExist:
            return{
                'ret':1,
                'msg': "数据不存在"
            }
        print(select_user)
        if 'user_name' in newdata:
            select_user.user_name = newdata['user_name']
        if 'email' in newdata:
            select_user.email = newdata['email'] 
        if 'pwd' in newdata:
            select_user.pwd = newdata['pwd'] 
        if 'phone' in newdata:
            select_user.phone = newdata['phone'] 
        if 'nickname' in newdata:
            select_user.nickname = newdata['nickname'] 
        select_user.save()
    return JsonResponse({"ret":0})
def add_userinfo(request):
    if request.method == 'POST':
        request.params = json.loads(request.body)
        info = request.params["data"]
        print(info)
        new_user = UserInfo.objects.create(
            user_name = info['username'],
            email = info['email'],
            pwd = info['pwd'],
            phone = info['phone'],
            nickname = info['nickname'],
        )
    return JsonResponse({"ret":0,"id":new_user.id})

def login_userinfo(request):
    if request.method == 'GET':
        request.params = json.loads(request.body)
        info = request.params['data']
        try:
            select_userinfo= UserInfo.objects.filter(id=info['id']).values()#产品的所有信息
        except UserInfo.DoesNotExist:
            return{
                'ret':1,
                'msg': "数据不存在"
            }
        userinfo_json= list(select_userinfo)#输出产品信息的json格式
        return JsonResponse({'ret':0, 'data': userinfo_json})