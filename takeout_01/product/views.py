import json
from django.shortcuts import render
from django.http import  JsonResponse
from product.models import Product

# Create your views here.

def all_product(request):#查询产品，采用GET请求
    if request.method == 'GET':
        all_product= Product.objects.values()#产品的所有信息
        product_json = list(all_product)#输出产品信息的json格式
        return JsonResponse({'ret':0, 'data': product_json})
def get_sure_product(request):#查询产品，采用GET请求
    if request.method == 'GET':
        request.params = json.loads(request.body)
        info = request.params['data']
        try:
            select_product= Product.objects.filter(id=info['id']).values()#产品的所有信息
        except Product.DoesNotExist:
            return{
                'ret':1,
                'msg': "数据不存在"
            }
        product_json = list(select_product)#输出产品信息的json格式
        return JsonResponse({'ret':0, 'data': product_json})
def add_product(request):
    if request.method == 'POST':
        request.params = json.loads(request.body)
        info = request.params['data']
        print(info)
        for i in info:
            new_product = Product.objects.create(
                product_name=i['product_name'],
                price = i['price'],
                market_price = i['market_price'],
                saler_id = i['saler_id'],
                sort = i['sort'],
                describation = i['describation'],
            )
    return JsonResponse({"ret":0,"id":new_product.id})
def delete_product(request):
    if request.method == 'DELETE':
        request.params = json.loads(request.body)
        info = request.params['data']
        try:
            select_product = Product.objects.get(id=info['id'])
        except Product.DoesNotExist:
            return{
                'ret':1,
                'msg': "数据不存在"
            }
        select_product.is_active = False
        select_product.save()
        return JsonResponse({'ret':0})
def update_product(request):
    if request.method == 'PUT':
        request.params = json.loads(request.body)
        newdata = request.params['newdata']
        try:
            select_product = Product.objects.get(id=newdata['id'])
        except Product.DoesNotExist:
            return{
                'ret':1,
                'msg': "数据不存在"
            }
        if 'product_name' in newdata:
            select_product.product_name = newdata['product_name']
        if 'price' in newdata:
            select_product.price = newdata['price'] 
        if 'market_price' in newdata:
            select_product.market_price = newdata['market_price'] 
        if 'is_active' in newdata:
            select_product.is_active = newdata['is_active'] 
        if 'saler_id' in newdata:
            select_product.saler_id = newdata['saler_id'] 
        if 'sort' in newdata:
            select_product.sort = newdata['sort'] 
        if 'describation' in newdata:
            select_product.describation = newdata['describation'] 
        select_product.save()
        return JsonResponse({'ret':0})

def recover_product(request):
    if request.method == 'POST':
        request.params = json.loads(request.body)
        info = request.params['data']
        try:
            select_product = Product.objects.get(id=info['id'])
        except Product.DoesNotExist:
            return{
                'ret':1,
                'msg': "数据不存在"
            }
        select_product.is_active = True
        select_product.save()
        return JsonResponse({'ret':0})