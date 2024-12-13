from django.shortcuts import render


def home(request):
    return render(request,'main/home.html')

def create_product(request):
    return render(request,'main/create_product.html')

def edit_product(request):
    return render(request,'main/edit_product.html')

def single_product(request):
    return render(request,'main/single_product')