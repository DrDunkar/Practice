from django.shortcuts import render
def home_view(request):
    restrolist = restro_list.object.all()
    return render(request,'index.html',{'restro':restro_list})

