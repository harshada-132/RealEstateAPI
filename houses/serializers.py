from rest_framework import serializers
from .models import House

class HouseSerializer(serializers.ModelSerializer):
    area = serializers.CharField()
    location = serializers.CharField()

    class Meta:
        model = House
        fields = '__all__'
        
    