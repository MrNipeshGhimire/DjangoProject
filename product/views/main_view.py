from django.shortcuts import render,redirect
from ..models import product
from django.contrib import messages

def home(request):
    return render(request,'main/home.html')

# FOR INSERTING DATA TO THE DATABASE
def create_product(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        category = request.POST.get("category")
        price = request.POST.get("price")
        image = request.FILES.get("image")
        description = request.POST.get("description")
        pdt = product.objects.create(
            title = title,
            category = category,
            price = price,
            image=image,
            description = description
        )
        pdt.save()
        messages.success(request,'Product Added Successfully')
        return redirect("create")
        
    return render(request,'main/create_product.html')

def edit_product(request):
    return render(request,'main/edit_product.html')

def single_product(request):
    return render(request,'main/single_product.html')