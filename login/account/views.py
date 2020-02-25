from django.shortcuts import render



def indexView(request):
    return render(request,'account/index.html')

def dashboardView(request):
    return render(request,'account/dashboard.html')

def registerView(request):
    return render(request, 'registration/register.html')