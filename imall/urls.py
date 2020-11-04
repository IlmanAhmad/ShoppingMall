from . import views
from django.urls import path, include


app_name = 'mall'

urlpatterns = [
    path('', views.basic, name = 'home'),
    path('handlelogin/', views.handlelogin, name = 'handlelogin'),
    path('logout/', views.handlelogout, name = 'handlelogout')
]