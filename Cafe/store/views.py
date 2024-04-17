from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


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

def login_user(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged in"))
            return redirect('index')
        else:
            messages.success(request, ("There was an error, please try again."))
            return redirect('login')
    else:
        return render(request, 'login.html',context)

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out."))
    return redirect('index')