import json
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from product.models import Product

# Create your views here.

def all_product(request):#查询产品，采用GET请求
    if request.method == 'GET':
        all_product= Product.objects.values()#产品的所有信息
        product_json = list(all_product)#输出产品信息的json格式
        return JsonResponse({'ret':0, 'data': product_json})
def update_product(request):
    if request.method == 'POST':
        request.params = json.loads(request.body)
        info = request.params['data']
        new_product = Product.objects.create(product_name=info['product_name'],
            price = info['price'],
            market_price = info['market_price'],
            saler_id = info['saler_id'],
            sort = info['sort'],
            describation = info['describation'],
        )
    return JsonResponse({'ret':0,'id':new_product.id})
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