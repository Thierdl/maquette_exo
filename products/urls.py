from django.urls import path
from products.views import index_views

urlpatterns=[
    path('', index_views, name='home')
]