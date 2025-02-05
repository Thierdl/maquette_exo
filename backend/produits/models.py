from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    pass


#models Produits
class Produit(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")

    title = models.TextField(max_length=100)

    price = models.FloatField()
    creaated = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    category=models.CharField(max_length=255, 
        choices=[
            ("Naturel", "Naturel"),
            ("Transformer","Transformer")
        ], default="Category")
    
    #mage models.ImageField(null=True,upload_to="media")
    #note
    #button add

    def __str__(self):
        return f"{self.title} {self.price} {self.category}"

#model Produit_add
class save_pro(models.Model):
    pass

#model_commente
class Commentes(models.Model):
    name = models.TextField(max_length=100)
    email = models.EmailField()
    text = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.name}"
