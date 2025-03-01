from django.shortcuts import render, redirect
from .models import Product


def index_views(request):
    return render (request, 'index.html')

def add_product(request):

    if request.method=='POST':
        title=request.POST.get("title")
        content=request.POST.get("content")
        price=request.POST.get("price")
        category=request.POST.get("category")

        Product.objects.create(
            title=title,
            content=content,
            price=price,
            category=category

            )
    
        return redirect
    return render(request, 'add_product.html')
