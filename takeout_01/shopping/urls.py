from django.urls import path
from django.views import View
from . import views
urlpatterns = [
    path('add_useraddress_info',views.add_useraddress_info),
    path('all_useraddress',views.all_useraddress),
    path('update_useraddress',views.update_useraddress),
    path('delete_useraddress',views.delete_useraddress),
    path('update_book_info',views.update_book_info),
    path('delete_book_info',views.delete_book_info),
    path('update_info_deliver',views.update_info_deliver),
    path('delete_info_deliver',views.delete_info_deliver),
    path('update_get_address',views.update_get_address),
    path('delete_get_address',views.delete_get_address),
]