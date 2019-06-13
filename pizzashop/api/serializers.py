from rest_framework import serializers

# found in pizza/models.py
from .models import PizzaTopping, Pizza, Topping


class PizzaToppingSerializer(serializers.ModelSerializer):
    # pizzas can have many toppings, but doesn't have to have toppings
    toppings = ToppingsSerializer(many=True, required=False)
    # pizzas can only have one base and it is required
    pizza = PizzaSerializer(many=False, required=True)

    class Meta: 
        model = PizzaTopping
        fields = '__all__' # what is this?

class PizzaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Pizza
        field = '__all__'

class ToppingSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Topping
        field = '__all__'
