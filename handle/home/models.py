from django.db import models


class department(models.Model):
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    image = models.ImageField(upload_to='image/',default = "default.jpg")
    description = models.TextField(default='')
    
    def __str__(self):
        return self.name

class PhoneNum(models.Model):
    department_name = models.ForeignKey(department, on_delete=models.CASCADE)
    number=models.CharField(max_length=30)

    def __str__(self):
        return self.number
class Food_item(models.Model):
    department_name=models.ForeignKey(department,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    price=models.FloatField()
    image=models.ImageField(upload_to='images/',default='default')
 

     