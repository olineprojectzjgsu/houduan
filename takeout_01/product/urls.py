from django.urls import path
from . import views
urlpatterns = [
    path('all_product',views.all_product),
    path('update_product',views.update_product),
    path('delete_product',views.delete_product),
    path('add_product',views.add_product),
    path('get_sure_product',views.get_sure_product),
    path('recover_product',views.recover_product),
]
# p1 = Product(product_name="荔枝",price=32.23,describation="超级甜",saler_id=1,sort="水果")