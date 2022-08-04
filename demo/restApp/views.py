from django.shortcuts import render
from rest_framework import viewsets
from .models import vehicleModels as v 
from .serializers import vehicleSerializer as s

# Create your views and viewsets here:
class vehicleViewset(viewsets.ModelViewSet):
    #define the queryset:
    queryset = v.objects.all()

    #specity the serializer set to use:
    serializer_class = s

