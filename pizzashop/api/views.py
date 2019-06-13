from rest_framework.views import APIView
from rest_framework.response import Response 
from django.shortcuts import get_object_or_404

from pizza.models import PizzaTopping, Pizza, Topping
from .serializers import PizzaToppingSerializer, ToppingSerializer, PizzaSerializer


class PizzaToppingList(APIView):
    def get(self, request):
        pizzas_topped = PizzaTopping.objects.all()
        data = PizzaToppingSerializer(pizzas_topped, many=True).data
        return Response(data)

class PizzaToppingDetail(APIView):
    def get(self, request, id):
        pizza_topped = get_object_or_404(PizzaTopping, id=id)
        data = PizzaToppingSerializer(pizza_topped).data
        return Response(data)
