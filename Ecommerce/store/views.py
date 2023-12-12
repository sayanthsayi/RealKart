from django.shortcuts import render
from . models import *

# Create your views here.

def Home(req):
    category=Category.objects.all()

    context={'category':category}   
    return render(req,"store/home.html",context)

def Brands(request,slug):
    category=Category.objects.all()
    category1=Category.objects.filter(slug=slug)
    subCategory=SubCategory.objects.filter(category__slug=slug)
    product=Product.objects.filter(category__slug=slug)


    context={'category':category,'product':product,"subCategory":subCategory,}  
    return render(request,"store/brands.html",context)

def ProductView(request,slug):
    category=Category.objects.all()
    category1=Category.objects.filter(slug=slug)
    product = Product.objects.filter(slug=slug)
    productSeries=ProductSeries.objects.filter(product__slug=slug)

    context={'category':category,'product':product,'productSeries':productSeries}  
    return render(request,"store/productview.html",context)