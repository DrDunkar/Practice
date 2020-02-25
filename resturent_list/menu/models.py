from django.db import models

class restro_list(models.Model):
    name=models.CharField(max_length=30)
    number=models.CharField(max_length=30)
    image=models.ImageField(upload_to='images/', default='default.jpg')
    address=models.CharField(max_length=30)

    
