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
    productSeries=ProductSeries.objects.filter(subcategory__slug=slug)

    all=[]
    for p in product:
        value =100-(p.Original_price/p.selling_price)*100
        off_price = value
        all.append(value)

    context={'category':category,'product':product,"subCategory":subCategory,"productseries":productSeries,"all":all,}  
    return render(request,"store/brands.html",context)

def ProductView(request,slug):
    category=Category.objects.all()
    product = Product.objects.filter(slug=slug)

    context={'category':category,'product':product}  
    return render(request,"store/productview.html",context)