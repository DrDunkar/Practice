from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    # return HttpResponse('<h3>hello world <h3>')
    return render(request,'index.html')
# Create your views here.
