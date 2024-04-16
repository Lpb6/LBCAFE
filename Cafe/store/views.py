from django.shortcuts import render
from .models import Product, Category


# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html',context)

def menu(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {"products": products, "categories":categories}
    return render(request, 'menu.html',context)

def checkout(request):
    context = {}
    return render(request, 'checkout.html',context)

def thankyou(request):
    context = {}
    return render(request, 'thankyou.html',context)