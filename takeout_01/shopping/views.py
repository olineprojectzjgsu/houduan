from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *

def update_useraddress(request, user_address_id):
    try:
        user_address = UserAddressInfo.objects.get(id = user_address_id, is_active = True )
    except Exception as e:
        print('--update useraddress is %s'%(e))
        return HttpResponse('--The user_address is not existed')
    if request.method == 'GET':
        pass#暂时先这样,待会修改
    elif request.method == 'POST':
        province = request.POST['province']
        city = request.POST['city']
        address = request.POST['address']
        print(province,city,address)
        user_address.province = request.POST['province']
        user_address.city= request.POST['city']
        user_address.address= request.POST['address']
        user_address.save()
        return HttpResponse("改变成功")
def delete_useraddress(request):
    user_address_id = request.GET.get('user_address_id')
    if not user_address_id:
        return HttpResponse("请求异常")
    try:
        user_address= user_address.objects.get(id=user_address_id,is_active=True)
    except Exception as e:
        print('----delete book get error is %s'%(e))
        return HttpResponse('---The book id is error')
    user_address.is_active=False
    user_address.save()
    #暂时先这样
    pass
def update_book(request, book_id):
    try:
        book = Book_Info.objects.get(id = book_id, is_active = True )
    except Exception as e:
        print('--update useraddress is %s'%(e))
        return HttpResponse('--The book is not existed')
    if request.method == 'GET':
        pass#暂时先这样,待会修改
    elif request.method == 'POST':
        remark = request.POST['remark']
        sale = request.POST['sale']
        address = request.POST['address']
        print(remark,sale,address)
        book.remark = request.POST['remark']
        book.sale= request.POST['sale']
        book.address= request.POST['address']
        book.save()
        return HttpResponse("改变成功")
def delete_book(request):
    book_id = request.GET.get('book_id')
    if not book_id:
        return HttpResponse("请求异常")
    try:
        book= Book_Info.objects.get(id=book_id,is_active=True)
    except Exception as e:
        print('----delete book get error is %s'%(e))
        return HttpResponse('---The book id is error')
    book.is_active=False
    book.save()
    #暂时先这样