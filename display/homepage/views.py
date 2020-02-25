from django.shortcuts import render
from .models import Resturent

def home(request):
    Resturent_list = Resturent.objects.all()
    return render(request,'base.html',{'Resturents':Resturent_list})
