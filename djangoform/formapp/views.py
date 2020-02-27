from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .forms import contact

def contactview(request):
    if request.method == 'POST':
        form = contact(request.POST)
        # print(request.body)
    else:
        form = contact()

    if form.is_valid():
                 name=form.cleaned_data['name'] 
                 email=form.cleaned_data['email']
                 print(name,email)
    return render(request,'form.html',{ 'form':form })