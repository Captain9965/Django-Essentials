from rest_framework import serializers

from .models import vehicleModels

class vehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = vehicleModels
        fields = ('model', 'engine_capacity', 'colour')
