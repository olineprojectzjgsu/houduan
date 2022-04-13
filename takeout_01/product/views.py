from itertools import product
from math import prod
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from takeout_django_01.takeout_01.product.models import Product

# Create your views here.
def update_product(request,product_id):
    try:
        product =  Product.objects.get(id=product_id,is_active=True);
    
    except Exception as e:
        print('--update book error is %s'%(e))
        return HttpResponse('--The book is not existed')
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        price = request.POST['price']
        print(price)
        market_price = request.POST['price']
        print(market_price)
        product.price = price
        product.market_price = market_price
        product.save()
        return HttpResponse('change successfully') 
def delete_product(request):
    product_id = request.GET.get('product_id')
    if not product_id:
        return HttpResponse("请求异常")
    try:
        product= Product.objects.get(id=product_id,is_active=True)
    except Exception as e:
        print('----delete book get error is %s'%(e))
        return HttpResponse('---The book id is error')
    product.is_active=False
    product.save()
    pass