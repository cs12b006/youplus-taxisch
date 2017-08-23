from django.shortcuts import render
from .models import Driver
from rest_framework import serializers, viewsets

class DriverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Driver
        fields = ['id']

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

# Create your views here.
