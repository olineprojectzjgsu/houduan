from django.urls import path
from . import views
urlpatterns = [
    path('update_userinfo',views.update_UserInfo),
]