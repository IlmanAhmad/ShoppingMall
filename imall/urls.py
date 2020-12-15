from . import views
from django.urls import path, include


app_name = 'mall'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('handlelogin/', views.handlelogin, name = 'handlelogin'),
    path('handlesignup/', views.handlesignup, name = 'handlesignup'),
    path('handlelogout/', views.handlelogout, name = 'handlelogout'),
    path('about/', views.about, name = 'about'),
    path('cart/', views.cart, name = 'cart'),
    path('orders/', views.orders, name = 'orders')

]