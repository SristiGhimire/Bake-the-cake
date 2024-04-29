from django.urls import path
from . views import ShopListView, ShopRetrieveUpdatedelete 

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('login', views.login, name='login'),
    path('contact', views.contact, name='contact'),

    path('shop', views.shop, name='shop'),
    path('shop/',ShopListView.as_view(), name = "shop_listview"),
    path('shop/<int:pk>/',ShopRetrieveUpdatedelete.as_view(), name = "shop_Updatedelete"),


    path('product/<int:id>/', views.product, name='product'),
    path('decoration', views.decoration, name='decoration'),
    path('decorationdetail/<int:id>/', views.decorationdetail, name='decorationdetail'),
    # path('cake', views.cake, name='cake'),
    # path('brownie', views.brownie, name='brownie'),
    # path('weddingcake', views.weddingcake, name='weddingcake'),
    # path('cupcake', views.cupcake, name='cupcake'),
    path('search/', views.searchbar, name='search'),
    path('signup', views.signup, name='signup'),
    path('userlogout/', views.userlogout, name = 'userlogout'),
    path('error', views.error, name='error'),
]
