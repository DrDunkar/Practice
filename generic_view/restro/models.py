from django.db import models
from PIL import Image

class Resturent(models.Model):
    name=models.CharField(max_length=30)
    number=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    image=models.ImageField(upload_to='images/',default='default.jpg')

    def __str__(self):
        return self.name

class Food_Item(models.Model):
    Resturent_name = models.ForeignKey(Resturent, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    catagory = models.CharField(max_length=30)
    price = models.FloatField()
    image = models.ImageField(upload_to='images/',default='default')

    