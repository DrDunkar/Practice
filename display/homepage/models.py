from django.db import models

class Resturent(models.Model):
    Name=models.CharField(max_length=30)
    Number=models.CharField(max_length=30)
    Vat_no = models.CharField(max_length=30)
    Address=models.CharField(max_length=30)
    Image=models.ImageField(upload_to='images', default="default.jpg")
    # Image=models.ImageField(upload_to='images/', blank=False , null=False)
 