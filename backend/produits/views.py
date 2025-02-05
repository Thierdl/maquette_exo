from django.shortcuts import render, redirect, get_object_or_404
from .models import Produit




def index_views(request):
    return render(request, "index.html") 


def views_produit(request):
    prods = Produit.objects.all()
    return render(request, 'page/test.html', {'prods':prods})


def create_produit(request):
    if request.method == "POST":
        title=request.POST.get("title")
        type_pro=request.POST.get("type_pro")
        price=request.POST.get("price")

        user=request.user

        prod = Produit.objects.create(

            title=title,
            type_pro=type_pro,
            price=price,
            user=user,
        )

        prod.save()

        return redirect()

    return render(request, "prouct/add.html")



def update_produit(request, id ):
    product=get_object_or_404(Produit, id=id)

    if request.method=="POST":

        title=request.POST.get("title")
        category=request.POST.get("type_pro")
        price=request.POST.get("price")

        product.title=title
        product.category=category
        product.price=price

        product.save()


        return redirect()
    return render(request, "product/update.html")



def delete_produit(request, id):
    del_pro=get_object_or_404(Produit, id=id)
    
    if request.method=="POST":
        del_pro.delete()
        return
    
    return render(request, "product/delete.html")

