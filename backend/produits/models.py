from django.db import models

# Create your models here.
class category(models.Model):
    pass


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


class save_pro(models.Model):
    pass