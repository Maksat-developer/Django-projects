from rest_framework import serializers
from .models import Action


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = ['name', 'pub_date', 'in_stock', 'product']



    