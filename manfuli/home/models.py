from django.db import models

class user(models.Model):
    Name=models.CharField(max_length=30)
    Contact_Number=models.CharField(max_length=30)
    Email=models.EmailField(max_length=30)

class Address(models.Model):
    street = models.TextField()
    city = models.TextField()
    province = models.TextField()
    code = models.TextField()