from django.urls import path
from .import views 

urlpatterns = [
    path('', views.index_views, name='views_produit'),
    path('list/', views.views_produit, name='produit'),

]