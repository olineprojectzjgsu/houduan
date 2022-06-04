from curses.ascii import NUL
import json
from multiprocessing.dummy import Array
from re import A
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from pymysql import NULL
from shopping.models import *
def all_useraddress(request):
    if request.method == "GET":
        all_useraddress = UserAddressInfo.objects.values()
        UserAddressInfo_json = list(all_useraddress)
        return JsonResponse({"ret":0,"data": UserAddressInfo_json})
def get_useraddress(request):
    if request.method == "POST":
        request.params = json.loads(request.body)
        data = request.params["data"]
        try:
            select_useraddress = UserAddressInfo.objects.filter(id = data['id']).values()
        except UserAddressInfo.DoesNotExist:
            return{
                'ret':1,
                'msg':'数据不存在'
            }
        print(select_useraddress)
        useraddress_json = list(select_useraddress)
        print(useraddress_json)
        
        return JsonResponse({'ret':0,'data':useraddress_json})
def update_useraddress(request):
    if request.method == 'PUT':
        request.params = json.loads(request.body)
        newdata = request.params['newdata']
        try:
            select_product = UserAddressInfo.objects.get(id=newdata['id'])
        except UserAddressInfo.DoesNotExist:
            return{
                'ret':1,
                'msg': "数据不存在"
            }
        if 'province' in newdata:
            select_product.province = newdata['province']
        if 'city' in newdata:
            select_product.city = newdata['city'] 
        if 'address' in newdata:
            select_product.address = newdata['address'] 
        if 'date' in newdata:
            select_product.date = newdata['date'] 
        if 'detail_addr' in newdata:
            select_product.detail_addr = newdata['detail_addr']
        select_product.save()
    return JsonResponse({"ret":0})

def add_useraddress_info(request):
    if request.method == 'POST':
        request.params = json.loads(request.body)
        info = request.params['data']
        print(info)
        new_product = UserAddressInfo.objects.create(
            name=info['name'],
            city = info['city'],
            detail_addr = info['detail_addr'],
            phone = info['phone'],
        )
    return JsonResponse({"ret":0,"id":new_product.id})
def delete_useraddress(request):
     if request.method == 'DELETE':
        request.params = json.loads(request.body)
        info = request.params['data']
        try:
            select_product = UserAddressInfo.objects.get(id=info['id'])
        except UserAddressInfo.DoesNotExist:
            return{
                'ret':1,
                'msg': "数据不存在"
            }
        select_product.is_active = False
        select_product.save()
        return JsonResponse({'ret':0})   

def get_book_info(request):
    if request.method == 'POST':
        request.params = json.loads(request.body)
        info = request.params['data']
        try:
            select_book = Book_Info.objects.filter(_iphone = info['_phone']).values()
            #选中的订单
        except Book_Info.DoesNotExist:
            return{
                'ret':1,
                'msg': "数据不存在"
            }
        book_info = list(select_book)
        return JsonResponse({'ret':0,'data':book_info})
    return JsonResponse({"ret":0})
def add_book_info(request):
    if request.method == 'POST':
        request.params = json.loads(request.body)
        info = request.params['data']
        new_book = Book_Info.objects.create(
            _phone = info['username'],
            shopname = info['shopname'],
            money = info['money']
        )
        return JsonResponse({'ret':0,'id':new_book.id})   
def update_shopping_cart(request):
    if request.method == 'PUT':
        request.params = json.loads(request.body)
        newdata = request.params['newdata']
        try:
            select_shopping_cart = Shopping_cart.objects.get(id=newdata['id'])
            #选中的订单
        except Shopping_cart.DoesNotExist:
            return{
                'ret':1,
                'msg': "数据不存在"
            }
        if 'product_name' in newdata:
            select_shopping_cart.product_name = newdata['product_name']
        if 'delivery_info' in newdata:
            select_shopping_cart.delivery_info = newdata['delivery_info'] 
        select_shopping_cart.save()
    return JsonResponse({"ret":0})

def delete_shopping_cart(request):
    if request.method == 'DELETE':
        request.params = json.loads(request.body)
        info = request.params['data']
        try:
            select_shopping_cart = Shopping_cart.objects.get(id=info['id'])
            #选中的订单
        except Shopping_cart.DoesNotExist:
            return{
                'ret':1,
                'msg': "数据不存在"
            }
        select_shopping_cart.is_active = False
        select_shopping_cart.save()
        return JsonResponse({'ret':0})   
def update_info_deliver(request):
    if request.method == 'PUT':
        request.params = json.loads(request.body)
        newdata = request.params['newdata']
        try:
            select_info_deliver = Info_deliver.objects.get(id=newdata['id'])
            #选中的订单
        except Info_deliver.DoesNotExist:
            return{
                'ret':1,
                'msg': "数据不存在"
            }
        if 'advertise' in newdata:
            select_info_deliver.advertise = newdata['advertise']
        select_info_deliver.save()
    return JsonResponse({"ret":0})

def delete_info_deliver(request):
    if request.method == 'DELETE':
        request.params = json.loads(request.body)
        info = request.params['data']
        try:
            select_info_deliver = Info_deliver.objects.get(id=info['id'])
            #选中的订单
        except Info_deliver.DoesNotExist:
            return{
                'ret':1,
                'msg': "数据不存在"
            }
        select_info_deliver.is_active = False
        select_info_deliver.save()
        return JsonResponse({'ret':0})   
def update_get_address(request):
    if request.method == 'PUT':
        request.params = json.loads(request.body)
        newdata = request.params['newdata']
        try:
            select_get_address=GetAddress.objects.get(id=newdata['id'])
            #选中的订单
        except GetAddress.DoesNotExist:
            return{
                'ret':1,
                'msg': "数据不存在"
            }
        if 'address' in newdata:
            select_get_address.address= newdata['address']
        if 'phone_number' in newdata:
            select_get_address.phone_number = newdata['phone_number']
        if 'name' in newdata:
            select_get_address.name = newdata['name']
        select_get_address.save()
    return JsonResponse({"ret":0})

def delete_get_address(request):
    if request.method == 'DELETE':
        request.params = json.loads(request.body)
        info = request.params['data']
        try:
            select_get_address = GetAddress.objects.get(id=info['id'])
            #选中的订单
        except GetAddress.DoesNotExist:
            return{
                'ret':1,
                'msg': "数据不存在"
            }
        select_get_address.is_active = False
        select_get_address.save()
        return JsonResponse({'ret':0})   
def get_sure_shop(request):
    if request.method == 'POST':
        request.params = json.loads(request.body)
        data = request.params['data']
        try:
            select_shop = Shop_List.objects.filter(id = data['id']).values()
        except Shop_List.DoesNotExist:
            return{
                'ret':1,
                'msg':'数据不存在'
            }
        shop_json = list(select_shop)
        return JsonResponse({'ret':0,'data':shop_json})
    
def get_all_shop(request):
    if request == 'POST':
        select_shop = [1,1,1,1,1]
        for i in range(5):
            select_shop[i] = Shop_List.objects.get(id=i)
        
        return JsonResponse({})
def add_shop(request):
    if request == 'POST':
        request.params = json.loads(request.body)
        info = request.params['data']
        print(info)
        
