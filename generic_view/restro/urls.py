from django.urls import path
from . import views
urlpatterns = [
    path('', views.IndexView.as_view()),
    path('food/<int:pk>', views.FoodDetailView.as_view(), name="food-detail"),
]