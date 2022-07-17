from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm
from django.forms import inlineformset_factory
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

def create_order(request, pk_test):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=3)
    customer = Customer.objects.get(id=pk_test)
    # form = OrderForm(initial={'customer':customer})
    formset = OrderFormSet(queryset = Order.objects.none(), instance=customer)
    if request.method == 'POST':
        # print('printing post: ', request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset':formset}
    return render(request, 'customers_app/order_form.html', context)

def update_order(request, pk_test):
    order = Order.objects.get(id=pk_test)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'customers_app/update_orders.html', context)

def delete_order(request, pk_test):
    order = Order.objects.get(id=pk_test)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    return render(request, 'customers_app/delete.html')