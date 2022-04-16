from django.shortcuts import render
from .models import UserInfo
from django.http import JsonResponse
import json
# Create your views here.

def update_UserInfo(request):
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
