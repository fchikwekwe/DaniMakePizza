from django.urls import path

from .views import PizzaToppingList, PizzaToppingDetail

urlpatterns = [
    path('pizzatoppings/', PizzaToppingList.as_views(), name="pizza_toppings_list"),
    path('pizzatoppings/<int:id>', PizzaToppingDetail.as_view(), name='pizza_topping_detail')
]