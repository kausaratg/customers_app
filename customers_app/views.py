from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status = 'pending').count()
    
    context = {'orders':orders, 'customers':customers, 'total_customers':total_customers, 
    'total_orders':total_orders, 'delivered':delivered, 'pending':pending}
    return render(request, 'customers_app/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'customers_app/products.html', context)

def customers(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    orders_count = orders.count()
    context = {'customer':customer, 'orders':orders, 'orders_count':orders_count}
    return render(request, 'customers_app/customers.html', context)
