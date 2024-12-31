from django.db import models

# Create your models here.
class category(models.Model):
    pass

#models Produits
class Produit(models.Model):
    title = models.TextField(max_length=100)
    type_pro = models.TextField(max_length=100)
    price = models.FloatField()
    date_add = models.DateTimeField(auto_now_add=True)
    #mage models.ImageField(null=True,upload_to="media")
    #note
    #button add

    def __str__(self):
        return f"{self.title} {self.price} {self.type_pro}"

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
