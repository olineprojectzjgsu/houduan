from django.urls import path
from django.views import View
from . import views
urlpatterns = [
    path('add_useraddress_info',views.add_useraddress_info),
    path('update_book_describation',views.update_book_describation),
    path('all_useraddress',views.all_useraddress),
    path('get_sure_useraddress',views.get_useraddress),
    path('update_useraddress',views.update_useraddress),
    path('delete_useraddress',views.delete_useraddress),
    path('get_book_info',views.get_book_info),
    path('add_book_info',views.add_book_info),
    path('update_info_deliver',views.update_info_deliver),
    path('delete_info_deliver',views.delete_info_deliver),
    path('update_get_address',views.update_get_address),
    path('delete_get_address',views.delete_get_address),
]