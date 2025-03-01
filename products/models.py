from django.db import models

class CategoryProduct(models.Model):
    TYPE_PRO={
        "Origin végétal":"Origin végétal",
        "Origin animal":"Origin animal",
        "Produti Transformé":"Produti Transformé",
    }

    category=models.CharField(max_length=18, choices=TYPE_PRO)



class Product(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField(max_length=255)
    price=models.FloatField()
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    #star=models.IntergerField(default=0)
    category=models.ForeignKey(
                    CategoryProduct,  
                    on_delete=models.CASCADE, 
                    related_name="product",
                     
                    )
    #image=models.ImageField()
    
  
