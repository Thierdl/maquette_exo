from django.contrib import admin
from .models import Produit, Category, Commentes
# Register your models here.
admin.site.register(Produit)
admin.site.register(Category)
admin.site.register(Commentes)