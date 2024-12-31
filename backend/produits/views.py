from django.shortcuts import render
from .models import Produit


# Create your views here.

def index_views(request):
    return render(request, "index.html") 

def views_produit(request):
    #prods = Produit.objects.all()
    prods = {'title':'thiakry','price':'12000'}
     
    return render(request, 'index.html', {'prods':prods})

def viexs_basket(request):
    return render(request)

def create_produit(request):
    if request.method == "POST":
        title=request.POST.get("title")
        type_pro=request.POST.get("type_pro")
        price=request.POST.get("price")

        prod = Produit.objects.create(
            title=title,
            type_pro=type_pro,
            price=price
        )
        prods = prod.save()

    return render(prods)

