from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from product.models import Product

# Create your views here.

def all_product(request):
    if request.method == 'GET':
        all_product= Product.objects.values()#产品的所有信息
        product_json = list(all_product)#输出产品信息的json格式
        return JsonResponse({'ret':0, 'retlist': product_json})
def update_product(request,product_id):
    try:
        product =  Product.objects.get(id=product_id,is_active=True);
    
    except Exception as e:
        print('--update product error is %s'%(e))
        return HttpResponse('--The product is not existed')
    if request.method == 'GET':
        pass
        #暂时先这样
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