from django.shortcuts import render
from django.http import HttpResponse
from .models import department
def display(request):
    department_list = department.objects.all()
    return render(request,'index.html', {'departments': department_list})
    

