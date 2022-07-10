from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'customers_app/dashboard.html')

def products(request):
    return render(request, 'customers_app/products.html')

def customers(request):
    return render(request, 'customers_app/customers.html')
