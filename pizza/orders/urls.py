from . import views
from django.urls import path

urlpatterns=[
    path("",views.index,name="index"),
    path("login",views.login,name="login"),
    path("register",views.register,name="register"),
    path("logout",views.logout,name="logout"),
    path("cart",views.cart,name="cart"),
    path("cart/shopping",views.saveItem,name="shopping"),
    path("remove",views.removeItem,name="removeItem"),
    path("json",views.sendJson,name="json"),
]