from django.urls import path
from . import views
urlpatterns = [
    path('update_userinfo',views.update_userinfo),
    path('add_userinfo',views.add_userinfo),
    path('login_user',views.login_userinfo),
]