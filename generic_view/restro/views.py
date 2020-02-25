from django.views import generic
from .models import Resturent
from .models import Food_Item
class IndexView(generic.ListView):
    model = Resturent
    template_name = 'restro/index.html'

    def get_queryset(self):
        return Resturent.objects.all()

class FoodDetailView(generic.DetailView):
    model = Resturent
    template_name = 'restro/detail.html'        

    # def get_queryset(self):
    #     return Food_Item.objects.all() 