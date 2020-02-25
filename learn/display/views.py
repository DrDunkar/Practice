from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    # return HttpResponse('<h3>hello world <h3>')
    # return render(request,'index.html'),
    # return render(request,'onclick.html')
    return render(request,'pic.html')

# Create your views here.
