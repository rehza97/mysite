from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Product
from django.urls import reverse
# Create your views here.


def products(request):
    product = Product.objects.all()
    context = {
        'page_obj' : product
    }
    return render(request ,'myapp/index.html',context)

def product(request , id):
    pro = Product.objects.get(id = id)
    context = {
        'product' : pro
    }
    return render(request ,'myapp/detail.html',context)   

def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        img = request.FILES.get('upload')
        product = Product(
        name=name ,
        price = price,
        desc = desc,
        img = img,
        )
        product.save()
    return render(request ,'myapp/addproduct.html')   


def update_product(request , id):
    product = Product.objects.get(id = id)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.desc = request.POST.get('desc')
        product.img = request.FILES.get('upload')
        product.save()
        return redirect(reverse('myapp:products'))
    context = {
        'product' : product
    }
    return render(request ,'myapp/addproduct.html',context)


def delete_product(request , id):
    product = Product.objects.get(id = id)
    if request.method == 'POST':
        product.delete()
        return redirect(reverse('myapp:products'))
    context = {
        'product' : product
    }
    return render(request , 'myapp/delete.html',context)
        