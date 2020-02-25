from django.db import models

class resturent(models.Model):
    Name=models.CharField(max_length=30)
    Image=models.ImageField(upload_to='image/')
    Addresses=models.CharField(max_length=30)
    vat_no=models.CharField(max_length=30)



