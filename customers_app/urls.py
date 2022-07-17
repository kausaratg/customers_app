from turtle import update
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customers/<str:pk_test>/', views.customers, name='customers'),
    path('create_order/<str:pk_test>/', views.create_order, name='create_order'),
    path('update_order/<str:pk_test>/', views.update_order, name='update_order'),
    path('delete_order/<str:pk_test>/', views.delete_order, name='delete_order'),
]
